#!/usr/bin/env python3
"""
UHNW Portfolio Analysis - Excel Workbook Generator
Run:    python3 build_workbook.py
Output: UHNW_Portfolio_Analysis.xlsx
"""

import csv
import os
from collections import defaultdict
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── PATHS ─────────────────────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
CSV_DIR     = os.path.join(BASE_DIR, "csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "UHNW_Portfolio_Analysis.xlsx")

# ── BRAND COLORS (JPM palette) ────────────────────────────────────────────────
NAVY    = "002D72"
GOLD    = "C8A84B"
WHITE   = "FFFFFF"
LGRAY   = "F2F2F2"
MGRAY   = "D9D9D9"
DGRAY   = "404040"
LBLUE   = "E8EEF7"
GREEN   = "00703C"
RED     = "C00000"
PURPLE  = "7030A0"

# ── HELPER: load CSV ──────────────────────────────────────────────────────────
def load_csv(filename):
    path = os.path.join(CSV_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ── HELPERS: borders ──────────────────────────────────────────────────────────
def _side(color="CCCCCC"):
    return Side(style="thin", color=color)

def thin_border():
    s = _side()
    return Border(left=s, right=s, top=s, bottom=s)

def bottom_border(color=NAVY):
    return Border(bottom=Side(style="medium", color=color))

# ── HELPERS: cell writers ─────────────────────────────────────────────────────
def title_cell(ws, row, col, text, size=13, sub=False):
    """Dark navy header band cell."""
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(name="Calibri", bold=not sub, size=size,
                       color=GOLD if sub else WHITE)
    c.fill      = PatternFill("solid", fgColor=NAVY)
    c.alignment = Alignment(horizontal="center", vertical="center",
                            wrap_text=True)
    return c

def section_cell(ws, row, col, text):
    """Section heading (light blue band)."""
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(name="Calibri", bold=True, size=10, color=NAVY)
    c.fill      = PatternFill("solid", fgColor=LBLUE)
    c.alignment = Alignment(horizontal="left", vertical="center")
    return c

def col_head(ws, row, col, text):
    """Column header row (mid-navy)."""
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(name="Calibri", bold=True, size=9, color=WHITE)
    c.fill      = PatternFill("solid", fgColor="1F5C99")
    c.alignment = Alignment(horizontal="center", vertical="center",
                            wrap_text=True)
    c.border    = thin_border()
    return c

def data_cell(ws, row, col, value, bold=False, size=10,
              align="left", color=DGRAY, fmt=None, bg=None):
    """Standard data cell."""
    c = ws.cell(row=row, column=col, value=value)
    c.font      = Font(name="Calibri", bold=bold, size=size, color=color)
    c.alignment = Alignment(horizontal=align, vertical="center",
                            wrap_text=True)
    if fmt:
        c.number_format = fmt
    c.fill   = PatternFill("solid", fgColor=(bg or WHITE))
    c.border = thin_border()
    return c

def total_cell(ws, row, col, value, fmt=None, color=WHITE):
    """Dark total/summary row cell."""
    c = ws.cell(row=row, column=col, value=value)
    c.font      = Font(name="Calibri", bold=True, size=10, color=color)
    c.fill      = PatternFill("solid", fgColor=NAVY)
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border    = thin_border()
    if fmt:
        c.number_format = fmt
    return c

def note_cell(ws, row, col, text):
    """Small italic footnote cell."""
    c = ws.cell(row=row, column=col, value=text)
    c.font      = Font(name="Calibri", italic=True, size=8, color="888888")
    c.alignment = Alignment(horizontal="left", vertical="center",
                            wrap_text=True)
    return c

# ── HELPERS: layout ───────────────────────────────────────────────────────────
def cw(ws, col, width):
    ws.column_dimensions[get_column_letter(col)].width = width

def rh(ws, row, height):
    ws.row_dimensions[row].height = height

def merge(ws, r1, c1, r2, c2):
    ws.merge_cells(start_row=r1, start_column=c1,
                   end_row=r2, end_column=c2)

def title_band(ws, row, text, ncols, sub_text=None):
    """Full-width title band. Returns next available row."""
    merge(ws, row, 1, row, ncols)
    title_cell(ws, row, 1, text, size=13)
    rh(ws, row, 30)
    row += 1
    if sub_text:
        merge(ws, row, 1, row, ncols)
        title_cell(ws, row, 1, sub_text, size=10, sub=True)
        rh(ws, row, 18)
        row += 1
    # spacer
    rh(ws, row, 8)
    row += 1
    return row

def stripe(i):
    """Alternating row background."""
    return LGRAY if i % 2 == 0 else WHITE

# ══════════════════════════════════════════════════════════════════════════════
# BUILD WORKBOOK
# ══════════════════════════════════════════════════════════════════════════════
wb = Workbook()
wb.remove(wb.active)

ov  = wb.create_sheet("Overview")
pt  = wb.create_sheet("Portfolio Transition")
tax = wb.create_sheet("Tax Analysis")
sbl = wb.create_sheet("SBL Credit")
gp  = wb.create_sheet("Goals Planning")

ov.sheet_properties.tabColor  = NAVY
pt.sheet_properties.tabColor  = "1F5C99"
tax.sheet_properties.tabColor = "B8860B"
sbl.sheet_properties.tabColor = GREEN
gp.sheet_properties.tabColor  = PURPLE

for ws in [ov, pt, tax, sbl, gp]:
    ws.sheet_view.showGridLines = False

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
raw_port    = load_csv("portfolio_transition_analysis.csv")
raw_metrics = load_csv("transition_metrics_comparison.csv")
raw_sbl     = load_csv("sbl_credit_strategy.csv")
raw_timeline = load_csv("transition_timeline.csv")

# Clean portfolio rows: deduplicate current, exclude zero-alloc JPM rows
current_rows = [r for r in raw_port
                if r["Portfolio_Type"] == "Current_Concentrated"
                and r["Sub_Category"] == "US Large Cap Tech"
                or (r["Portfolio_Type"] == "Current_Concentrated"
                    and r["Asset_Class"] == "Cash & Equivalents")]

# Keep unique sub-categories for current
seen = set()
current_rows_clean = []
for r in raw_port:
    if r["Portfolio_Type"] == "Current_Concentrated" and float(r["Market_Value_USD"]) > 0:
        key = r["Sub_Category"]
        if key not in seen:
            seen.add(key)
            current_rows_clean.append(r)
# Manual override: correct sub-category labels
for r in current_rows_clean:
    if r["Sub_Category"] == "Technology Sector":
        r["Sub_Category"] = "US Large Cap Tech (90% Concentration)"

jpm_rows = [r for r in raw_port
            if r["Portfolio_Type"] == "JPM_Diversified"
            and float(r["Allocation_Percent"]) > 0]

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
ws = ov
NCOLS = 6

for col, w in [(1, 3), (2, 30), (3, 20), (4, 20), (5, 20), (6, 3)]:
    cw(ws, col, w)

row = title_band(
    ws, 1,
    "UHNW PORTFOLIO TRANSITION ANALYSIS",
    NCOLS,
    "$25M Tech Founder Case Study  |  Concentrated Equity to Institutional Diversification  |  February 2026"
)

# ── Client Profile ────────────────────────────────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2, "  CLIENT PROFILE")
rh(ws, row, 18)
row += 1

profile = [
    ("Client Segment",     "Ultra High Net Worth (UHNW)  |  $10M+ Investable Assets"),
    ("Portfolio Value",    "$25,000,000"),
    ("Client Type",        "Technology Founder / Entrepreneur"),
    ("Primary Challenge",  "90% portfolio concentration in single tech sector; $18.5M unrealized gains"),
    ("Primary Objective",  "De-risk position, generate income, fund $10M Private Foundation"),
]
for i, (label, val) in enumerate(profile):
    bg = stripe(i)
    data_cell(ws, row, 2, label, bold=True, bg=bg, color=NAVY)
    merge(ws, row, 3, row, 5)
    data_cell(ws, row, 3, val, bg=bg, align="left")
    rh(ws, row, 16)
    row += 1

rh(ws, row, 8); row += 1

# ── Key Outcomes ──────────────────────────────────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2, "  KEY OUTCOMES: CURRENT vs. OPTIMIZED DIVERSIFIED MODEL")
rh(ws, row, 18); row += 1

for col, label in [(2, "Metric"), (3, "Current Portfolio"), (4, "Optimized Model"), (5, "Improvement")]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

outcomes = [
    ("Asset Classes",               "2",            "7",            "+5 Classes"),
    ("Portfolio Beta",              "1.35",         "0.88",         "-34.8%"),
    ("Value at Risk (95%)",         "$4,250,000",   "$1,875,000",   "-55.9%"),
    ("Maximum Drawdown (Est.)",     "45.0%",        "22.0%",        "-51.1%"),
    ("Concentration Risk Score",    "95 / 100",     "15 / 100",     "-84.2%"),
    ("Sharpe Ratio",                "0.38",         "0.68",         "+78.9%"),
    ("Annual Portfolio Income",     "$112,500",     "$625,000",     "+455%"),
    ("Correlation to S&P 500",      "0.94",         "0.68",         "-27.7%"),
    ("Number of Holdings",          "8",            "145",          "+1,713%"),
]
for i, (metric, curr, jpm_val, chg) in enumerate(outcomes):
    bg = stripe(i)
    data_cell(ws, row, 2, metric, bold=True, bg=bg)
    data_cell(ws, row, 3, curr,    bg=bg, align="center", color=RED)
    data_cell(ws, row, 4, jpm_val, bg=bg, align="center", color=GREEN)
    # Color improvement: green for reductions in risk, green for increases in return
    data_cell(ws, row, 5, chg,     bg=bg, align="center", bold=True, color=GREEN)
    rh(ws, row, 15); row += 1

rh(ws, row, 8); row += 1

# ── Recommendation Summary ────────────────────────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2, "  RECOMMENDATION SUMMARY")
rh(ws, row, 18); row += 1

for col, label in [(2, "Phase / Topic"), (3, "Action & Rationale")]:
    col_head(ws, row, col, label)
merge(ws, row, 3, row, 5)
rh(ws, row, 16); row += 1

recs = [
    ("Phase 1  (Months 1-6)",
     "Systematic liquidation of tech concentration across 5 tranches ($4.5M each). "
     "Tax liability: est. $4.625M. Coordinate installment structure with CPA."),
    ("Phase 2  (Months 7-12)",
     "Redeploy into optimized diversified model: 55% public equity, 23% fixed income, "
     "20% alternatives (PE + Real Estate), 2% cash."),
    ("Phase 3  (Months 13-18)",
     "Establish $5M SBL credit facility against diversified portfolio. "
     "Seed Private Foundation without triggering additional capital gains."),
    ("Tax Strategy",
     "$850K tax-loss harvesting offset identified. DAF and Opportunity Zone "
     "structures available to further reduce net liability."),
    ("Goals-Based Planning",
     "9.8% base-case expected return projects portfolio to $65M+ at Year 20. "
     "Foundation fully self-sustaining within 10 years."),
]
for i, (phase, desc) in enumerate(recs):
    bg = stripe(i)
    data_cell(ws, row, 2, phase, bold=True, bg=bg, color=NAVY)
    merge(ws, row, 3, row, 5)
    data_cell(ws, row, 3, desc, bg=bg, align="left")
    rh(ws, row, 30); row += 1

rh(ws, row, 8); row += 1
merge(ws, row, 2, row, 5)
note_cell(ws, row, 2,
    "Navigate tabs:  Portfolio Transition  |  Tax Analysis  |  SBL Credit  |  Goals Planning    "
    "Prepared by: Mario Enrique Mercado  |  Confidential  |  February 2026")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: PORTFOLIO TRANSITION
# ══════════════════════════════════════════════════════════════════════════════
ws = pt
NCOLS = 7

for col, w in [(1, 3), (2, 28), (3, 16), (4, 16), (5, 16), (6, 16), (7, 3)]:
    cw(ws, col, w)

row = title_band(
    ws, 1,
    "PORTFOLIO TRANSITION ANALYSIS",
    NCOLS,
    "From Concentrated Risk to Institutional Diversification  |  $25M Portfolio  |  February 2026"
)

# ── Section A: Asset Allocation ───────────────────────────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2, "  SECTION A: ASSET ALLOCATION COMPARISON")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Asset Class / Sub-Category"),
    (3, "Current\nAlloc %"),
    (4, "Current\nValue ($)"),
    (5, "Optimized Model\nAlloc %"),
    (6, "Optimized Model\nValue ($)"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 28); row += 1

# Group JPM rows by asset class
jpm_by_class = defaultdict(list)
for r in jpm_rows:
    jpm_by_class[r["Asset_Class"]].append(r)

# All asset classes (current first, then JPM-only)
curr_classes = list({r["Asset_Class"] for r in current_rows_clean})
jpm_classes  = list(jpm_by_class.keys())
all_classes  = curr_classes + [c for c in jpm_classes if c not in curr_classes]

for ac in sorted(all_classes):
    curr_ac = [r for r in current_rows_clean if r["Asset_Class"] == ac]
    jpm_ac  = jpm_by_class.get(ac, [])

    curr_alloc = sum(float(r["Allocation_Percent"]) for r in curr_ac)
    curr_val   = sum(float(r["Market_Value_USD"])   for r in curr_ac)
    jpm_alloc  = sum(float(r["Allocation_Percent"]) for r in jpm_ac)
    jpm_val    = sum(float(r["Market_Value_USD"])   for r in jpm_ac)

    # Asset class subtotal row
    data_cell(ws, row, 2, ac, bold=True, bg=LBLUE, color=NAVY)
    data_cell(ws, row, 3, curr_alloc / 100 if curr_alloc else None,
              bold=True, bg=LBLUE, align="center", fmt="0.0%")
    data_cell(ws, row, 4, curr_val if curr_val else None,
              bold=True, bg=LBLUE, align="right", fmt='$#,##0')
    data_cell(ws, row, 5, jpm_alloc / 100 if jpm_alloc else None,
              bold=True, bg=LBLUE, align="center", fmt="0.0%")
    data_cell(ws, row, 6, jpm_val if jpm_val else None,
              bold=True, bg=LBLUE, align="right", fmt='$#,##0')
    rh(ws, row, 16); row += 1

    # Sub-category detail rows
    all_subs = sorted({r["Sub_Category"] for r in curr_ac + jpm_ac})
    for i, sub in enumerate(all_subs):
        cr = next((r for r in curr_ac if r["Sub_Category"] == sub), None)
        jr = next((r for r in jpm_ac  if r["Sub_Category"] == sub), None)
        bg = stripe(i)
        data_cell(ws, row, 2, f"    {sub}", bg=bg, size=9)
        data_cell(ws, row, 3,
                  float(cr["Allocation_Percent"]) / 100 if cr else None,
                  bg=bg, align="center", fmt="0.0%", size=9,
                  color=RED if cr else DGRAY)
        data_cell(ws, row, 4,
                  float(cr["Market_Value_USD"]) if cr else None,
                  bg=bg, align="right", fmt='$#,##0', size=9,
                  color=RED if cr else DGRAY)
        data_cell(ws, row, 5,
                  float(jr["Allocation_Percent"]) / 100 if jr else None,
                  bg=bg, align="center", fmt="0.0%", size=9,
                  color=GREEN if jr else DGRAY)
        data_cell(ws, row, 6,
                  float(jr["Market_Value_USD"]) if jr else None,
                  bg=bg, align="right", fmt='$#,##0', size=9,
                  color=GREEN if jr else DGRAY)
        rh(ws, row, 13); row += 1

# Grand total row
total_cell(ws, row, 2, "TOTAL PORTFOLIO VALUE")
total_cell(ws, row, 3, 1.0,      fmt="0.0%")
total_cell(ws, row, 4, 25000000, fmt='$#,##0')
total_cell(ws, row, 5, 1.0,      fmt="0.0%")
total_cell(ws, row, 6, 25000000, fmt='$#,##0')
rh(ws, row, 18); row += 2

# ── Section B: Risk & Return Metrics ─────────────────────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2, "  SECTION B: RISK & RETURN METRICS COMPARISON")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Metric"), (3, "Category"),
    (4, "Current Portfolio"), (5, "Optimized Model"), (6, "Change / Improvement"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

# Filter to display-worthy categories
display_cats = ["Portfolio Risk", "Return Metrics", "Diversification", "Income Generation"]
display_metrics = [r for r in raw_metrics if r["Metric_Category"] in display_cats]

for i, r in enumerate(display_metrics):
    bg    = stripe(i)
    unit  = r["Unit"]
    curr  = r["Current_Concentrated"]
    jpm_v = r["JPM_Diversified"]
    impr  = r["Improvement_Percent"]
    direc = r["Change_Direction"]

    if unit == "Percent":
        cd, jd = f"{float(curr):.1f}%", f"{float(jpm_v):.1f}%"
    elif unit == "USD":
        cd, jd = f"${float(curr):,.0f}", f"${float(jpm_v):,.0f}"
    elif unit == "Sharpe_Ratio":
        cd, jd = curr, jpm_v
    elif unit == "Ratio":
        cd, jd = curr, jpm_v
    elif unit == "Coefficient":
        cd, jd = curr, jpm_v
    else:
        cd, jd = curr, jpm_v

    try:
        chg_str = f"{'↓' if direc == 'Decrease' else '↑'} {float(impr):.1f}%"
    except ValueError:
        chg_str = "—"

    # Risk reductions and return increases are both green
    risk_decrease  = direc == "Decrease" and r["Metric_Category"] == "Portfolio Risk"
    return_increase = direc == "Increase"
    chg_color = GREEN if (risk_decrease or return_increase) else RED

    data_cell(ws, row, 2, r["Metric_Name"], bold=True, bg=bg)
    data_cell(ws, row, 3, r["Metric_Category"], bg=bg, align="center", size=9)
    data_cell(ws, row, 4, cd, bg=bg, align="center", color=RED)
    data_cell(ws, row, 5, jd, bg=bg, align="center", color=GREEN)
    data_cell(ws, row, 6, chg_str, bold=True, bg=bg, align="center",
              color=chg_color)
    rh(ws, row, 15); row += 1

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3: TAX ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
ws = tax
NCOLS = 6

for col, w in [(1, 3), (2, 30), (3, 18), (4, 18), (5, 25), (6, 3)]:
    cw(ws, col, w)

row = title_band(
    ws, 1,
    "TAX TRANSITION ANALYSIS",
    NCOLS,
    "Capital Gains Management & Tax-Efficient Liquidation Strategy  |  February 2026"
)

# ── Section A: Capital Gains Overview ────────────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2, "  SECTION A: CAPITAL GAINS OVERVIEW")
rh(ws, row, 18); row += 1

for col, label in [(2, "Item"), (3, "Value"), (4, "Notes")]:
    col_head(ws, row, col, label)
merge(ws, row, 4, row, 5)
rh(ws, row, 16); row += 1

cg_items = [
    ("Current Portfolio Value",          25000000, "$#,##0",
     "Total market value of concentrated tech position"),
    ("Estimated Cost Basis",             6500000,  "$#,##0",
     "Original acquisition cost of tech holdings"),
    ("Unrealized Capital Gains",         18500000, "$#,##0",
     "Gross gains subject to tax upon liquidation"),
    ("Federal Long-Term Cap Gains Rate", "20.0%",  None,
     "Top federal rate on long-term capital gains"),
    ("Net Investment Income Tax (NIIT)", "3.8%",   None,
     "Medicare surtax on investment income (IRC §1411)"),
    ("State Tax Rate (CA)",              "13.3%",  None,
     "Highest marginal California income tax rate"),
    ("Gross Effective Rate",             "37.1%",  None,
     "Blended federal + state rate on recognized gains"),
    ("Estimated Gross Tax Liability",    4625000,  "$#,##0",
     "Full tax if all gains recognized in a single year"),
    ("Tax-Loss Harvesting Offset",       -850000,  "$#,##0",
     "Identified losses across portfolio to offset gains"),
    ("Net Tax Liability (After Offset)", 3775000,  "$#,##0",
     "Net transition cost after harvesting strategy"),
]

for i, (label, val, fmt, note) in enumerate(cg_items):
    bg   = stripe(i)
    bold = label in ["Unrealized Capital Gains",
                     "Estimated Gross Tax Liability",
                     "Net Tax Liability (After Offset)"]
    if isinstance(val, (int, float)):
        color = RED if val > 0 and "Tax" in label and "Offset" not in label \
                else (GREEN if val < 0 else DGRAY)
        data_cell(ws, row, 2, label, bold=bold, bg=bg,
                  color=NAVY if bold else DGRAY)
        data_cell(ws, row, 3, val, bold=bold, bg=bg,
                  align="right", fmt=fmt, color=color)
    else:
        data_cell(ws, row, 2, label, bold=bold, bg=bg)
        data_cell(ws, row, 3, val, bold=bold, bg=bg, align="center")
    merge(ws, row, 4, row, 5)
    data_cell(ws, row, 4, note, bg=bg, size=9, color="666666")
    rh(ws, row, 15); row += 1

rh(ws, row, 8); row += 1

# ── Section B: Phased Liquidation Schedule ───────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2,
    "  SECTION B: PHASED LIQUIDATION SCHEDULE  —  5 Tranches Over 8 Months")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Tranche / Month"),
    (3, "Amount Liquidated"),
    (4, "Est. Tax Impact"),
    (5, "Cumulative Liquidated"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

tranches = [
    ("Tranche 1  (Month 4)", 4500000, 925000),
    ("Tranche 2  (Month 5)", 4500000, 925000),
    ("Tranche 3  (Month 6)", 4500000, 925000),
    ("Tranche 4  (Month 7)", 4500000, 925000),
    ("Tranche 5  (Month 8)", 4500000, 925000),
]
cumulative = 0
for i, (label, amt, tax_imp) in enumerate(tranches):
    bg = stripe(i)
    cumulative += amt
    data_cell(ws, row, 2, label, bold=True, bg=bg)
    data_cell(ws, row, 3, amt,       bg=bg, align="right", fmt='$#,##0')
    data_cell(ws, row, 4, tax_imp,   bg=bg, align="right", fmt='$#,##0',
              color=RED)
    data_cell(ws, row, 5, cumulative, bg=bg, align="right", fmt='$#,##0')
    rh(ws, row, 15); row += 1

total_cell(ws, row, 2, "TOTAL LIQUIDATED")
total_cell(ws, row, 3, 22500000, fmt='$#,##0')
total_cell(ws, row, 4, 4625000,  fmt='$#,##0')
total_cell(ws, row, 5, 22500000, fmt='$#,##0')
rh(ws, row, 18); row += 2

# ── Section C: Tax Optimization Strategies ───────────────────────────────────
merge(ws, row, 2, row, 5)
section_cell(ws, row, 2, "  SECTION C: TAX OPTIMIZATION STRATEGIES")
rh(ws, row, 18); row += 1

for col, label in [(2, "Strategy"), (3, "Est. Value"), (4, "Description")]:
    col_head(ws, row, col, label)
merge(ws, row, 4, row, 5)
rh(ws, row, 16); row += 1

strategies = [
    ("Tax-Loss Harvesting",
     850000,
     "Identify offsetting losses in fixed income and other equity positions. "
     "Reduces net taxable gain dollar-for-dollar."),
    ("Donor-Advised Fund (DAF)",
     500000,
     "Contribute appreciated shares directly to DAF. Avoid capital gains entirely; "
     "receive fair-market-value charitable deduction."),
    ("Qualified Opportunity Zone (QOZ)",
     1000000,
     "Invest deferred gains into QOZ fund. Defer recognition and potentially exclude "
     "future appreciation after 10-year hold."),
    ("Installment Liquidation Structure",
     None,
     "Spread recognition across 5 tax years. Avoids single-year tax cliff and keeps "
     "income below highest bracket thresholds."),
    ("Charitable Remainder Trust (CRT)",
     None,
     "Transfer appreciated stock into CRT. Avoid immediate gain, receive income stream, "
     "estate planning benefit."),
]
for i, (strat, val, desc) in enumerate(strategies):
    bg = stripe(i)
    data_cell(ws, row, 2, strat, bold=True, bg=bg, color=NAVY)
    data_cell(ws, row, 3,
              val if val else "Structural",
              bg=bg, align="right",
              fmt='$#,##0' if val else None,
              color=GREEN if val else DGRAY)
    merge(ws, row, 4, row, 5)
    data_cell(ws, row, 4, desc, bg=bg, size=9)
    rh(ws, row, 28); row += 1

rh(ws, row, 8); row += 1
merge(ws, row, 2, row, 5)
note_cell(ws, row, 2,
    "All tax figures are estimates. Actual liability depends on cost basis, "
    "holding period, filing status, and applicable deductions. "
    "Coordinate with qualified CPA and estate attorney before execution.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4: SBL CREDIT
# ══════════════════════════════════════════════════════════════════════════════
ws = sbl
NCOLS = 7

for col, w in [(1, 3), (2, 28), (3, 16), (4, 16), (5, 16), (6, 18), (7, 3)]:
    cw(ws, col, w)

row = title_band(
    ws, 1,
    "SECURITIES-BASED LENDING (SBL) CREDIT FACILITY",
    NCOLS,
    "$5M Non-Purpose Credit Facility  |  Private Foundation Funding Strategy  |  February 2026"
)

# ── Section A: Credit Facility Structure ─────────────────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2, "  SECTION A: CREDIT FACILITY STRUCTURE")
rh(ws, row, 18); row += 1

for col, label in [(2, "Parameter"), (3, "Value"), (4, "Notes")]:
    col_head(ws, row, col, label)
merge(ws, row, 4, row, 6)
rh(ws, row, 16); row += 1

# Pull key values from SBL CSV
sbl_struct = {r["Metric_Name"]: r for r in raw_sbl
              if r["Metric_Category"] == "Loan_Structure"}
interest_rate = 0.065  # 6.5% from CSV

loan_params = [
    ("Loan Purpose",
     "Non-Purpose Loan",
     "Proceeds cannot be used to purchase or carry securities"),
    ("Loan Amount",
     "$5,000,000",
     "20% of total $25M portfolio value"),
    ("Collateral Portfolio Value",
     "$15,000,000",
     "60% of diversified portfolio pledged; 40% remains unencumbered"),
    ("Loan-to-Value (LTV)",
     "33.3%",
     "Conservative LTV — well below margin call threshold"),
    ("Margin Call Trigger",
     "40.0% LTV",
     "Additional collateral required if portfolio declines to this level"),
    ("Interest Rate — SOFR",
     "4.50%",
     "Secured Overnight Financing Rate (benchmark)"),
    ("Credit Spread",
     "+200 bps",
     "Institutional pricing — reflects UHNW client tier"),
    ("All-In Interest Rate",
     "6.50%",
     "SOFR 4.50% + Spread 2.00%"),
    ("Effective After-Tax Rate",
     "4.10%",
     "6.50% × (1 − 37% tax bracket) — interest may be deductible"),
    ("Payment Structure",
     "Interest-Only",
     "No mandatory principal amortization; annual rate resets"),
    ("Facility Term",
     "12 Months (Renewable)",
     "Annually renewable at bank's discretion; no prepayment penalty"),
    ("Annual Gross Interest",
     "$325,000",
     "5,000,000 × 6.50%"),
    ("Annual After-Tax Interest",
     "$204,750",
     "Effective cost after investment interest deduction at 37%"),
    ("Use of Proceeds",
     "Private Foundation Seed Capital",
     "Fund $10M philanthropic vehicle without triggering capital gains"),
]
for i, (param, val, note) in enumerate(loan_params):
    bg   = stripe(i)
    bold = param in ["Loan Amount", "All-In Interest Rate",
                     "Annual Gross Interest", "Margin Call Trigger",
                     "Effective After-Tax Rate"]
    data_cell(ws, row, 2, param, bold=bold, bg=bg,
              color=NAVY if bold else DGRAY)
    data_cell(ws, row, 3, val, bold=bold, bg=bg, align="center")
    merge(ws, row, 4, row, 6)
    data_cell(ws, row, 4, note, bg=bg, size=9, color="666666")
    rh(ws, row, 16); row += 1

rh(ws, row, 8); row += 1

# ── Section B: Interest-Only Amortization Schedule ───────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2,
    "  SECTION B: INTEREST-ONLY PAYMENT SCHEDULE  —  12-Month Facility")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Period"),
    (3, "Beginning Balance"),
    (4, "Monthly Interest"),
    (5, "Principal Payment"),
    (6, "Ending Balance"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

principal    = 5_000_000
monthly_int  = principal * interest_rate / 12

for month in range(1, 13):
    bg   = stripe(month)
    bold = month == 12
    data_cell(ws, row, 2, f"Month {month:>2}", bold=bold, bg=bg)
    data_cell(ws, row, 3, principal,    bold=bold, bg=bg,
              align="right", fmt='$#,##0')
    data_cell(ws, row, 4, monthly_int,  bold=bold, bg=bg,
              align="right", fmt='$#,##0', color=RED)
    data_cell(ws, row, 5, 0,            bold=bold, bg=bg,
              align="center", fmt='$#,##0')
    data_cell(ws, row, 6, principal,    bold=bold, bg=bg,
              align="right", fmt='$#,##0')
    rh(ws, row, 14); row += 1

total_cell(ws, row, 2, "TOTAL ANNUAL INTEREST")
total_cell(ws, row, 3, principal,              fmt='$#,##0')
total_cell(ws, row, 4, principal * interest_rate, fmt='$#,##0')
total_cell(ws, row, 5, 0,                      fmt='$#,##0')
total_cell(ws, row, 6, principal,              fmt='$#,##0')
rh(ws, row, 18); row += 2

# ── Section C: Margin Call Stress Test ───────────────────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2, "  SECTION C: MARGIN CALL STRESS TEST")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Scenario"),
    (3, "Collateral Decline"),
    (4, "Collateral Value"),
    (5, "Resulting LTV"),
    (6, "Margin Call Triggered?"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

collateral_base = 15_000_000
scenarios = [
    ("Base Case",         0.00),
    ("Moderate Decline",  0.10),
    ("Significant Drop",  0.20),
    ("Severe Stress",     0.30),
    ("2008-Style Crisis", 0.40),
    ("Extreme Tail Risk", 0.50),
]
for i, (scenario, decline) in enumerate(scenarios):
    port_val   = collateral_base * (1 - decline)
    ltv        = principal / port_val
    triggered  = ltv > 0.40
    call_label = "YES  ⚠" if triggered else "NO  ✓"
    call_color = RED if triggered else GREEN
    bg         = stripe(i)
    data_cell(ws, row, 2, scenario, bold=True, bg=bg)
    data_cell(ws, row, 3,
              f"-{decline*100:.0f}%" if decline else "0%  (Baseline)",
              bg=bg, align="center",
              color=RED if decline > 0 else GREEN)
    data_cell(ws, row, 4, port_val,  bg=bg, align="right", fmt='$#,##0')
    data_cell(ws, row, 5, ltv,       bg=bg, align="center", fmt="0.0%",
              color=RED if triggered else DGRAY, bold=triggered)
    data_cell(ws, row, 6, call_label, bold=True, bg=bg, align="center",
              color=call_color)
    rh(ws, row, 15); row += 1

rh(ws, row, 8); row += 1
merge(ws, row, 2, row, 6)
note_cell(ws, row, 2,
    "Stress test applies to the $15M pledged collateral. The remaining $10M portfolio "
    "and $2.5M cash reserve are unpledged and available for additional collateral posting "
    "or margin call response. 2008 historical S&P 500 peak-to-trough: -57%.")
rh(ws, row, 28); row += 2

# ── Section D: SBL vs. Liquidation — Tax Arbitrage ───────────────────────────
merge(ws, row, 2, row, 6)
section_cell(ws, row, 2,
    "  SECTION D: SBL STRATEGY vs. OUTRIGHT LIQUIDATION — TAX ARBITRAGE ANALYSIS")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Comparison Factor"),
    (3, "Liquidate & Pay Gains"),
    (4, "SBL Credit Facility"),
    (5, "SBL Advantage"),
]:
    col_head(ws, row, col, label)
merge(ws, row, 5, row, 6)
rh(ws, row, 16); row += 1

arbitrage = [
    ("Immediate Tax Cost",
     "$1,669,500",
     "$0",
     "Defers $1.67M tax on $5M tranche"),
    ("Annual Carry Cost",
     "$0",
     "$204,750 (after-tax)",
     "Net interest replaces tax burden"),
    ("Capital Deployed to Foundation",
     "$3,330,500",
     "$5,000,000",
     "+$1,669,500 more for philanthropy"),
    ("Portfolio Assets Still Compounding",
     "$20,000,000",
     "$25,000,000",
     "+$5M earning 9.8% annually"),
    ("Est. Return on Preserved Capital (Yr 1)",
     "N/A",
     "~$490,000",
     "9.8% × $5M not sold"),
    ("Net Annual Benefit of SBL (Yr 1)",
     "N/A",
     "~$285,250",
     "$490K return − $204.75K net interest"),
    ("SBL Breakeven vs. Liquidation",
     "N/A",
     "3.1 Years",
     "From sbl_credit_strategy.csv analysis"),
    ("10-Year SBL Advantage",
     "N/A",
     "$7,124,500",
     "Tax saved + opportunity cost of capital"),
]
for i, (factor, liq, sbl_v, adv) in enumerate(arbitrage):
    bg = stripe(i)
    data_cell(ws, row, 2, factor, bold=True, bg=bg)
    data_cell(ws, row, 3, liq,   bg=bg, align="center",
              color=RED if "$" in liq and liq != "$0" else DGRAY)
    data_cell(ws, row, 4, sbl_v, bg=bg, align="center", color=GREEN)
    merge(ws, row, 5, row, 6)
    data_cell(ws, row, 5, adv,   bg=bg, align="left",
              bold=True, color=GREEN, size=9)
    rh(ws, row, 16); row += 1

rh(ws, row, 8); row += 1
merge(ws, row, 2, row, 6)
note_cell(ws, row, 2,
    "Liquidation tax figures based on $5M tranche: $4.5M taxable gain × 37.1% effective rate = $1,669,500 tax. "
    "SBL after-tax interest: $325,000 × (1 − 37%) = $204,750. "
    "Opportunity cost data sourced from sbl_credit_strategy.csv.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 5: GOALS PLANNING
# ══════════════════════════════════════════════════════════════════════════════
ws = gp
NCOLS = 8

for col, w in [(1, 3), (2, 20), (3, 14), (4, 18), (5, 18), (6, 18), (7, 20), (8, 3)]:
    cw(ws, col, w)

row = title_band(
    ws, 1,
    "GOALS-BASED WEALTH PLANNING",
    NCOLS,
    "$10M Private Foundation  |  20-Year Portfolio Projection  |  Bear / Base / Bull Scenarios  |  February 2026"
)

# ── Section A: Planning Assumptions ──────────────────────────────────────────
merge(ws, row, 2, row, 7)
section_cell(ws, row, 2, "  SECTION A: PLANNING ASSUMPTIONS")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Parameter"), (3, "Bear Case"),
    (4, "Base Case"),  (5, "Bull Case"), (6, "Notes"),
]:
    col_head(ws, row, col, label)
merge(ws, row, 6, row, 7)
rh(ws, row, 16); row += 1

assumptions = [
    ("Starting Portfolio Value",
     "$20,375,000", "$20,375,000", "$20,375,000",
     "Net of $4.625M estimated tax on full transition"),
    ("Expected Annual Return",
     "5.0%", "9.8%", "13.5%",
     "Conservative / Institutional Base / Optimistic scenario"),
    ("Annual Withdrawal Rate",
     "2.0%", "2.0%", "2.0%",
     "Sustainable distribution rate for lifestyle & philanthropy"),
    ("Investment Horizon",
     "20 Years", "20 Years", "20 Years",
     "Long-term compounding window"),
    ("Private Foundation Target",
     "$10,000,000", "$10,000,000", "$10,000,000",
     "Philanthropic endowment goal"),
    ("Foundation Funding Method",
     "SBL Facility", "SBL Facility", "SBL Facility",
     "$5M drawn from credit line — no liquidation, no additional tax"),
    ("Annual SBL Interest Cost",
     "$204,750", "$204,750", "$204,750",
     "After-tax interest (6.50% rate × $5M × (1−37%))"),
    ("Net Annual Portfolio Income",
     "$420,250", "$625,000", "$900,000",
     "Income generation after SBL interest carry cost"),
]
for i, (param, bear, base, bull, note) in enumerate(assumptions):
    bg = stripe(i)
    data_cell(ws, row, 2, param, bold=True, bg=bg)
    data_cell(ws, row, 3, bear, bg=bg, align="center", color=RED)
    data_cell(ws, row, 4, base, bg=bg, align="center", color=NAVY, bold=True)
    data_cell(ws, row, 5, bull, bg=bg, align="center", color=GREEN)
    merge(ws, row, 6, row, 7)
    data_cell(ws, row, 6, note, bg=bg, size=9, color="666666")
    rh(ws, row, 16); row += 1

rh(ws, row, 8); row += 1

# ── Section B: 20-Year Projection ────────────────────────────────────────────
merge(ws, row, 2, row, 7)
section_cell(ws, row, 2,
    "  SECTION B: 20-YEAR PORTFOLIO PROJECTION  —  Net of 2% Annual Withdrawal")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Year"),
    (3, "Calendar Year"),
    (4, "Bear Case\n(Net 3.0%)"),
    (5, "Base Case\n(Net 7.8%)"),
    (6, "Bull Case\n(Net 11.5%)"),
    (7, "Milestone"),
]:
    col_head(ws, row, col, label)
rh(ws, row, 28); row += 1

start_val    = 20_375_000
bear_net     = 0.030   # 5.0%  − 2.0% withdrawal
base_net     = 0.078   # 9.8%  − 2.0%
bull_net     = 0.115   # 13.5% − 2.0%

bear_v = start_val
base_v = start_val
bull_v = start_val

for yr in range(1, 21):
    bear_v *= (1 + bear_net)
    base_v *= (1 + base_net)
    bull_v *= (1 + bull_net)

    cal_yr  = 2026 + yr
    bg      = stripe(yr)
    bold    = yr in [5, 10, 15, 20]

    milestone = ""
    if yr == 1:
        milestone = "SBL Facility Established"
    elif yr == 5:
        milestone = "5-Year Review"
    elif yr == 10:
        milestone = "Foundation Self-Sustaining"
    elif yr == 15:
        milestone = "15-Year Review"
    elif yr == 20:
        milestone = "▲ Planning Horizon"

    ms_color = PURPLE if milestone else "888888"

    data_cell(ws, row, 2, f"Year {yr:>2}", bold=bold, bg=bg)
    data_cell(ws, row, 3, cal_yr, bold=bold, bg=bg, align="center")
    data_cell(ws, row, 4, bear_v, bold=bold, bg=bg,
              align="right", fmt='$#,##0',
              color=RED if bold else DGRAY)
    data_cell(ws, row, 5, base_v, bold=bold, bg=bg,
              align="right", fmt='$#,##0',
              color=NAVY if bold else DGRAY)
    data_cell(ws, row, 6, bull_v, bold=bold, bg=bg,
              align="right", fmt='$#,##0',
              color=GREEN if bold else DGRAY)
    data_cell(ws, row, 7, milestone, bold=bold, bg=bg,
              size=9, color=ms_color)
    rh(ws, row, 14); row += 1

# Final summary row
total_cell(ws, row, 2, "20-YEAR ENDING VALUE")
total_cell(ws, row, 3, 2046, fmt="0")
total_cell(ws, row, 4, bear_v, fmt='$#,##0')
total_cell(ws, row, 5, base_v, fmt='$#,##0')
total_cell(ws, row, 6, bull_v, fmt='$#,##0')
total_cell(ws, row, 7, "End of Planning Horizon")
rh(ws, row, 20); row += 2

# ── Section C: Foundation Funding Analysis ────────────────────────────────────
merge(ws, row, 2, row, 7)
section_cell(ws, row, 2,
    "  SECTION C: PRIVATE FOUNDATION FUNDING ANALYSIS")
rh(ws, row, 18); row += 1

for col, label in [
    (2, "Milestone"), (3, "Year"), (4, "Foundation Value"),
    (5, "Cumulative Grants"), (6, "Endowment Status"), (7, ""),
]:
    col_head(ws, row, col, label)
rh(ws, row, 16); row += 1

found_items = [
    ("SBL Proceeds Deployed",          "Year 1",  5_000_000,  0,
     "Foundation Seeded", "100% via credit facility — zero liquidation"),
    ("Foundation — Year 5",            "Year 5",  7_200_000,  1_750_000,
     "Growing",           "7.5% return net of 5% annual grantmaking"),
    ("Foundation — Year 10",           "Year 10", 10_300_000, 3_500_000,
     "Target Achieved",   "$10M endowment target reached"),
    ("SBL Loan Fully Repaid",          "Year 10", 10_300_000, 3_500_000,
     "Debt-Free",         "Loan retired from portfolio income — no asset sales"),
    ("Foundation — Year 20 (Proj.)",   "Year 20", 24_000_000, 12_000_000,
     "Generational Impact","Compound growth + grantmaking at scale"),
]
for i, (milestone, yr, fval, grants, status, note) in enumerate(found_items):
    bg    = stripe(i)
    bold  = status in ["Target Achieved", "Debt-Free"]
    sc    = GREEN if "Achieved" in status or "Debt" in status else NAVY
    data_cell(ws, row, 2, milestone, bold=bold, bg=bg, color=sc)
    data_cell(ws, row, 3, yr,        bg=bg, align="center")
    data_cell(ws, row, 4, fval,   bg=bg, align="right",
              fmt='$#,##0', bold=bold, color=GREEN if bold else DGRAY)
    data_cell(ws, row, 5, grants, bg=bg, align="right", fmt='$#,##0')
    data_cell(ws, row, 6, status, bold=bold, bg=bg, align="center",
              color=sc)
    data_cell(ws, row, 7, note,   bg=bg, size=9, color="666666")
    rh(ws, row, 22); row += 1

rh(ws, row, 8); row += 1
merge(ws, row, 2, row, 7)
note_cell(ws, row, 2,
    "Projections are illustrative and not a guarantee of returns. "
    "Base case uses institutional long-term capital market assumptions (9.8% expected return). "
    "Foundation values assume 7.5% endowment return net of 5% annual grantmaking distribution. "
    "Consult a financial advisor before making investment or philanthropic decisions.")
rh(ws, row, 28)

# ── SAVE ──────────────────────────────────────────────────────────────────────
wb.save(OUTPUT_FILE)
print(f"Workbook saved: {OUTPUT_FILE}")
print(f"Tabs: {', '.join(wb.sheetnames)}")
