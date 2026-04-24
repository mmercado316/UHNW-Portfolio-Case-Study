# Client Book Project — Working Memory v2

Comprehensive working memory of locked substance for the UHNW prospecting case study. Use this file to resume work across sessions. Supersedes memory.md (which captured pre-flight context only).

---

## STATUS

We are in the **substance-locking phase** before drafting the final deliverable.

**Locked:**
- Frame (bespoke Client Book; AI-augmented in build but not body headline; not a JPM playbook)
- Naming convention (Prospect 1/2/3; Existing Client 1/2/etc; COI 1/2/etc)
- Three-layer Prospect File architecture (Profile / Decision Log / Relational Graph)
- 14-category Layer 1 schema with ~150 fields and if/thens
- Layer 2 Decision Log structure (6 entry types) with worked example
- Layer 3 Relational Graph (COI Ledger + Pattern Map) with worked example
- Inference Layer (5 rules + 3 discovery answers) with worked example
- Prospect 1 fully populated (drafted, pending user revision notes; post-M2)
- Prospect 2 fully populated (drafted, pending user revision notes; post-M2)
- Prospect 3 fully populated (drafted, pending user revision notes; post-M1)
- Prospect 4 fully populated (drafted, pending user revision notes; pre-M1, qualification stage)

**Pending, in order:**
1. Incorporate user revision notes on Prospects 1, 2, 3, and 4
2. Strategic memo light revision (compress AI subsections, fold in 67%-of-affluent-prospects-knew-someone data point, keep tight)
3. Opening narrative light revision (probably survives mostly intact)
4. Closing questions light revision
5. Extensibility sidebar (probably survives)
6. Project card entry (revise to lead with banker craft, not toolchain)
7. Notes & Sources expansion (add Prince, Allison, Oechsli, Bowen, Mullen, Knapp, WealthManagement.com, Beyer Kitces ep, Willis, Cerulli)
8. Full fresh draft of deliverable (treat existing v1 mdx as scaffolding only, ~30–40% reusable)
9. Site integration (locate Next.js repo, reconcile frontmatter, drop into content/projects/)
10. Vercel deployment

**Prospect profiles:** live in `website/prospect_1.md`, `website/prospect_2.md`, `website/prospect_3.md`, `website/prospect_4.md`. The four are staggered across the BD funnel: Prospect 4 (qualification, pre-M1) → Prospect 3 (first-touch, post-M1) → Prospects 1 and 2 (post-M2 depth, two cultural contexts). See README.md for the full file map.

---

## PROJECT CONTEXT

**Audience:** A senior leader at a major UHNW private bank (no direct mention of name or firm anywhere in deliverable).

**Target outcome:** The reader sees Mario as someone who already thinks like a UHNW private banker, not a candidate who needs training. Drives a second-round interview.

**Vertical:** Bay Area tech UHNW (single vertical for depth). Extensibility sidebar shows schema generalizes.

**Author voice:** Mario Mercado as practicing senior UHNW private banker. Friendly but professional, direct, analytical, data-driven. Style guide: /Users/Mario/.claude/CLAUDE.md.

**The thesis:**
> "If you speak to a client and you don't know what they want and what they're looking to solve, you cannot get them a solution."

Most senior associates and VPs at UHNW advisory firms boil the ocean with templated outreach. The alternative: bespoke outreach grounded in *relationship intelligence* — a structured memory system, built from attentive listening and cross-referenced public signals, that turns conversational fragments into a coherent outreach decision. AI augments the signal layer; the banker runs the relationship.

---

## VOICE AND CONSTRAINTS (non-negotiable)

- **No em dashes anywhere.** Use commas, periods, parentheses.
- **No banned phrases:** "basically," "sync up," "push the envelope," "run it up the flagpole," "cadence" (for meetings), "leverage AI solutions," "in today's fast-paced landscape."
- **Zero firm names in body text.** Not JPMorgan, JPM, Morgan Stanley, Goldman, Bessemer, Rockefeller, Cresset, Pathstone, BBH, Wells Fargo, UBS, Schwab. Firms and practitioners may appear ONLY in Notes & Sources.
- **Zero individual names in body text.** Not Beyer, Grubman, Kochis, Jaffe, Willis, Allison, Oechsli, Bowen, Prince, Mullen, Knapp, duQuesnay. Names go in Notes & Sources only.
- **Framing:** relationship intelligence captured from attentive listening, cross-referenced with public signals. NOT data harvesting. NOT covert surveillance.
- **Prospecting goal:** convert a cold or warm lead into a first seated conversation. NOT close business. NOT sell a product.
- **Active voice default.** Passive voice rare.
- **No hedging on data-backed claims.** Avoid "somewhat," "rather," "quite," "I believe," "in my opinion."
- **Italicize technical terms on first use:** *relationship intelligence*, *centers of influence*, *book*.
- **Headers as thesis statements** that argue, not just label.
- **Cause-effect language:** "driven by," "results in," "necessitates."
- **Closing:** forward-looking questions about how the practice evolves, not prescriptive call-to-action.

---

## FRAME DECISIONS (locked through conversation)

1. **The piece is a Client Book case study, NOT a JPM prospecting curriculum.** Every research finding from the operational craft pass (Prince/Allison/Oechsli/Bowen/etc.) lands as "this is what the Prospect File captures" or "this is the decision the Prospect File drives," NOT as top-down methodology.

2. **AI supplements the prospecting process; it does not drive it.** The case-study title is "The Client Book: Relationship Intelligence for UHNW Prospecting" (no "AI-Augmented" in the title). The strategic memo no longer has a standalone AI section; incidental AI references appear only where accurate to industry practice (templated-outreach cadence, provenance discipline around public-record synthesis) and in third-party landscape grounding (tier-one firm positions) held in an "Additional context" footer of Notes & Sources rather than as body-cited material. Banker craft is the body's center of gravity.

3. **Length constraint relaxed.** The deliverable will render as discrete sections on the Vercel site, not as one long document. Don't over-optimize for word count; optimize for content correctness.

4. **Naming convention.** Prospect 1, Prospect 2, Prospect 3. Existing Client 1, Existing Client 2, etc. COI 1, COI 2, etc. No fictional names.

5. **Sensitive information held with discipline.** Sensitive fields (Cat 13) are empty by default and never extrapolated. Entry only when the prospect themselves volunteers the fact. The piece says this out loud as a discipline.

6. **The deliverable comes LAST.** Substance first (schema, profiles, inference layer), then framing revisions, then a fresh draft. The existing v1 mdx is scaffolding only.

---

## ARCHITECTURE: THREE LAYERS

**Layer 1: Profile** — static facts per prospect. 14 categories, ~150 fields. What the prospect IS.

**Layer 2: Decision Log** — running journal per prospect. Dated entries of inferences, moves considered, moves taken, outcomes. What the BANKER has thought and done.

**Layer 3: Relational Graph** — COI Ledger (one record per intro source, used across many prospects) + Pattern Map (per prospect, links to Existing Clients with similar signal sets). The connective tissue.

A Prospect File pulls from all three layers. The COI ledger is shared across prospects. Pattern-match references cross-link to handled clients.

---

## LAYER 1 SCHEMA — full field list

Each field tagged **[DD]** (decision-driving with if/then) or **[REF]** (reference, supports other fields). If/thens follow each DD field.

### Cat 1 — Core identity and residences

Establishes who the prospect is, which jurisdictions apply, rhythm of presence. Drives timing and jurisdictional framing of outreach.

- **Legal name** [REF]
- **Preferred name / informal name** [DD]. *If they consistently use a preferred name different from their legal name, use it in every written touch; using the legal name in a first email signals the banker pulled the name from a database.*
- **Date of birth** [REF]
- **Age and current life-stage** [DD]. Early-operator, mid-career, pre-exit, post-exit, semi-retired, retired, elder. *If pre-exit (18+ months before known liquidity event), open with pre-liquidity framing; if post-exit past 18 months, that framing is late.*
- **Citizenship(s) and active passports** [DD]. *If dual citizenship with active second passport in use, opening routes through jurisdictional estate structure, not US-only trust planning.*
- **Languages and fluency** [DD]. Language used in business, family, emotional contexts. *If they process emotional content in a second language, route culturally-loaded conversations through a colleague or COI fluent in that language.*
- **Religion and level of observance** [DD, volunteered only]. *If observant, no substantive outreach during high holy days, Ramadan, Lent, Lunar New Year, Diwali. Congregation-based intros via co-congregant outperform cold channels.*
- **Primary residence** [REF]
- **Secondary residences with rationale** [DD]. *If secondary in a different tax jurisdiction with material time spent there, trigger domicile-planning conversation. If stated reason is "my parents live there," route outreach through the family connection.*
- **Tax domicile state** [DD]. *If recently changed or under consideration, open with state-tax-driven planning (exit-tax exposure, grantor-trust situs, residency steps). If stable and high-tax (CA, NY), frame around migration optionality.*
- **Weeks per year at each location** [DD]. *If 12+ consecutive weeks at secondary residence, time outreach to physical presence. During absence, spouse or EA becomes access point.*
- **Household staff signals** [REF]
- **Visa / green card status** [DD]. *If non-immigrant visa or green card, pre-naturalization or expatriation planning may apply.*
- **Preferred pronouns** [REF/DD]. Volunteered only. Calibrates written outreach.
- **EA / chief-of-staff direct contact** [DD]. *If gatekeeper exists, build that relationship as first-class; gifts and direct outreach to them are not optional.*
- **Birthplace and where raised** [DD]. Distinct from current residence. *Drives cultural-orientation calibration; a prospect born in San Jose to Vietnamese parents reads differently than a prospect born in Hanoi.*
- **Marital and civil status** [REF, with downstream implications]. Married, single, divorced, widowed, partnered, prior marriages.
- **Residence ownership structure** [DD]. *If primary residence is in an irrevocable trust, the prospect has done sophisticated estate work; basic planning insults them. If $50M+ net worth and primary in personal name, that gap is an opener.*
- **Domicile history and supporting evidence** [DD]. Voter registration, driver's license, primary doctor, club, mail address. *If claimed new low-tax domicile but voter registration and driver's license remain in prior state, audit risk elevated; planning conversation around domicile substantiation is a strong opener.*

### Cat 2 — Family, multi-generational

Drives spouse engagement, generational planning timing, decision-rights mapping, emotional weight.

- **Spouse name, age, background** [REF]
- **Spouse citizenship and immigration status** [DD]. *If non-US spouse and US prospect (or vice versa), trigger QDOT and spousal-gift conversation; standard unlimited marital deduction does not apply.*
- **Spouse financial agency** [DD]. Primary, joint, passive, non-participant. *If spouse is primary decision-maker, prospect-only first meeting is wasted; pivot to couple-format venue.*
- **Marriage history and prenup status** [DD]. *If second marriage with children from a first, open with discretionary-trust conversation that protects prior-marriage children's interests.*
- **Children: names, ages, life stage** [REF]
- **Children's schools, every level** [DD]. *If children attend immersion schools in family's heritage language, legacy-and-transmission framing outperforms capital-allocation framing; specific private schools' development offices are high-yield COIs.*
- **Each child's relationship quality with prospect** [DD]. *If a specific child is in a strained relationship, do not propose intergenerational governance requiring their seat; route around with separate trusts.*
- **Each child's career stage and financial dependency** [DD]. *If an adult child is financially dependent, planning routes through structured discretionary trusts, not outright gifts.*
- **Grandchildren: names, ages** [REF]
- **Parents: living, where, health, dependency** [DD]. *If aging parent lives with prospect or nearby without long-term-care plan, open with multi-generational planning that includes parent's care.*
- **Siblings: count, locations, relationship, financial dependency** [DD]. *If prospect is high-earning sibling supporting siblings, planning includes structured family-loan or trust mechanisms; surfaces with discovery question.*
- **In-laws: parallel data** [REF/DD when material]
- **Extended family within 2-hour drive** [DD]. *If robust extended family in market, family-philanthropy conversation (small foundation or DAF with cousins as advisors) opens different door than household-wealth conversation.*
- **Designated executors, trustees, health proxies** [REF/DD]. *If named trustee is sibling rather than professional fiduciary, surface corporate-trustee or co-trustee conversation.*
- **Household staff and key household contacts** [DD]. *If chief of staff or family-office principal exists, that person becomes calendar/document gatekeeper; outreach often routes through them.*
- **Pets** [REF, soft]. Notable when ownership signals lifestyle pattern (horses, working dogs, show stables).

### Cat 3 — Education, across generations

Drives alumni-network intro routes, school-development-office relationships, K-college planning, cultural calibration.

- **Prospect's undergraduate institution** [DD]. *If active alum (mentions reunions, gives, attends events), alumni development office is viable COI; intros via fellow alums often outperform other warm channels.*
- **Prospect's graduate institutions** [DD]. *If holds JD and practiced before pivoting, frame trust-and-estate conversations in technical language; novice framing insults them.*
- **Prospect's high school (when private or boarding)** [REF]
- **Prospect's professional certifications and continuing ed** [REF]. CFA, CPA, CFP, executive ed, board governance.
- **Spouse's education at all levels** [REF/DD]. Material when spouse's alumni network includes useful COIs.
- **Children's schools, every level (K through grad)** [DD]. *If child at specific private school, school's parent network and development office are high-yield COIs.*
- **Children's college and graduate school** [DD]. *If child in college, 529 review and gift-tax-funded education trust conversations are timely.*
- **Grandchildren's schools** [REF]
- **Notable extended family education** [REF]
- **Alumni affiliations and giving history** [DD]. *If prospect chairs a capital campaign at alma mater, treat as active major-gifts donor; philanthropy conversation is more accessible than wealth conversation.*

### Cat 4 — Wealth story

Drives every product and structuring conversation. Shapes emotional posture toward wealth.

- **Wealth source(s)** [DD]. Founder equity, employee equity, inheritance, operating business, professional practice, real estate, secondary sales, M&A or fund carry, royalties. *If from inheritance, frame around stewardship and continuation; if self-built operating, frame around continuation and risk transfer; "wealth management" framing collapses for inheritors who do not identify as wealthy.*
- **Wealth-building timeline** [DD]. *If recent (under 24 months from event), prospect is in psychological adjustment window; early conversations do identity work, not portfolio work. Multi-decade wealth skips identity and goes to optimization and continuity.*
- **Liquidity event history** [DD]. Pre-, in-, post-event with dates and approximate values. *6 to 18 months pre-event, lead pre-liquidity (10b5-1, AMT, QSBS stacking, exchange funds, CRT); past 18 months post-event, late.*
- **Net worth tier estimate** [DD]. *Under $50M, lead with consolidation; above $250M, lead with intergenerational structuring.*
- **Liquid vs. illiquid split** [DD]. *Less than 20% liquid, conversation is about creating liquidity (SBL, exchange funds, secondary sales, single-stock hedging). Greater than 70%, conversation is about deployment and structure.*
- **Asset concentration in a single position** [DD]. *Above 70% in one position, do not open with diversification; reads as criticism. Open with risk-insurance framing (collars, prepaid forwards, exchange funds).*
- **Existing trust structures** [DD]. Revocable, irrevocable, dynasty, GRAT, CRT, ILIT, GST, IDGT, CLT, plus home-country trusts. *If sophisticated stack, planning conversation is coordination and tax-efficient unwinding; introductory trust pitch insults them.*
- **DAF and foundation status** [DD]. *If DAF exists but no foundation, strategic-philanthropy conversation about foundation formation is strong opener. If foundation exists, conversation is governance, programmatic strategy, mission-related investing.*
- **Known tax moves executed** [DD]. QSBS qualification and stacking, 10b5-1, exchange funds, PPLI, CRT/CLT, valuation discount work. *If QSBS claimed but not stacked across spouse and trusts, the gap is an opener.*
- **Existing custodians, banks, advisors** [DD]. Platforms and named advisors with relationship duration and stated satisfaction. *If single individual at wirehouse, team-based-bench framing is opener. If MFO, conversation is specific gaps in MFO coverage, not wholesale replacement.*
- **Known insurance structures** [REF/DD]. PPLI, life, LTC, umbrella. Material when underinsured.
- **Credit relationships** [DD]. Mortgages, margin, SBL, art-backed financing. *If no SBL line in place and significant marketable securities, SBL setup is quiet, low-intensity opener.*
- **Known collectibles, art, aircraft, yacht** [REF]
- **Compensation structure and vesting timing** [DD]. For active operators: when bonuses pay, stock vests, carry crystallizes. *Drives WHEN to surface concentrated-stock conversations and tax-deferral structures.*
- **Multi-advisor structure** [DD]. How they split work today (assets at one firm, trust at another, tax at a third, philanthropy at a fourth). *If split with no quarterback, convening-advisor opportunity is opener; if consolidated, second-opinion path applies.*
- **Family-office or family-council participation** [DD]. For G2/G3 with structured family office. *If active in governance, conversation routes through governance. If absent or excluded, that absence is a planning question.*
- **Generation of wealth** [DD]. G1 creator, G2 inheritor, G3 trustee, beyond.
- **Adjustment posture** [DD]. Denial, assimilation, integration (Grubman). *If G1 in denial or assimilation, identity work precedes optimization conversation; if G3 integrated, skip identity and go directly to governance and continuity.*

### Cat 5 — Professional history and boards

Drives sector-specific framing, board-meeting timing, identification of fellow board members as warm-intro routes.

- **Current role and employer** [REF]
- **Career narrative arc (in their words)** [DD]. *If series of operator roles, frame around active operating identity; if single founder identity ("I built X"), the company is the central biographical fact and any reference must be precise.*
- **Companies founded, exited, sold** [DD]. *If co-founded with someone they no longer reference (avoidance signal in Cat 12), do not introduce co-founder's name in conversation.*
- **Current operating role** [DD]. *If active operator at venture-backed company, calendar discipline severe; one-meeting first asks; prefer asynchronous follow-ups, 7am or 7pm window.*
- **Public company board seats** [DD]. *Treat as fiduciary-experienced peer; fiduciary-duty language lands precisely. Fellow board members are high-yield warm-intro routes.*
- **Private company board seats** [DD]. Drives identification of co-board members and shared advisor networks.
- **Non-profit and philanthropic board seats** [DD]. *If chairs non-profit board, philanthropic conversation routes through existing board work, not new-cause introduction.*
- **Industry vertical and sub-vertical expertise** [REF]
- **Professional associations and trade memberships** [REF]
- **Notable past employers** [REF]
- **Public profile and published content** [DD]. Whether prospect publishes essays, posts on LinkedIn, gives interviews, appears on podcasts. *Their published content tells you what they think about. Reference a specific essay or quote in a way that demonstrates real reading. If private, do not surface their public content unprompted.*

### Cat 6 — Cultural origin and orientation

Drives vocabulary, calendar, advisor-fit framing, choice of intro source.

- **Country of origin and family-identified country** [DD]. *If family identifies with country different from where prospect was born, route emotional and family-centered conversations through family-identified country.*
- **Generation in the US (or adopted country)** [DD]. First, 1.5, second, third. *If first-generation, treat as immigrant to wealth in addition to immigrant to country.*
- **Childhood-home language** [DD]. *If different from daily working language, certain conversations (parents, legacy, children) gain access by routing through that language.*
- **Languages spoken at home today** [REF/DD]
- **Ties to home country: property** [DD]. *If maintains real estate abroad, cross-border-trust and basis-step-up conversation timely.*
- **Ties to home country: family** [DD]. *If parent or sibling depends on prospect across borders, planning includes international remittance, currency exposure, possibly offshore family entity.*
- **Ties to home country: business** [DD]. *If retains operating business interest abroad, conversation is bi-jurisdictional.*
- **Travel frequency to home country** [DD]. *If more than twice annually for extended stays, calendar respects this; outreach during absence routes through spouse or EA.*
- **Religion and observance level** [DD]. Cross-references Cat 1.
- **Cultural and religious holidays observed** [DD]. *Calendar discipline. Timely greeting in observed tradition (sent by hand) builds quiet relational equity.*
- **Immigration story** [REF/DD]. *If political (refugee, asylum, post-conflict), home-country topic carries trauma; do not press for detail not volunteered.*
- **Naturalization status and timing** [DD]. *If on visa or green card, pre-naturalization or expatriation planning may apply.*
- **Family decision-making cultural mode** [DD]. Individualist, Collective Harmony, or Honor (Jaffe & Grubman three-culture). *If Collective Harmony, no commitment possible until group aligns. If Honor, route early outreach through patriarch even if prospect is operator generation.*

### Cat 7 — Food, beverage, dietary

Drives venue choice, gift selection, meal-based meeting design.

- **Dietary restrictions** [DD]. Kosher, halal, vegetarian, vegan, gluten-free, allergies, religious fasts. *If kosher or halal, propose venue that accommodates without theatrical effort; if vegetarian by religious observance (Hindu, Buddhist, Jain), venue should reflect understanding.*
- **Cuisine preferences and aversions** [DD]. *If avoided a cuisine three meetings in a row, do not propose it.*
- **Favorite restaurants and venues they have suggested** [DD]. *If selected a venue once, propose it again for second material meeting; venue continuity is low-friction comfort signal.*
- **Wine preferences** [DD]. Specific varietals, regions, producers, vintages. *Calibrate restaurant choice to wine list. Bottle gift for personal milestone pulls from prospect's referenced producer set, never from generic "good wine" list.*
- **Spirits and liqueurs** [REF/DD]
- **Coffee and tea preferences** [REF]
- **Drinking patterns and posture** [DD]. Social, oenophile, abstainer, recovering. *If abstaining, never propose wine-centered dinner; do not signal awareness of why they abstain unless they have volunteered it.*
- **Smoking, cigars, vaping** [REF]
- **Hosting style at home** [REF]

### Cat 8 — Sports, fitness, hobbies, travel

Drives event-based outreach, gift selection, texture of small talk.

- **Athletic and fitness habits** [DD]. *If runner, propose morning run as venue; if tennis at specific club, club programming viable warm-intro route. If golfer, course is canonical UHNW venue.*
- **Teams followed and season tickets** [DD]. *If season tickets to specific team, invitation to comparable game in team's away city is thoughtful gift.*
- **Hobbies and collections** [DD]. Wine, art, classic cars, watches, books, photography, music, woodworking, gardening, hunting, fly-fishing, sailing, horology, philately, numismatics. *Specificity is the signal. Wine-loving prospect declines art events; art-loving declines wine dinners.*
- **Travel patterns** [DD]. Annual rhythm. *If August routes through specific location, time back-half outreach for September.*
- **Favorite destinations** [REF]
- **Private aviation use** [DD]. *If owns aircraft, calendar logistics expand; conversation about aircraft itself is technical and identity-loaded.*
- **Pets and animals (lifestyle scale)** [REF]
- **Cultural consumption** [REF]. Theater, opera, ballet, jazz, classical, contemporary art.

### Cat 9 — Personality and communication

Drives meeting format, channel, evidence density, pacing.

- **Reserved vs. outgoing** [DD]. *If reserved, propose one-on-one tea, walking meeting, or small breakfast; six-person dinner is a disaster.*
- **Analytical vs. intuitive** [DD]. *If analytical, lead with one-page tax model or scenario analysis; if intuitive, lead with story about comparable family.*
- **Skeptical vs. receptive** [DD]. *If skeptical, open by naming what you do not yet know about their situation; if receptive, lead with specific observation that demonstrates work already done.*
- **Detail-oriented vs. big-picture** [DD]. *If detail, send fully built financial summary 24 hours before; expect mark-ups. If big-picture, one-page summary; model lives in appendix.*
- **Decisive vs. deliberative** [DD]. *If decisive, in-meeting commitment achievable on right setup. If deliberative, build six-month relationship arc with two seated conversations and explicit offline-thinking time between.*
- **Humor and warmth** [REF]
- **Preferred communication channel** [DD]. Email, text, phone, LinkedIn, in-person only. *Match channel exactly.*
- **Response-time norm** [DD]. *Asking an "always responds in a week" prospect to confirm by tomorrow signals you do not understand their time.*
- **Calendar gatekeeping** [DD]. EA, chief of staff, spouse, none. *If EA controls calendar, build that relationship as first-class.*
- **Preferred meeting time of day** [DD]
- **Preferred meeting length** [DD]
- **Venue preferences and aversions** [DD]
- **Five Ps rank ordering** [DD]. People, Philosophy, Process, Performance, Fees (Beyer). *If over-indexes Performance, they are buying the last three years; if over-indexes Fees, prior bad experience with opacity. Calibrate the entire pitch around the heaviest P.*
- **Media and information diet** [REF/DD]. *If public posting cadence on specific topic, content shared on that topic lands; off-topic content reads as outreach.*

### Cat 10 — Philanthropy

Drives warmest non-commercial entry to household and framing of legacy conversations.

- **Causes supported** [DD]. *If funds specific named cause through repeat gifts, substantive content piece on that cause's funding landscape is low-pressure relational opener; never propose a cause they have not signaled.*
- **Giving vehicle** [DD]. DAF, private foundation, LLC (CZI model), supporting organization, CRT, CLT, direct.
- **Annual giving cadence and approximate scale** [REF]
- **Naming gifts and major-gift history** [DD]. *If naming gift made, recipient organization's development office is high-yield COI route.*
- **Non-profit board seats** [DD]. *If chairs board, other directors are warm-intro candidates.*
- **Family involvement in philanthropy** [DD]. *If family-philanthropy structure already includes adult children, next-generation governance conversation routes through that existing structure.*
- **Private operating foundation activity** [REF/DD]
- **Philanthropic peer network** [REF]

### Cat 11 — Network, memberships, centers of influence

Feeds Layer 3 (COI ledger). Captures relational ecosystem.

- **Close friends referenced by first name** [DD]. *If a name recurs across meetings, candidate intro source if also relevant by other criteria; surface to prospect indirectly ("how do you know X?").*
- **Clubs and memberships** [DD]. Olympic Club, Battery, Jonathan Club, Pacific Union, country clubs, golf, yacht, dining clubs. *Meeting at prospect's home club signals comfort that office meeting cannot.*
- **Alumni networks active in** [DD]. *If active, alumni event introduction often outperforms cold professional touch.*
- **Mutual professional connections** [DD]. *Validate relationship quality before requesting intro; "mutual connection" who is actually casual acquaintance is worse than cold approach.*
- **Known prior advisors and how the relationships ended** [DD]. *If ended on fee issue, do not open with performance; open with transparency. If on service, lead with team-bench framing. If on single-incident error, name category of error in diagnostic question without naming the firm.*
- **Stated views on advisors as a class** [DD]. *Calibrate framing accordingly; a prospect who says "they're all the same" needs the meeting to feel different in form, not just in claim.*
- **Active intro-source ledger references** [REF]. Cross-references Layer 3 COI Ledger.
- **Decision-making style for advisor selection** [DD]. Single meeting, multi-meeting, requires references, requires team meeting, requires spouse approval, requires sample work. *Selection process is rehearsal of working relationship.*
- **Stated criteria for engaging a new or additional advisor** [DD]. *Most prospects do not voice this directly but signal it across meetings. The Prospect File records inferred criteria; next material proposal addresses them explicitly.*

### Cat 12 — Conversational signals and behavioral notes

Most diagnostic single category for outreach decisions; often overrides "harder" data when in tension.

- **Topics volunteered unprompted** [DD]. *Topic raised twice without prompting is prospect signaling weight; route next material outreach through that topic.*
- **Topics avoided or deflected** [DD]. *Avoided topic is data, not silence; do not solve for it and do not stumble into it.*
- **Topics returned to repeatedly** [DD]. *Returning to topic across multiple meetings signals unresolved processing; next outreach offers structural answer, not sympathetic ear.*
- **Names referenced by first name vs. last name vs. never named** [DD]. *First name = intimates or peers; full name = formal distance; never named when cited = deeply intimate or actively suppressed. Pattern locates prospect's relational map without asking.*
- **Inside jokes and recurring humor** [REF]
- **Pacing and energy in conversation** [REF/DD]. *Match pace.*
- **Boundaries explicitly voiced** [DD]. *Honor every voiced boundary; transgression closes the relationship faster than any other failure.*
- **Behavioral notes from non-verbal observation** [REF]
- **Stated motivations and goals (discovery answers)** [DD]. Recorded answers to: most important about wealth, most proud of, where they want to go from here, what makes "success in three years" look right, most important relationships, what they enjoy when not working. *These answers ARE the outreach thesis. Next material outreach must route through one of these answers explicitly; failing to do so signals discovery was theater.*
- **Prior-advisor diagnostic answers** [DD]. Answers to "What was your experience with prior advisors? How did you choose them? What did you learn?" *Answers reveal selection model and where last relationship broke. First material proposal addresses gap surfaced.*
- **Stated time horizon for planning** [DD]. 1Y, 5Y, 10Y, generational. *If generationally, route through dynasty trusts and family governance. If 5Y, scope around tactical structuring within decision window.*
- **Risk posture in their own words** [DD]. *Distinct from any RTQ score. Narrative is more diagnostic than score; route conversations around narrative, not against it.*
- **First vs. third-person wealth language** [DD]. (Willis diagnostic) *If consistent third-person language ("the money," "my family's assets"), product pitch premature; first mandate is psychological. Carry inheritor through identity work before any portfolio proposal.*

### Cat 13 — Sensitive information (volunteered only)

Highest discretion. Empty by default. Captured only as prospect volunteers, never speculatively, never inferred from public data.

- **Volunteered health status** [DD, volunteered only]. *If serious condition, planning includes incapacity documents, trustee succession, life-insurance review; do not surface unless prospect raised it.*
- **Family medical history as volunteered** [DD]. *If parent's serious illness referenced, long-term-care planning timely.*
- **Sobriety, addiction history, recovery status as volunteered** [DD]. *If shared, calibrate Cat 7 (no wine dinners, no spirits gifts, no cocktail-hour venues). Highest discretion.*
- **Mental health context as volunteered** [REF]
- **Political orientation as volunteered** [DD] (moved from Cat 1). *Calibrate ESG and philanthropy-vehicle vocabulary; never extrapolate from proxies.*
- **Stated planning fears** [DD]. *Voiced fear IS the opener. Offer specific structural answer in next material outreach, not sympathetic ear.*
- **Stated regrets and "would do differently"** [DD]. *Voiced regret is diagnostic for unmet planning needs.*
- **Family rifts and estrangements as volunteered** [DD]. *If child cut contact, sibling no longer spoken to, former co-founder excised from narrative — do not solve for the wound, route around it.*
- **Past legal or regulatory matters as volunteered** [REF/DD]. *Material when bearing on fiduciary planning. The Prospect File holds the fact; planning conversation respects without surfacing.*
- **Identity transitions as volunteered** [REF/DD]. Gender, religious conversion, naturalization in process, marital identity changes. *Material only when bearing on documents.*
- **Known fiduciary appointments tied to health** [REF]

### Cat 14 — Trigger events and timing markers

The WHEN of outreach. Calendar overlay across every other category. Most operationally useful layer once relationship is established.

- **Known forward triggers** [DD]. Planned exits, IPOs, M&A close, children's college entry, marriages, foundation launch, board rotation, sabbatical, anticipated parent care, lockup releases, major-gift commitments due. *Outreach times to trigger. Trust conversation 60 days before planned IPO is timely; six months after is late.*
- **Personal milestones and significant dates** [DD]. Birthdays, wedding anniversary, children's birthdays, parents' birthdays, deceased-family-member anniversaries, naturalization date, exit anniversary, founding anniversary. *Handwritten note on right anniversary signals memory. Deceased-family-member anniversaries particularly load-bearing because most advisors do not track them.*
- **Recent personal transitions** [DD]. Last 12 to 24 months: deaths, births, marriages, divorces, moves, empty nest, illnesses, retirements. *Recent transition almost always changes a planning need. Death of parent triggers estate review; empty nest triggers residence and giving review; divorce triggers beneficiary refresh. Window is 90 days, not later.*
- **Liturgical and observance calendar windows** [DD]. High holy days, Ramadan, Lent, Lunar New Year, Diwali, Holi, Vesak. Cross-references Cat 6. *No substantive outreach during observance windows.*
- **Known travel windows** [REF]
- **Known seasonal residence patterns** [REF]
- **Last touch and next scheduled touch** [DD]. *If next touch slips past prospect's stated comfort window, relationship cools without notice. The Prospect File prompts touches at prospect's natural rhythm.*

---

## LAYER 2 — DECISION LOG

Per prospect, dated chronological journal. Six entry types:

1. **Inference drawn** — what an observed signal implies about prospect's decision model, identity, or preferences. Triggered by meeting, public signal, third-party report.
2. **Move considered** — menu of outreach options evaluated. Options NOT taken get logged with rationale, so future bankers do not re-learn.
3. **Move taken** — what was executed. Channel, content, expected outcome.
4. **Outcome** — what happened. Signal the move produced. What worked, what did not, what to repeat or avoid.
5. **Question to surface** — open questions about prospect not yet answered. Next conversation attempts to surface these.
6. **Pattern match flag** — when banker recognizes prospect's signal set resembles an Existing Client; flags for Layer 3 pattern-map entry.

Each entry holds: date, type, trigger, content, Layer 1 cross-references (which fields informed or were updated), Layer 3 cross-references (which COIs or pattern matches involved), author.

**Worked example:** see `website/prospect_1.md` for the full Layer 2 decision log on Prospect 1.

---

## LAYER 3 — RELATIONAL GRAPH

Two sub-tables.

### COI Ledger

One record per Center of Influence the banker directly knows, used across many prospects within the banker's own book.

Per-COI fields:
- **Identity** [REF]. Name, role, firm type.
- **Relationship origin** [REF]. How known, year met, foundation strength.
- **Relationship temperature** [DD]. Cold, warm, hot. *If cold or unevenly returned, do not request intro yet; build first.*
- **Last touch and next scheduled touch** [DD]. *If next touch slips past COI's natural rhythm, relationship cools.*
- **Touch cadence** [DD]. *Match cadence COI prefers, not banker's preference.*
- **Past introductions made** [DD]. Each intro: prospect/Existing Client, date, outcome. *Track conversion per COI; some intro frequently with low conversion, others rarely intro with high conversion.*
- **What COI needs from banker in return** [DD]. Specialist intros, content, co-marketing presence, named-CE speaking slots, social inclusion, mutual referrals, no direct asks. *First material intro request should follow at least one delivered value.*
- **Reciprocity ledger** [DD]. What banker has given; what received. *If imbalance favors banker, slow asks; if favors COI, accelerate delivery before next ask.*
- **Style notes** [REF]
- **Mutual professional connections** [REF]
- **Sensitive context (volunteered)** [REF]. Same discretion discipline as Cat 13.

**Worked example for COI 4:**
Outside counsel, Bay Area corporate law firm, senior partner, M&A + emerging-company. Met 2022 at small-format M&A panel; medium foundation. Warm temperature; responds within 24 hours; accepted three quarterly breakfasts; one prior intro converted (Existing Client 3, mandate within 8 months). Quarterly 90-minute breakfast cadence + ad hoc on deals. Past intros: Prospect 1 (active), Existing Client 3 (mandate). Needs: specialist intros for clients with international tax exposure, content on private-company governance; declines social-only meetings. Reciprocity: banker has delivered 2 specialist intros + 1 quarterly content piece on QSBS stacking; received 1 client mandate + 1 active prospect intro. Style: brief in writing, expansive in person; will not refer to advisors who pitch products in initial meetings; declines breakfast before 8am. Mutual: COI 7 (estate counsel), COI 12 (M&A banker, boutique). Sensitive: mentioned in 2024 that one founder client is in active M&A; banker has not surfaced or referenced.

### Pattern Map

Per prospect. Flags 1-3 Existing Clients whose signal set this prospect resembles. Pattern matches are drawn only from the banker's own directly-served clients; client information protected by firm confidentiality policy and regulatory privacy frameworks stays within the trust boundary that earned it. The Pattern Map reflects the banker's own book, not a firm-wide client database.

- **Pattern match #1** [DD]. Existing Client. Match type. What worked. What failed. What to carry forward. What to avoid.
- **Pattern match #2** [DD]. Same structure if exists.
- **Anti-pattern** [DD]. Existing Client whose situation looked similar but played out differently. What looked like a match but wasn't. Why the move that worked there will not work here.

**Worked example:** see `website/prospect_1.md` for the Pattern Map on Prospect 1.

---

## INFERENCE LAYER

The mental model for turning Layer 1 + Layer 2 + Layer 3 data into a specific outreach move. Without this layer, the Prospect File is a data dictionary; with it, the Prospect File is a decision engine.

### Five rules for reading the file

1. **Weight is uneven.** 1 or 2 signals carry disproportionate weight; the rest is context. Banker's first job is to identify the load-bearing signal, not to triangulate across 150 fields equally.
2. **Absence is signal.** Avoidance, silence, omission are data. Map what the prospect does not say. Solving for the avoided topic stumbles into the wound.
3. **Contradictions are diagnostic.** When Layer 1 fields contradict, the contradiction IS the planning conversation.
4. **The strongest opener routes through the heaviest signal.** Outreach built around second-heaviest signal is competent but generic — the template's failure mode.
5. **Pattern-match before drafting.** Every first-touch draft starts from Layer 3 (pattern map), not from a blank page. If no pattern match exists, file is a new archetype — flag, draft from first principles, be explicit about it.

### The three discovery answers

Three highest-yield early-meeting questions:
- "What is most important about this wealth to you?" (values-first opener)
- "If we were meeting three years from now, what would have to happen for this to feel successful?" (three-year question)
- "What has been your experience with prior advisors? How did you choose them? What did you learn?" (selection diagnostic)

Once all three are in Cat 12, outreach thesis is close to determined. Until all three captured, outreach is tentative; once captured, outreach is decisive.

### Worked example for Prospect 1
(See `website/prospect_1.md` for the full decision log plus the inference application: load-bearing signals are family weight and heritage identity; co-founder absence is structural; no contradictions; family is heaviest; Layer 3 points to Existing Client 1 play; outreach decision is warm intro through COI 4 to estate counsel COI 7 for 7am Stanford Dish run, opening on generational trust accommodating mother's long-term care.)

---

## EXISTING DELIVERABLE FILES

- **/Users/Mario/jpmproject/prospecting/ai-augmented-uhnw-prospecting.mdx** — v1 deliverable. Treat as scaffolding only. Reusable: opening narrative (~310 words, decent landscape-setting), some framing in strategic memo, extensibility sidebar, closing questions structure, Notes & Sources. NOT reusable: schema section (too tight), profiles (need full rewrite from scratch using new Layer 1+2+3 structure), AI subsections (compress massively).
- **/Users/Mario/jpmproject/prospecting/memory.md** — original pre-flight working memory (Verdi/JPM/Mario context).

---

## STRATEGIC MEMO REVISION NOTES (pending)

When we get to the memo:
- **Compress the AI sections** to one ~80-word paragraph at the end of the memo.
- **Fold in the load-bearing data point**: 67% of affluent prospects who hired an advisor already knew someone with that advisor (Oechsli). Justifies the Prospect File's emphasis on relational mapping as a first-class citizen.
- **Add a tight section on what the Prospect File actually solves**: ocean-boiling fails because templated outreach cannot adjust to the prospect's heaviest weighted P; relationship intelligence reframes top-of-funnel as fit-diagnosis first, capability demonstration second.
- **Keep the workflow paragraph short**: first encounter logs to the Prospect File within 24 hours; conversational signals verbatim; public signals refresh monthly via research-compression pass; every prospect carries a single-sentence outreach thesis.

---

## ACRONYMS AND TERMS

Glossary of acronyms and shorthand in use across the project. Add new terms here as they enter the working vocabulary.

### Wealth structures and tax instruments
- **DAF** — Donor-Advised Fund
- **GRAT** — Grantor Retained Annuity Trust
- **CRT** — Charitable Remainder Trust
- **CLT** — Charitable Lead Trust
- **ILIT** — Irrevocable Life Insurance Trust
- **IDGT** — Intentionally Defective Grantor Trust
- **GST** — Generation-Skipping Transfer (tax)
- **QDOT** — Qualified Domestic Trust (for non-US-citizen spouses)
- **QSBS** — Qualified Small Business Stock (IRC Section 1202 exclusion)
- **PPLI** — Private Placement Life Insurance
- **SBL** — Securities-Based Lending (line of credit collateralized by marketable securities)
- **LTC** — Long-Term Care (insurance)
- **AMT** — Alternative Minimum Tax
- **IRC** — Internal Revenue Code
- **10b5-1** — SEC Rule 10b5-1 trading plan (preset stock-sale schedule for insiders)
- **RSU** — Restricted Stock Unit
- **LLC** — Limited Liability Company
- **SCI** — Société Civile Immobilière (French civil real-estate holding company)
- **mandat à effet posthume** — French legal instrument for posthumous administration of a closely held interest (not an acronym; listed for cross-reference)

### International tax and cross-border
- **FBAR** — Foreign Bank Account Report
- **PFIC** — Passive Foreign Investment Company
- **CRS** — Common Reporting Standard (OECD financial-account info exchange)
- **OCI** — Overseas Citizen of India (lifelong India visa for diaspora)

### Wealth tiers and family generations
- **HNW** — High-Net-Worth (industry shorthand: $1M+ investable assets)
- **UHNW** — Ultra-High-Net-Worth (industry shorthand: $30M+ net worth)
- **G1, G2, G3** — first-, second-, third-generation wealth holder (G1 = creator, G2 = inheritor, G3 = grandchildren cohort)

### Roles and credentials
- **COI** — Center of Influence (referral source: outside counsel, CPA, accountant, board member, school development officer, etc.)
- **EA** — Executive Assistant
- **CFA** — Chartered Financial Analyst
- **CPA** — Certified Public Accountant
- **CFP** — Certified Financial Planner
- **JD** — Juris Doctor
- **PM** — Product Manager
- **VP** — Vice President
- **CEO** — Chief Executive Officer
- **EIR** — Entrepreneur in Residence (typical role at venture firms)

### Education
- **BS** — Bachelor of Science
- **CS** — Computer Science
- **MBA** — Master of Business Administration
- **MPP** — Master of Public Policy
- **HKS** — Harvard Kennedy School
- **GSD** — Harvard Graduate School of Design
- **HEC** — HEC Paris (École des Hautes Études Commerciales)
- **ESCP** — École Supérieure de Commerce de Paris
- **K** — Kindergarten (used in "K-college" / "K through grad" education-stage references)

### Firm types, entities, and finance shorthand
- **MFO** — Multi-Family Office
- **SFO** — Single-Family Office
- **YPO** — Young Presidents' Organization (peer network of operators / CEOs)
- **M&A** — Mergers and Acquisitions
- **IPO** — Initial Public Offering
- **PE** — Private Equity
- **IR** — Investor Relations
- **SaaS** — Software as a Service

### SEC filings (used in provenance context)
- **Form 4** — insider trading disclosure (officer/director equity activity)
- **S-1** — IPO registration statement
- **10-K** — annual report
- **990** — IRS annual filing for non-profit organizations and private foundations

### Geographic shorthand
- **SF** — San Francisco
- **PNW** — Pacific Northwest
- **CA / NY / etc.** — US state codes (standard usage)

### Project-internal codes (Layer 1, provenance, methodology)
- **The Client Book** — case-study title only (the project's brand and the title under which it publishes). NOT used in body text to refer to the structured-memory system; that is the Prospect File.
- **Prospect File** — the structured-memory system per relationship. Each prospect (and each existing client we cross-reference) has one Prospect File; the file persists across stages of the relationship. Replaces "the Book" in body text. Distinct from "book of business," which refers to the firm's existing-client roster.
- **Pipeline** — the system-level view across all Prospect Files. Each file sits at a stage in the pipeline: qualification, first-touch, multi-meeting depth, existing-client. The same Prospect File travels with each relationship across stages.
- **Cat 1–14** — Layer 1 schema categories: (1) Core identity / residences; (2) Family, multi-generational; (3) Education; (4) Wealth story; (5) Professional history / boards; (6) Cultural origin / orientation; (7) Food, beverage, dietary; (8) Sports, fitness, hobbies, travel; (9) Personality and communication; (10) Philanthropy; (11) Network, memberships, COIs; (12) Conversational signals and behavioral notes; (13) Sensitive (volunteered only); (14) Trigger events and timing markers
- **DD** — Decision-Driving field (Layer 1 schema tag; field carries explicit if/then logic for outreach decisions)
- **REF** — Reference field (Layer 1 schema tag; supports other fields, no direct decision rule)
- **M1, M2, M3...** — Numbered meeting (with date in the provenance ledger)
- **E** — Email or written exchange between meetings (provenance code)
- **Sp** — Volunteered by spouse during a joint meeting (provenance code)
- **Obs** — Behavioral observation during a meeting (pacing, name usage, body language; provenance code)
- **Inf** — Inferred from cross-reference of multiple signals (provenance code)
- **RTQ** — Risk Tolerance Questionnaire (industry-standard advisor intake form; Cat 12 distinguishes risk posture in own words from any RTQ score)
- **Five Ps** — People, Philosophy, Process, Performance, Fees (Beyer's five evaluation criteria UHNW prospects rank-order when comparing advisors)

### External works and outlets (in Notes & Sources)
- **FA-Mag** — Financial Advisor Magazine
- **FAS** — Financial Advisor Success (Michael Kitces podcast)
- **CEG** — CEG Worldwide (advisor coaching firm; John Bowen)
- **CCH** — Commerce Clearing House (publisher of Kochis's *Wealth Management*)
- **CFA Institute** — Chartered Financial Analyst professional body (publisher of Beyer's "Relationship Alpha" brief)

---

## NOTES & SOURCES (consolidated, for the deliverable)

Practitioner mental-model layer:
1. Charlotte Beyer, *Wealth Management Unwrapped* (Wiley, rev. 2017). Five Ps framework; rank-ordering as diagnostic.
2. Charlotte Beyer, "Relationship Alpha," CFA Institute Research Foundation Brief, 2019. Relationship alpha vs. investment alpha.
3. Charlotte Beyer interview on Kitces Financial Advisor Success podcast. Prior-advisor history as the highest-yield first-meeting diagnostic question.
4. James Grubman, *Strangers in Paradise* (2013). Immigrants-to-wealth model; denial / assimilation / integration.
5. Jaffe & Grubman, *Cross Cultures* (2016). Three-culture model: Individualist, Collective Harmony, Honor.
6. Dennis Jaffe, *Borrowed from Your Grandchildren* (Wiley, 2020). Generative families; non-financial wealth by G2.
7. Tim Kochis, *Managing Concentrated Stock Wealth* (Bloomberg, 2015). Pre-event tax-alpha window.
8. Tim Kochis, *Wealth Management* (CCH, 2nd ed.). Goals-first, products-last.
9. Thayer Willis, *Navigating the Dark Side of Wealth*. Inheritor identity diagnostic; third-person wealth language.
10. Kitces FAS #474, Blair duQuesnay on UHNW service. UHNW fear is catastrophic mistake, not running out of money.

Operational craft layer:
11. Russ Alan Prince & Brett Van Bortel, *Ultimate Rainmaker* (2024 ed.). COI methodology.
12. Russ Alan Prince et al., *Optimizing the Financial Lives of Clients* (2023). How CPAs decide to refer.
13. Russ Alan Prince, "The Whole Client Model," Financial Advisor Magazine. Seven-category profiling.
14. Dan Allison on Kitces FAS #447. Highest-signal operational source on COI work; referral-risk opener; client-feedback loop; quarterly mutual-education meeting; capacity-signaling.
15. John Bowen (CEG Worldwide) on Kitces. Five values-first questions; advisor as general manager not quarterback; 84% want emotional connection first.
16. Matt Oechsli, "Anatomy of an Effective LinkedIn Prospecting Message"; "Generate Referrals with This Simple Phrase"; "Factor of Six Rule"; "The #1 Reason Affluent Prospects Select Their Advisor." 67% of affluent hires know someone with the advisor; Advocate Search script; volatility-triggered intro line.
17. WealthManagement.com, "Courting Centers of Influence." Six named-advisor case studies.
18. Carl Richards / Kitces, "When the Big Prospect Doesn't Want Your Financial Plan." Method-vs-goal separation; Sullivan's three-year question.
19. Rob Knapp, *The Supernova Advisor*. 12-4-2 service model.
20. David J. Mullen Jr., *The Million-Dollar Financial Advisor*. Niche marketing; daily prospecting discipline.
21. Francis Financial via FA-Mag. Free-second-opinion intake.

AI tooling positions (for the compressed AI paragraph):
22. Morgan Stanley press release, "AI @ Morgan Stanley Debrief." ~30 min saved per client interaction; AI generates prompts for advisor, not messages to client.
23. Goldman Sachs Insights, AI page. Position that AI empowers advisor with contextual cues; client-facing generative AI held back until accuracy/compliance thresholds met.
24. Rockefeller Capital Management leadership public framing on hybrid AI-plus-advisor.

Bay Area UHNW grounding:
25. Altrata, *The Wealthy in San Francisco 2023*. ~4,380 UHNW; 84 billionaires; 7th-highest global UHNW density.
26. Joint Venture Silicon Valley / Kauffman, summarized 2025. ~66% foreign-born tech workforce; ~45% of Bay Area tech startups have ≥1 foreign-born founder.
27. Cerulli Associates. ~$84T US wealth transfer through 2045.
28. Knight Frank, *The Wealth Report 2025*.
29. Altrata, *World Ultra Wealth Report 2024/2025*.
