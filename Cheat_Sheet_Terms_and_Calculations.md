# Personal Reference: Terms, Formulas, and Calculations
## UHNW Portfolio Transition Case Study

---

## CORE PORTFOLIO INPUTS

| Input | Value |
|---|---|
| Portfolio Value | $25,000,000 |
| Cost Basis | $6,500,000 |
| Unrealized Gains | $18,500,000 |
| Tech Equity Concentration | 90% ($22,500,000) |
| Cash | 10% ($2,500,000) |
| Tech Cost Basis | $4,000,000 (cost basis minus $2.5M cash) |
| Tech Gain | $18,500,000 ($22.5M value - $4M basis) |
| Gain Ratio on Tech | 82.22% ($18.5M / $22.5M) |

---

## SECTION 1: TAX CALCULATIONS

### Terms

**Unrealized Capital Gain:** The profit embedded in a position that has not yet been sold. Taxable only upon sale. Calculated as: Current Market Value - Cost Basis.

**Cost Basis:** The original purchase price of an asset, used to determine the taxable gain upon sale. Here, $6,500,000 against a $25,000,000 portfolio.

**Long-Term Capital Gains (LTCG):** Gains on assets held more than one year. Taxed at preferential federal rates (0%, 15%, or 20% depending on income). This client is in the 20% bracket.

**Net Investment Income Tax (NIIT):** A 3.8% federal surtax on investment income (capital gains, dividends, interest) for high earners. Applies to lesser of net investment income or the amount by which MAGI exceeds threshold ($200K single / $250K married). Applies to this client.

**California State Tax on Capital Gains:** California taxes capital gains as ordinary income. No preferential rate. At this income level, the rate is 13.3%.

**Blended Effective Tax Rate:** The combined rate from all three tax components applied to capital gains.

### Blended Rate Calculation
```
Federal LTCG:    20.0%
NIIT:             3.8%
CA State:        13.3%
               -------
Blended Rate:    37.1%
```

### Gross Tax Liability
```
Formula: Unrealized Gains x Blended Rate
$18,500,000 x 0.371 = $6,863,500
```

### Tax-Loss Harvesting Offset
A strategy where you sell positions at a loss to offset realized gains, reducing your taxable gain dollar-for-dollar.
```
Gross Tax Liability:       $6,863,500
TLH Offset:               ($850,000)
Net Tax Liability:          $6,013,500
```

### Post-Tax Portfolio Value
```
$25,000,000 - $6,013,500 = $18,986,500
```

### Per-Tranche Tax (Correct Method)
Each $4.5M tranche liquidates proportional tech stock. Only the gain portion is taxable.
```
Gain ratio on tech:         82.22% ($18.5M / $22.5M)
Gain in each $4.5M tranche: $4,500,000 x 0.8222 = $3,699,900
Tax per tranche:            $3,699,900 x 0.371 = $1,372,662
Total (5 tranches):         $1,372,662 x 5 = $6,863,310 (~$6,863,500, rounding)
```

**Note:** A common error is to apply the 37.1% rate to the full tranche value ($4.5M x 37.1% = $1,669,500). This is wrong because it ignores the cost basis. The full $4.5M is NOT all gain. Only 82.22% of it is gain.

### Tax on $5M Liquidation (SBL Comparison)
```
Gain in $5M sale:   $5,000,000 x 0.8222 = $4,111,000
Tax:                $4,111,000 x 0.371 = $1,525,181
Net to foundation:  $5,000,000 - $1,525,181 = $3,474,819
```

---

## SECTION 2: RISK METRICS

### Beta
Measures a portfolio's sensitivity to market movements relative to a benchmark (S&P 500 = 1.0).
- Beta > 1.0: More volatile than the market
- Beta < 1.0: Less volatile than the market
```
Current: 1.35 (amplifies every S&P move by 35%)
Optimized: 0.88 (dampens market moves)
Change: (0.88 - 1.35) / 1.35 = -34.8%
```
"The current portfolio takes on 53% more market risk":
```
(1.35 - 0.88) / 0.88 = 53.4% more risk than the optimized portfolio
```

### Value at Risk (VaR) at 95% Confidence
The maximum expected loss over a given period at a given confidence level. A 95% VaR of $4.25M means there is a 5% chance of losing MORE than $4.25M in any given period.
```
Current VaR (95%): $4,250,000
Optimized VaR (95%): $1,875,000
Change: ($1,875,000 - $4,250,000) / $4,250,000 = -55.9%
```

### Maximum Drawdown
The largest peak-to-trough decline an asset or portfolio has historically experienced. Expressed as a percentage.
```
Current: 45.0% (a repeat of 2008 could erase $11.25M)
Optimized: 22.0%
Change: (22% - 45%) / 45% = -51.1%
```

### Sharpe Ratio
Measures risk-adjusted return. How much return you earn per unit of risk taken.
```
Formula: (Portfolio Return - Risk-Free Rate) / Standard Deviation
Current: 0.38 (poor — high risk, moderate return)
Optimized: 0.68 (better — more return per unit of risk)
Change: (0.68 - 0.38) / 0.38 = +78.9%
```
A higher Sharpe ratio means the portfolio is more efficient — you're getting more return for the same (or less) risk.

### S&P 500 Correlation
Measures how closely a portfolio moves with the S&P 500. Range: -1.0 to +1.0.
- 1.0: Perfect positive correlation (moves in lockstep)
- 0.0: No correlation
- -1.0: Perfect inverse correlation
```
Current: 0.94 (essentially a leveraged S&P 500 exposure)
Optimized: 0.68
Change: (0.68 - 0.94) / 0.94 = -27.7%
```

### Concentration Risk Score
A composite score (0-100) measuring portfolio concentration. Higher = more concentrated = more fragile.
```
Current: 95/100 (extreme concentration)
Optimized: 15/100 (well-diversified)
Change: -84.2%
```

### Annual Income
```
Current: $112,500 (0.45% yield on $25M — tech equity pays minimal dividends)
Optimized: $625,000 (2.5% blended yield across fixed income, REITs, dividends)
Change: ($625,000 - $112,500) / $112,500 = +455.6%
"82% less income" claim: ($625,000 - $112,500) / $625,000 = 82.0%
```

---

## SECTION 3: SECURITIES-BASED LENDING (SBL)

### What It Is
A non-purpose credit facility where a client pledges a portfolio of securities as collateral to borrow cash. The securities are not sold. The client retains ownership and continues to benefit from appreciation and income. The loan proceeds can fund any purpose except purchasing additional securities on margin.

### Key Terms

**Loan-to-Value (LTV):** The ratio of the loan balance to the market value of the pledged collateral.
```
Formula: Loan Balance / Collateral Market Value
At origination: $5,000,000 / $15,000,000 = 33.3%
```

**Margin Call Trigger:** The LTV level at which the lender requires the borrower to either post additional collateral or repay part of the loan. Set at 40% LTV here.

**SOFR (Secured Overnight Financing Rate):** The benchmark rate that replaced LIBOR. Used as the floating base rate for many institutional loans.
```
SOFR:              4.5%
Credit Spread:    +2.0%
All-In SBL Rate:   6.5%
```

**After-Tax SBL Rate:**
```
Formula: SBL Rate x (1 - Marginal Tax Bracket)
6.5% x (1 - 0.37) = 6.5% x 0.63 = 4.095% (~4.10%)
```
Interest on investment loans is generally deductible against investment income. The 37% marginal bracket is used (not the 37.1% blended LTCG rate — this is ordinary income treatment).

### Interest Calculations
```
Annual Gross Interest: $5,000,000 x 6.5% = $325,000
Annual Net Interest:   $5,000,000 x 4.095% = $204,750
Monthly Interest:      $325,000 / 12 = $27,083.33
10-Year Net Interest:  $204,750 x 10 = $2,047,500
```

### Margin Call Stress Test
Collateral starts at $15,000,000. Loan stays at $5,000,000.
```
0% decline:   LTV = $5M / $15.0M = 33.3%  NO CALL
-10% decline: LTV = $5M / $13.5M = 37.0%  NO CALL
-20% decline: LTV = $5M / $12.0M = 41.7%  MARGIN CALL (above 40% threshold)
-30% decline: LTV = $5M / $10.5M = 47.6%  MARGIN CALL
```

### SBL vs. Liquidation (10-Year Advantage: $7,124,500)
The $7,124,500 figure captures the total wealth benefit of using SBL instead of liquidating $5M to fund the foundation. It accounts for:
1. More capital to the foundation ($5M via SBL vs. ~$3.47M net after tax via liquidation): +$1,525,000
2. Portfolio compounding on a larger base ($25M vs. $20M) at base rate for 10 years
3. Less the 10-year after-tax interest cost of $2,047,500

---

## SECTION 4: ASSET ALLOCATION

### Target Allocation Math
All values derived from $25,000,000 pre-tax portfolio.

| Asset Class | % | Calculation | Value |
|---|---|---|---|
| Public Equity Total | 55% | $25M x 0.55 | $13,750,000 |
| -- US Large Cap | 25% | $25M x 0.25 | $6,250,000 |
| -- Intl / EM | 17% | $25M x 0.17 | $4,250,000 |
| -- US Mid/Small | 13% | $25M x 0.13 | $3,250,000 |
| Fixed Income | 23% | $25M x 0.23 | $5,750,000 |
| Private Equity | 12% | $25M x 0.12 | $3,000,000 |
| Real Estate | 8% | $25M x 0.08 | $2,000,000 |
| Cash | 2% | $25M x 0.02 | $500,000 |

Check: 25+17+13 = 55 ✓ | 55+23+12+8+2 = 100 ✓

### Asset Class Definitions

**Public Equity:** Stocks of publicly traded companies. Divided into US large cap (S&P 500 type), international/EM (foreign developed and emerging markets), and US mid/small cap.

**Fixed Income:** Bonds and debt instruments. Generates regular coupon (interest) payments. Categories here include investment grade corporate bonds, high-yield (junk) bonds, and municipal bonds.

**Private Equity:** Ownership stakes in private (non-publicly traded) companies. Accessed via funds (buyout or venture capital). Illiquid with a typical 7-10 year lock-up. Targets higher returns through operational improvement and illiquidity premium.

**Real Estate:** Physical property or real estate investment vehicles. Can include direct ownership, REITs, or private real estate funds. Provides inflation hedge and income.

**Illiquidity Premium:** The additional return investors demand for holding an asset that cannot be quickly sold. Private equity and real estate capture this premium vs. liquid public markets.

---

## SECTION 5: GOALS-BASED PLANNING

### Scenario Assumptions
```
Bear: 5.0% gross return - 2.0% withdrawal = 3.0% net
Base: 9.8% gross return - 2.0% withdrawal = 7.8% net
Bull: 13.5% gross return - 2.0% withdrawal = 11.5% net
```

### Projection Formula
Simple compound growth applied annually to the post-tax starting portfolio.
```
Formula: Starting Value x (1 + Net Rate)^Years
Starting Value: $18,986,500
```

**Spot Check Examples:**
```
Bear Year 5:  $18,986,500 x (1.03)^5  = $18,986,500 x 1.15927 = $22,010,557
Base Year 10: $18,986,500 x (1.078)^10 = $18,986,500 x 2.11999 = $40,237,642
Bull Year 20: $18,986,500 x (1.115)^20 = $18,986,500 x 8.82059 = $167,472,021
```

### Why Net Rate = Gross Minus Withdrawal Rate
The 2.0% annual withdrawal is treated as a drag on the compounding rate. Instead of computing withdrawals separately, netting the rate is a simplification that assumes withdrawals are proportional and continuous. For projection purposes this is standard practice and produces directionally accurate results.

### Private Foundation Projection

**Inputs:**
```
Seed capital (via SBL):    $5,000,000
Annual contribution:        $70,760 (from portfolio income)
Foundation net return:      2.5% (7.5% gross - 5.0% annual grantmaking payout)
```

**Formula (Future Value of lump sum + annuity):**
```
FV = PV x (1+r)^n + PMT x [(1+r)^n - 1] / r

Year 20:
= $5,000,000 x (1.025)^20 + $70,760 x [(1.025)^20 - 1] / 0.025
= $5,000,000 x 1.63862 + $70,760 x 25.5446
= $8,193,100 + $1,807,574
= $10,000,674 (~$10,000,000 target) ✓

Year 10:
= $5,000,000 x (1.025)^10 + $70,760 x [(1.025)^10 - 1] / 0.025
= $5,000,000 x 1.28008 + $70,760 x 11.2034
= $6,400,400 + $792,752
= $7,193,152 (~$7.2M) ✓
```

**Why 5% annual grantmaking?** The IRS requires private foundations to distribute at least 5% of net assets annually as qualifying distributions (grants, program expenses). This is the *minimum distribution requirement* for private foundations.

---

## SECTION 6: ADDITIONAL TERMS

### Donor-Advised Fund (DAF)
A charitable giving vehicle. The donor contributes cash or appreciated securities, takes an immediate tax deduction, and recommends grants to charities over time. Contributing appreciated stock directly to a DAF avoids capital gains on the contributed shares entirely.

### Qualified Opportunity Zone (QOZ)
A federal tax incentive (created by the 2017 Tax Cuts and Jobs Act) that allows investors to defer and potentially reduce capital gains taxes by reinvesting gains into designated low-income census tracts (Opportunity Zones) through a Qualified Opportunity Fund. Holding for 10+ years eliminates tax on QOZ appreciation entirely.

### Charitable Remainder Trust (CRT)
An irrevocable trust that allows the donor to: (1) contribute appreciated assets, (2) receive an income stream for life or a term of years, (3) take a partial charitable deduction, and (4) defer or avoid capital gains on the contributed assets. The remainder passes to a designated charity at the end of the term.

### Installment Liquidation (Tax Year Straddle)
By straddling a December-to-January calendar year split across the five tranches, a portion of recognized gains falls into the following tax year. This delays the cash tax payment by one year on that portion and can smooth the client's income across years, potentially keeping them below certain surtax thresholds.

### Net Investment Income Tax (NIIT) Threshold
The 3.8% NIIT applies to the lesser of: (a) net investment income, or (b) the amount by which MAGI exceeds $200,000 (single) or $250,000 (married filing jointly). For a client with $18.5M in gains, this threshold is easily exceeded and the full 3.8% applies to all investment income.

### Sharpe Ratio (Extended)
```
Sharpe = (Rp - Rf) / σp
Rp = Portfolio return
Rf = Risk-free rate (typically 10-year Treasury yield)
σp = Standard deviation of portfolio returns
```
A Sharpe ratio below 0.5 is generally considered poor. Above 1.0 is good. Moving from 0.38 to 0.68 is a meaningful improvement in return efficiency but not yet in "excellent" territory — appropriate for a multi-asset portfolio with private equity and real estate exposure (which dampen short-term volatility but compress measured Sharpe ratios due to appraisal-based pricing).

### Beta (Extended)
```
Beta = Covariance(Portfolio, Market) / Variance(Market)
```
A beta of 1.35 means: if the S&P 500 drops 10%, the portfolio historically drops ~13.5%. A beta of 0.88 means: if the S&P 500 drops 10%, the portfolio drops ~8.8%. Lower beta = smoother ride, less amplified losses.

### LTV (Loan-to-Value) in SBL Context
Unlike mortgage LTV (loan / property value), SBL LTV uses the market value of pledged liquid securities as the denominator. Because securities can be volatile, lenders set conservative trigger points (40% here) well below the maximum (typically 50-70% depending on asset type) to build in a cushion before a margin call is required.

---

## QUICK REFERENCE: KEY FIGURES

| Figure | Value | Source |
|---|---|---|
| Portfolio Value | $25,000,000 | Input |
| Cost Basis | $6,500,000 | Input |
| Unrealized Gains | $18,500,000 | $25M - $6.5M |
| Blended Tax Rate | 37.1% | Fed 20% + NIIT 3.8% + CA 13.3% |
| Gross Tax Liability | $6,863,500 | $18.5M x 37.1% |
| TLH Offset | $850,000 | Identified harvest opportunities |
| Net Tax Liability | $6,013,500 | $6,863,500 - $850,000 |
| Post-Tax Portfolio | $18,986,500 | $25M - $6,013,500 |
| SBL Loan | $5,000,000 | Input |
| SBL Collateral | $15,000,000 | Input |
| SBL LTV | 33.3% | $5M / $15M |
| SBL All-In Rate | 6.50% | SOFR 4.5% + 2.0% spread |
| SBL After-Tax Rate | 4.095% | 6.5% x (1 - 0.37) |
| Annual Gross Interest | $325,000 | $5M x 6.5% |
| Annual Net Interest | $204,750 | $5M x 4.095% |
| 10-Year Net Interest | $2,047,500 | $204,750 x 10 |
| Annual Portfolio Income (Optimized) | $625,000 | ~2.5% blended yield on $25M |
| Foundation Annual Contribution | $70,760 | Directed from portfolio income |
| Foundation Target | $10,000,000 | Client goal |
| Foundation Year 10 Value | ~$7,200,000 | FV calculation |
| Foundation Year 20 Value | ~$10,000,000 | FV calculation |
| Projection Start | $18,986,500 | Post-tax portfolio |
| Bear Net Rate | 3.0% | 5.0% gross - 2.0% withdrawal |
| Base Net Rate | 7.8% | 9.8% gross - 2.0% withdrawal |
| Bull Net Rate | 11.5% | 13.5% gross - 2.0% withdrawal |
| Year 20 Base Portfolio | $85,274,686 | $18,986,500 x 1.078^20 |
