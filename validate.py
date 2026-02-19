#!/usr/bin/env python3
"""
validate.py — Cross-file consistency checker for UHNW Portfolio case study.

Hierarchy:  CSV source data  →  Excel workbook  →  PowerPoint presentation

Checks:
  1. Workbook Inputs tab cells match expected constant values
  2. All derived values are mathematically correct given those inputs
  3. Every hardcoded value in build_workbook.py matches the CSV / derived truth
  4. Every hardcoded value in build_presentation.py matches the CSV / derived truth

Run directly:       python3 validate.py
Run via build_all:  python3 build_all.py  (recommended)
"""

import csv
import os
import re
import sys
import math

from openpyxl import load_workbook

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DIR  = os.path.join(BASE_DIR, "csv")
WB_FILE  = os.path.join(BASE_DIR, "UHNW_Portfolio_Analysis.xlsx")
WB_SRC   = os.path.join(BASE_DIR, "build_workbook.py")
PPT_SRC  = os.path.join(BASE_DIR, "build_presentation.py")

ERRORS   = []
PASSES   = []


# ── helpers ──────────────────────────────────────────────────────────────────

def ok(name, value=""):
    PASSES.append(f"  ✓  {name}  [{value}]")


def fail(name, expected, actual):
    ERRORS.append(
        f"  ✗  {name}\n"
        f"       expected : {expected}\n"
        f"       actual   : {actual}"
    )


def near(a, b, tol=0.0005):
    """True when two numbers agree within a relative + absolute tolerance."""
    try:
        a, b = float(a), float(b)
        return abs(a - b) <= max(tol * max(abs(a), abs(b)), 1e-9)
    except Exception:
        return False


def load_csv_file(filename):
    path = os.path.join(CSV_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def src(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def src_has(text, pattern, label):
    """Confirm a regex pattern appears in source text."""
    if re.search(pattern, text):
        ok(label, f"found: {re.search(pattern, text).group(0)[:60]}")
    else:
        fail(label, f"regex: {pattern}", "NOT FOUND in source file")


def src_not_has(text, pattern, label):
    """Confirm a banned pattern does NOT appear in source text."""
    m = re.search(pattern, text)
    if not m:
        ok(label, "absent ✓")
    else:
        fail(label, "should NOT appear", f"found: '{m.group(0)}' — fix this")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 0 — KEY INPUTS (constants — edit here if assumptions change)
# ══════════════════════════════════════════════════════════════════════════════
PORTFOLIO    = 25_000_000
COST_BASIS   =  6_500_000
TECH_CONC    =      0.90
CASH_CONC    =      0.10
FED_RATE     =      0.200
NIIT_RATE    =      0.038
STATE_RATE   =      0.133
TAX_BRACKET  =      0.370
HARVESTING   =    850_000
N_TRANCHES   =          5
TRANCHE_AMT  =  4_500_000
LOAN_AMT     =  5_000_000
COLLATERAL   = 15_000_000
SOFR         =      0.045
SPREAD       =      0.020
LTV_TRIGGER  =      0.40
BEAR_R       =      0.050
BASE_R       =      0.098
BULL_R       =      0.135
WITHDRAWAL   =      0.020
HORIZON      =         20
FOUND_TARGET = 10_000_000
FOUND_RETURN =      0.075
FOUND_PAYOUT =      0.050

# ── derived values (single source of truth for all math) ─────────────────────
UNREALIZED    = PORTFOLIO - COST_BASIS
EFF_RATE      = FED_RATE + NIIT_RATE + STATE_RATE
GROSS_TAX     = UNREALIZED * EFF_RATE
NET_TAX       = GROSS_TAX - HARVESTING
ALLIN_RATE    = SOFR + SPREAD
AFTERTAX_RATE = ALLIN_RATE * (1 - TAX_BRACKET)
GROSS_INT     = LOAN_AMT * ALLIN_RATE
NET_INT       = LOAN_AMT * ALLIN_RATE * (1 - TAX_BRACKET)
START_VAL     = PORTFOLIO - NET_TAX            # post-tax projection start (net of harvesting offset)
BEAR_NET      = BEAR_R - WITHDRAWAL
BASE_NET      = BASE_R - WITHDRAWAL
BULL_NET      = BULL_R - WITHDRAWAL
SBL_BLOCK_BASIS = 500_000                      # cost basis of the specific $5M block (from CSV)
LIQ_TAX_5M   = (LOAN_AMT - SBL_BLOCK_BASIS) * EFF_RATE   # tax on $4.5M taxable gain
CAP_TO_FOUND  = LOAN_AMT - LIQ_TAX_5M         # capital reaching foundation after liq. tax
FOUND_NET_R   = FOUND_RETURN - FOUND_PAYOUT
FOUND_CONTRIB =     70_760   # annual client contribution from portfolio income
FOUND_Y10     = (LOAN_AMT * (1 + FOUND_NET_R) ** 10
                 + FOUND_CONTRIB * ((1 + FOUND_NET_R) ** 10 - 1) / FOUND_NET_R)
FOUND_Y20     = (LOAN_AMT * (1 + FOUND_NET_R) ** 20
                 + FOUND_CONTRIB * ((1 + FOUND_NET_R) ** 20 - 1) / FOUND_NET_R)
TECH_VALUE    = PORTFOLIO * TECH_CONC
CASH_VALUE    = PORTFOLIO * CASH_CONC
TRANCHE_TOTAL = N_TRANCHES * TRANCHE_AMT
LTV_BASE      = LOAN_AMT / COLLATERAL

# optimized allocation values
PUB_EQ_PCT  = 0.55;  PUB_EQ_VAL  = PORTFOLIO * PUB_EQ_PCT
FI_PCT      = 0.23;  FI_VAL      = PORTFOLIO * FI_PCT
PE_PCT      = 0.12;  PE_VAL      = PORTFOLIO * PE_PCT
RE_PCT      = 0.08;  RE_VAL      = PORTFOLIO * RE_PCT
CASH_OPT_PCT= 0.02;  CASH_OPT_VAL= PORTFOLIO * CASH_OPT_PCT
LRGCAP_PCT  = 0.25;  LRGCAP_VAL  = PORTFOLIO * LRGCAP_PCT
INTL_PCT    = 0.17;  INTL_VAL    = PORTFOLIO * INTL_PCT
MIDSMALL_PCT= 0.13;  MIDSMALL_VAL= PORTFOLIO * MIDSMALL_PCT


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — DERIVED MATH SELF-CHECK
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 1. DERIVED MATH SELF-CHECK ══")

math_checks = [
    ("Unrealized gains",              18_500_000,  UNREALIZED),
    ("Effective cap gains rate",            0.371,  EFF_RATE),
    ("Gross tax liability",            6_863_500,  GROSS_TAX),
    ("Net tax after offset",           6_013_500,  NET_TAX),
    ("SBL all-in rate",                    0.065,  ALLIN_RATE),
    ("SBL after-tax rate",               0.04095,  AFTERTAX_RATE),
    ("SBL gross annual interest",        325_000,  GROSS_INT),
    ("SBL net annual interest",          204_750,  NET_INT),
    ("Post-tax start value (projections)",18_986_500, START_VAL),
    ("Bear net return",                    0.030,  BEAR_NET),
    ("Base net return",                    0.078,  BASE_NET),
    ("Bull net return",                    0.115,  BULL_NET),
    ("Liq tax cost on $5M",            1_669_500,  LIQ_TAX_5M),
    ("Capital to foundation (liq)",    3_330_500,  CAP_TO_FOUND),
    ("Foundation net return",              0.025,  FOUND_NET_R),
    ("Foundation Year-10 value (w/ contrib)", 7_193_173,  FOUND_Y10),
    ("Foundation Year-20 value (w/ contrib)", 10_000_094, FOUND_Y20),
    ("Tech equity value",             22_500_000,  TECH_VALUE),
    ("Cash value (current)",           2_500_000,  CASH_VALUE),
    ("Tranche total (5 × $4.5M)",     22_500_000,  TRANCHE_TOTAL),
    ("LTV baseline",                       0.333,  LTV_BASE),
    ("Optimized allocation sums to 100%", 1.00,
        PUB_EQ_PCT + FI_PCT + PE_PCT + RE_PCT + CASH_OPT_PCT),
    ("Public equity sub-alloc sums to 55%", PUB_EQ_PCT,
        LRGCAP_PCT + INTL_PCT + MIDSMALL_PCT),
    ("Tranche total = tech equity",   TECH_VALUE,  TRANCHE_TOTAL),
    ("LTV stress -20%",                   0.4167,  LOAN_AMT / (COLLATERAL * 0.80)),
    ("LTV stress -10%",                   0.3704,  LOAN_AMT / (COLLATERAL * 0.90)),
    ("VaR improvement %",                  55.88,
        (4_250_000 - 1_875_000) / 4_250_000 * 100),
    ("Beta improvement %",                 34.81,
        (1.35 - 0.88) / 1.35 * 100),
    ("Sharpe improvement %",               78.95,
        (0.68 - 0.38) / 0.38 * 100),
    ("Income improvement %",              455.56,
        (625_000 - 112_500) / 112_500 * 100),
    ("Beta increase vs optimized %",       53.41,
        (1.35 - 0.88) / 0.88 * 100),
    ("Income 82% less (current vs opt)",   82.00,
        (625_000 - 112_500) / 625_000 * 100),
    ("Geographic exposure +300%",         300.00,
        (4 - 1) / 1 * 100),
    ("Holdings +1712.5%",                1712.5,
        (145 - 8) / 8 * 100),
    ("Concentration improvement %",        84.21,
        (95 - 15) / 95 * 100),
    ("Drawdown improvement %",             51.11,
        (45 - 22) / 45 * 100),
    ("Correlation improvement %",          27.66,
        (0.94 - 0.68) / 0.94 * 100),
]

for name, expected, actual in math_checks:
    if near(expected, actual, tol=0.005):
        ok(name, f"{actual:,.4g}")
    else:
        fail(name, expected, actual)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — CSV SOURCE DATA CHECK
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 2. CSV SOURCE DATA ══")

metrics_raw = load_csv_file("transition_metrics_comparison.csv")
met = {r["Metric_Name"]: r for r in metrics_raw}

sbl_raw  = load_csv_file("sbl_credit_strategy.csv")
sbl_dict = {}
for r in sbl_raw:
    sbl_dict[r["Metric_Name"]] = r

csv_checks = [
    ("CSV Beta current",        1.35,      met["Portfolio Beta"]["Current_Concentrated"]),
    ("CSV Beta optimized",      0.88,      met["Portfolio Beta"]["JPM_Diversified"]),
    ("CSV VaR current",    4_250_000,      met["Value at Risk 95%"]["Current_Concentrated"]),
    ("CSV VaR optimized",  1_875_000,      met["Value at Risk 95%"]["JPM_Diversified"]),
    ("CSV MaxDD current",      45.0,       met["Maximum Drawdown Estimate"]["Current_Concentrated"]),
    ("CSV MaxDD optimized",    22.0,       met["Maximum Drawdown Estimate"]["JPM_Diversified"]),
    ("CSV Sharpe current",      0.38,      met["Risk-Adjusted Return"]["Current_Concentrated"]),
    ("CSV Sharpe optimized",    0.68,      met["Risk-Adjusted Return"]["JPM_Diversified"]),
    ("CSV income current",   112_500,      met["Annual Income Projection"]["Current_Concentrated"]),
    ("CSV income optimized", 625_000,      met["Annual Income Projection"]["JPM_Diversified"]),
    ("CSV corr current",       0.94,       met["Correlation to S&P 500"]["Current_Concentrated"]),
    ("CSV corr optimized",     0.68,       met["Correlation to S&P 500"]["JPM_Diversified"]),
    ("CSV holdings current",      8,       met["Number of Holdings"]["Current_Concentrated"]),
    ("CSV holdings optimized",  145,       met["Number of Holdings"]["JPM_Diversified"]),
    ("CSV asset classes curr",    2,       met["Asset Class Count"]["Current_Concentrated"]),
    ("CSV asset classes opt",     7,       met["Asset Class Count"]["JPM_Diversified"]),
    ("CSV SBL all-in rate",     6.50,       sbl_dict["Interest_Rate_SOFR_Plus_Spread"]["Value"]),
    ("CSV SBL net interest",  204_750,     sbl_dict["Net_After_Tax_Interest_Cost"]["Value"]),
    ("CSV SBL after-tax rate",  4.10,      sbl_dict["Effective_Interest_Rate_After_Tax"]["Value"]),
    ("CSV SBL 10yr advantage",7_124_500,   sbl_dict["SBL_Advantage_10_Year"]["Value"]),
    ("CSV SBL 10-yr advantage", 7_124_500, sbl_dict["SBL_Advantage_10_Year"]["Value"]),
]

for name, expected, actual in csv_checks:
    if near(expected, actual, tol=0.005):
        ok(name, actual)
    else:
        fail(name, expected, actual)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — WORKBOOK INPUT CELLS
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 3. WORKBOOK INPUTS TAB CELLS ══")

wb  = load_workbook(WB_FILE)
inp = wb["Inputs"]

cell_checks = [
    ("C6  Portfolio Value",         PORTFOLIO,    inp["C6"].value),
    ("C7  Cost Basis",              COST_BASIS,   inp["C7"].value),
    ("C8  Tech Concentration",      TECH_CONC,    inp["C8"].value),
    ("C9  Cash Allocation",         CASH_CONC,    inp["C9"].value),
    ("C12 Fed LTCG Rate",           FED_RATE,     inp["C12"].value),
    ("C13 NIIT Rate",               NIIT_RATE,    inp["C13"].value),
    ("C14 State Rate (CA)",         STATE_RATE,   inp["C14"].value),
    ("C15 Marginal Tax Bracket",    TAX_BRACKET,  inp["C15"].value),
    ("C16 Harvesting Offset",       HARVESTING,   inp["C16"].value),
    ("C19 Number of Tranches",      N_TRANCHES,   inp["C19"].value),
    ("C20 Tranche Amount",          TRANCHE_AMT,  inp["C20"].value),
    ("C23 Loan Amount",             LOAN_AMT,     inp["C23"].value),
    ("C24 Collateral Value",        COLLATERAL,   inp["C24"].value),
    ("C25 SOFR Rate",               SOFR,         inp["C25"].value),
    ("C26 Credit Spread",           SPREAD,       inp["C26"].value),
    ("C27 LTV Trigger",             LTV_TRIGGER,  inp["C27"].value),
    ("C30 Bear Gross Return",       BEAR_R,       inp["C30"].value),
    ("C31 Base Gross Return",       BASE_R,       inp["C31"].value),
    ("C32 Bull Gross Return",       BULL_R,       inp["C32"].value),
    ("C33 Withdrawal Rate",         WITHDRAWAL,   inp["C33"].value),
    ("C34 Horizon (Years)",         HORIZON,      inp["C34"].value),
    ("C35 Foundation Target",       FOUND_TARGET, inp["C35"].value),
    ("C36 Foundation Return",       FOUND_RETURN, inp["C36"].value),
    ("C37 Foundation Payout",       FOUND_PAYOUT, inp["C37"].value),
]

for name, expected, actual in cell_checks:
    if near(expected, actual if actual is not None else 0, tol=0.0001):
        ok(name, actual)
    else:
        fail(name, expected, actual)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — WORKBOOK SOURCE: HARDCODED VALUES
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 4. WORKBOOK SOURCE — HARDCODED VALUES ══")

wb_text = src(WB_SRC)

# Overview "Key Outcomes" table — must match CSV metrics
wb_hardcoded = [
    (r'"1\.35"',                  "WB Overview: beta current 1.35"),
    (r'"0\.88"',                  "WB Overview: beta optimized 0.88"),
    (r'"\$4,250,000"',            "WB Overview: VaR current $4,250,000"),
    (r'"\$1,875,000"',            "WB Overview: VaR optimized $1,875,000"),
    (r'"45\.0%"',                 "WB Overview: max drawdown current 45.0%"),
    (r'"22\.0%"',                 "WB Overview: max drawdown optimized 22.0%"),
    (r'"0\.38"',                  "WB Overview: Sharpe current 0.38"),
    (r'"0\.68"',                  "WB Overview: Sharpe optimized 0.68"),
    (r'"\$112,500"',              "WB Overview: income current $112,500"),
    (r'"\$625,000"',              "WB Overview: income optimized $625,000"),
    (r'"0\.94"',                  "WB Overview: correlation current 0.94"),
    (r'"8"',                      "WB Overview: holdings current 8"),
    (r'"145"',                    "WB Overview: holdings optimized 145"),
    (r'"\↑ 455%"',                "WB Overview: income improvement ↑ 455%"),
    (r'"\↓ 55\.9%"',              "WB Overview: VaR improvement ↓ 55.9%"),
    (r'"\↓ 34\.8%"',              "WB Overview: beta improvement ↓ 34.8%"),
    (r'"\↑ 78\.9%"',              "WB Overview: Sharpe improvement ↑ 78.9%"),
    (r'"\↓ 84\.2%"',              "WB Overview: concentration ↓ 84.2%"),
    (r'"\↓ 51\.1%"',              "WB Overview: drawdown ↓ 51.1%"),
    (r'"\↓ 27\.7%"',              "WB Overview: correlation ↓ 27.7%"),
    # SBL key values
    (r'5_000_000',                "WB Inputs: loan amount 5,000,000"),
    (r'15_000_000',               "WB Inputs: collateral 15,000,000"),
    (r'4_500_000',                "WB Inputs: tranche amount 4,500,000"),
    (r'850_000',                  "WB Inputs: harvesting offset 850,000"),
    # Phase timeline
    (r'Months 1-3',               "WB Overview: Phase 1 Months 1-3"),
    (r'Months 4-11',              "WB Overview: Phase 2 Months 4-11"),
    (r'Months 12-18',             "WB Overview: Phase 3 Months 12-18"),
    # Tranche schedule — months generated dynamically via loop; check loop bounds
    (r'month_num\s*=\s*4\s*\+\s*i',  "WB Tax: tranche loop starts at Month 4"),
    (r'range\(5\)',                   "WB Tax: 5 tranches in loop"),
    # Column references fixed
    (r'Inputs C23',               "WB SBL: column C reference (not D)"),
    (r'Inputs C24',               "WB SBL: column C reference (not D)"),
    # No stale "5 tax years" language
]

for pattern, label in wb_hardcoded:
    src_has(wb_text, pattern, label)

# Banned patterns — should not exist in workbook source
wb_banned = [
    (r'Inputs D2[3-7]',       "WB SBL: stale column D reference (should be C)"),
    (r'5 tax years',          "WB Tax: 'five tax years' — factually wrong for Months 4-8"),
]
for pattern, label in wb_banned:
    src_not_has(wb_text, pattern, label)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — PRESENTATION SOURCE: HARDCODED VALUES
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 5. PRESENTATION SOURCE — HARDCODED VALUES ══")

ppt_text = src(PPT_SRC)

ppt_hardcoded = [
    # Tax facts (Slide 7)
    (r'\$18,500,000',              "PPT Slide 7: unrealized gains $18,500,000"),
    (r'37\.1%',                    "PPT Slide 7: effective rate 37.1%"),
    (r'\$6,863,500',               "PPT Slide 7: gross tax $6,863,500"),
    (r'\(\$850,000\)',             "PPT Slide 7: harvesting offset ($850,000)"),
    (r'\$6,013,500',               "PPT Slide 7: net tax $6,013,500"),
    # SBL Core Insight (Slide 8)
    (r'\$1,669,500',               "PPT Slide 8: liq tax cost $1,669,500"),
    (r'\$3,330,500',               "PPT Slide 8: capital to foundation $3,330,500"),
    (r'\$204,750',                 "PPT Slide 8: after-tax SBL interest $204,750"),
    (r'\$325,000',                 "PPT Slide 8: gross SBL interest $325,000"),
    (r'4\.10%',                    "PPT Slide 8: after-tax SBL rate 4.10%"),
    (r'6\.50%',                    "PPT Slide 8: all-in SBL rate 6.50%"),
    (r'\$2,047,500',               "PPT Slide 8: 10-yr interest cost $2,047,500"),
    (r'\$7,124,500',               "PPT Slide 8: 10-yr advantage $7,124,500"),
    # Stress test LTVs (Slide 8)
    (r'33\.3%',                    "PPT Slide 8: base LTV 33.3%"),
    (r'37\.0%',                    "PPT Slide 8: -10% stress LTV 37.0%"),
    (r'41\.7%',                    "PPT Slide 8: -20% stress LTV 41.7%"),
    (r'47\.6%',                    "PPT Slide 8: -30% stress LTV 47.6%"),
    # Metrics (Slides 3, 4)
    (r'\$4\.25M',                  "PPT Slide 4: VaR current $4.25M"),
    (r'\$1\.875M',                 "PPT Slide 4: VaR optimized $1.875M"),
    (r'↓ 55\.9%',                  "PPT Slide 4: VaR improvement 55.9%"),
    (r'↓ 34\.8%',                  "PPT Slide 4: beta improvement 34.8%"),
    (r'↑ 78\.9%',                  "PPT Slide 4: Sharpe improvement 78.9%"),
    (r'↑ 455%',                    "PPT Slide 4: income improvement 455%"),
    (r'↓ 84\.2%',                  "PPT Slide 4: concentration 84.2%"),
    (r'↓ 51\.1%',                  "PPT Slide 4: drawdown 51.1%"),
    (r'↓ 27\.7%',                  "PPT Slide 4: correlation 27.7%"),
    # Projection parameters (Slide 9)
    (r'start\s*=\s*18_986_500',    "PPT Slide 9: projection start $18,986,500"),
    (r'bear_r.*=.*0\.030',         "PPT Slide 9: bear net rate 3.0%"),
    (r'base_r.*=.*0\.078',         "PPT Slide 9: base net rate 7.8%"),
    (r'bull_r.*=.*0\.115',         "PPT Slide 9: bull net rate 11.5%"),
    # Foundation callout (Slide 9)
    (r'\$7\.2M',                   "PPT Slide 9: foundation Year-10 $7.2M"),
    (r'\$10\.0M',                  "PPT Slide 9: foundation Year-20 $10.0M"),
    (r'2\.5% net',                 "PPT Slide 9: foundation net return 2.5%"),
    (r'70,760',                    "PPT Slide 9: annual contribution $70,760"),
    # Asset allocation (Slide 6)
    (r'\$22,500,000',              "PPT Slide 6: tech equity $22,500,000"),
    (r'\$2,500,000',               "PPT Slide 6: cash current $2,500,000"),
    (r'\$13,750,000',              "PPT Slide 6: public equity total $13,750,000"),
    (r'\$6,250,000',               "PPT Slide 6: US large cap $6,250,000"),
    (r'\$4,250,000',               "PPT Slide 6: int'l/EM $4,250,000"),
    (r'\$3,250,000',               "PPT Slide 6: US mid/small cap $3,250,000"),
    (r'\$5,750,000',               "PPT Slide 6: fixed income $5,750,000"),
    (r'\$3,000,000',               "PPT Slide 6: private equity $3,000,000"),
    (r'\$2,000,000',               "PPT Slide 6: real estate $2,000,000"),
    (r'(?<!\d)\$500,000',          "PPT Slide 6: cash optimized $500,000"),
    # Phase timeline consistency (Slide 10)
    (r'Months 1-3',                "PPT Slide 10: Discovery Months 1-3"),
    (r'Months 4-11',               "PPT Slide 10: Execution Months 4-11"),
    (r'Months 12-18',              "PPT Slide 10: Monitoring Months 12-18"),
    # Key insight claims (Slide 4)
    (r'53%',                       "PPT Slide 4: 53% more market risk"),
    (r'82%',                       "PPT Slide 4: 82% less income"),
]

for pattern, label in ppt_hardcoded:
    src_has(ppt_text, pattern, label)

# Banned patterns — should not exist in presentation source
ppt_banned = [
    (r'"\$1\.88M"',            "PPT: stale VaR $1.88M — should be $1.875M"),
    (r'5 tax years',           "PPT: 'five tax years' — factually wrong for Months 4-8"),
    (r'"Fund the \$10M',       "PPT Slide 8: slide header should say 'Seed' not 'Fund'"),
    (r'credit facility to fund the \$10M foundation',
                               "PPT Agenda: should say 'seed' not 'fund'"),
]

for pattern, label in ppt_banned:
    src_not_has(ppt_text, pattern, label)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — CROSS-FILE CONSISTENCY: KEY VALUES IN BOTH FILES
# ══════════════════════════════════════════════════════════════════════════════
print("\n══ 6. CROSS-FILE CONSISTENCY ══")

cross_checks = [
    # Phase timeline
    ("Phase 1 months match",
     bool(re.search(r'Months 1-3', wb_text)),
     bool(re.search(r'Months 1-3', ppt_text))),
    ("Phase 2 months match",
     bool(re.search(r'Months 4-11', wb_text)),
     bool(re.search(r'Months 4-11', ppt_text))),
    ("Phase 3 months match",
     bool(re.search(r'Months 12-18', wb_text)),
     bool(re.search(r'Months 12-18', ppt_text))),
    # Tranche schedule — workbook uses a loop; presentation uses Mo.4…Mo.8 labels
    ("Tranche loop starts Month 4 (WB) + Mo.4 label present (PPT)",
     bool(re.search(r'month_num\s*=\s*4\s*\+\s*i', wb_text)),
     bool(re.search(r'Mo\.4', ppt_text))),
    # 10yr SBL advantage
    ("10yr SBL advantage $7,124,500 in both",
     bool(re.search(r'7,124,500', wb_text)),
     bool(re.search(r'7,124,500', ppt_text))),
    # Foundation Year 20
    ("Foundation $10.0M at Year 20 in both",
     bool(re.search(r'\$10\.0M', wb_text)),
     bool(re.search(r'\$10\.0M', ppt_text))),
]

for label, wb_val, ppt_val in cross_checks:
    if wb_val and ppt_val:
        ok(label, "both files ✓")
    elif not wb_val:
        fail(label, "should appear in workbook source", "NOT FOUND in build_workbook.py")
    else:
        fail(label, "should appear in presentation source", "NOT FOUND in build_presentation.py")


# ══════════════════════════════════════════════════════════════════════════════
# REPORT
# ══════════════════════════════════════════════════════════════════════════════
print(f"\n{'═'*62}")
print(f"  PASSES   : {len(PASSES)}")
print(f"  ERRORS   : {len(ERRORS)}")
print(f"{'═'*62}")

if ERRORS:
    print(f"\n{'─'*62}")
    print(f"  FAILED CHECKS ({len(ERRORS)})")
    print(f"{'─'*62}")
    for e in ERRORS:
        print(e)
    print(f"\n{'═'*62}")
    print("  BUILD FAILED — resolve all errors before delivery.")
    print(f"{'═'*62}\n")
    sys.exit(1)
else:
    print(f"\n  ALL {len(PASSES)} CHECKS PASSED.")
    print(f"  Files are consistent and mathematically verified.")
    print(f"{'═'*62}\n")
    sys.exit(0)
