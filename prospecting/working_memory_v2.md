# Client Book Project — Working Memory v2

Comprehensive working memory of locked substance for the UHNW prospecting case study. Use this file to resume work across sessions. Supersedes memory.md (which captured pre-flight context only).

---

## STATUS

We are in the **substance-locking phase** before drafting the final deliverable.

**Locked:**
- Frame (bespoke Client Book; AI-augmented in build but not body headline; not a JPM playbook)
- Naming convention (Prospect 1/2/3; Existing Client 1/2/etc; COI 1/2/etc)
- Three-layer Book architecture (Profile / Decision Log / Relational Graph)
- 14-category Layer 1 schema with ~150 fields and if/thens
- Layer 2 Decision Log structure (6 entry types) with worked example
- Layer 3 Relational Graph (COI Ledger + Pattern Map) with worked example
- Inference Layer (5 rules + 3 discovery answers) with worked example
- Prospect 1 fully populated
- Prospect 2 fully populated (drafted, pending user revision notes)
- Prospect 3 fully populated (drafted, pending user revision notes)

**Pending, in order:**
1. Incorporate user revision notes on Prospects 2 and 3
2. Strategic memo light revision (compress AI subsections, fold in 67%-of-affluent-prospects-knew-someone data point, keep tight)
3. Opening narrative light revision (probably survives mostly intact)
4. Closing questions light revision
5. Extensibility sidebar (probably survives)
6. Project card entry (revise to lead with banker craft, not toolchain)
7. Notes & Sources expansion (add Prince, Allison, Oechsli, Bowen, Mullen, Knapp, WealthManagement.com, Beyer Kitces ep, Willis, Cerulli)
8. Full fresh draft of deliverable (treat existing v1 mdx as scaffolding only, ~30–40% reusable)
9. Site integration (locate Next.js repo, reconcile frontmatter, drop into content/projects/)
10. Vercel deployment

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

1. **The piece is a Client Book case study, NOT a JPM prospecting curriculum.** Every research finding from the operational craft pass (Prince/Allison/Oechsli/Bowen/etc.) lands as "this is what the Book captures" or "this is the decision the Book drives," NOT as top-down methodology.

2. **AI is the build substrate (in title), not the body's headline.** "AI-Augmented" stays in the title because it honestly describes how the playbook was built. The strategic memo compresses AI to one ~80-word paragraph at the end. Banker craft is the body's center of gravity.

3. **Length constraint relaxed.** The deliverable will render as discrete sections on the Vercel site, not as one long document. Don't over-optimize for word count; optimize for content correctness.

4. **Naming convention.** Prospect 1, Prospect 2, Prospect 3. Existing Client 1, Existing Client 2, etc. COI 1, COI 2, etc. No fictional names.

5. **Sensitive information held with discipline.** Sensitive fields (Cat 13) are empty by default and never extrapolated. Entry only when the prospect themselves volunteers the fact. The piece says this out loud as a discipline.

6. **The deliverable comes LAST.** Substance first (schema, profiles, inference layer), then framing revisions, then a fresh draft. The existing v1 mdx is scaffolding only.

---

## ARCHITECTURE: THREE LAYERS

**Layer 1: Profile** — static facts per prospect. 14 categories, ~150 fields. What the prospect IS.

**Layer 2: Decision Log** — running journal per prospect. Dated entries of inferences, moves considered, moves taken, outcomes. What the BANKER has thought and done.

**Layer 3: Relational Graph** — COI Ledger (one record per intro source, used across many prospects) + Pattern Map (per prospect, links to Existing Clients with similar signal sets). The connective tissue.

A prospect file pulls from all three layers. The COI ledger is shared across prospects. Pattern-match references cross-link to handled clients.

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
- **Stated criteria for engaging a new or additional advisor** [DD]. *Most prospects do not voice this directly but signal it across meetings. Book records inferred criteria; next material proposal addresses them explicitly.*

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
- **Past legal or regulatory matters as volunteered** [REF/DD]. *Material when bearing on fiduciary planning. Book holds the fact; planning conversation respects without surfacing.*
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
- **Last touch and next scheduled touch** [DD]. *If next touch slips past prospect's stated comfort window, relationship cools without notice. Book prompts touches at prospect's natural rhythm.*

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

**Worked example for Prospect 1:**

- *2025-03-12. Inference drawn.* Trigger: first meeting (intro via COI 4). Mentioned mother twice unprompted; co-founder zero times; named high school in country of origin before naming Berkeley. Inference: family weight exceeds founder weight; co-founder omission reads as wound, not oversight; identity is heritage-first. Updates Cat 12 and Cat 6.
- *2025-03-14. Move considered.* Three options: (a) email memo on lockup tax sequencing — rejected, leads with founder identity; (b) dinner via mutual school parent — rejected, declines unknown-group dinners (Cat 9); (c) warm intro request to estate counsel for generational-trust conversation including mother's long-term care — selected, routes through heaviest signal.
- *2025-03-15. Move taken.* Requested warm intro from COI 4 to specialty estate counsel COI 7 for 7am Stanford Dish run with prospect. Opening framing: structural question about generational trust accommodating mother's long-term care, not a pitch.
- *2025-04-02. Outcome.* Run accepted. Conversation routed through father's retirement (volunteered by prospect within first ten minutes). Founder biography never raised. Prospect requested follow-up with spouse present; volunteered that spouse's parents also live in market without long-term-care planning. Updates Cat 2 and Cat 14.
- *2025-04-02. Question to surface.* Spouse's financial agency. Spouse's view on long-term-care timing. Whether brother-in-law involved in in-laws' planning. To surface in next meeting if naturally arising.
- *2025-04-02. Pattern match flag.* Prospect 1's signal set matches Existing Client 1. Update Layer 3 pattern map.

---

## LAYER 3 — RELATIONAL GRAPH

Two sub-tables.

### COI Ledger

One record per Center of Influence, used across many prospects.

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

Per prospect. Flags 1-3 Existing Clients whose signal set this prospect resembles.

- **Pattern match #1** [DD]. Existing Client. Match type. What worked. What failed. What to carry forward. What to avoid.
- **Pattern match #2** [DD]. Same structure if exists.
- **Anti-pattern** [DD]. Existing Client whose situation looked similar but played out differently. What looked like a match but wasn't. Why the move that worked there will not work here.

**Worked example for Prospect 1:**
- *Match #1.* Existing Client 1. Match: post-acquisition founder, family-first identity, observant household, declined dinners (3 of 3 early), mentioned mother before company in first three meetings. Worked: morning-run venue picked by intro source; opening question about father's estate; six-month gap before any product mention; spouse included in second meeting at her invitation. Failed: early wine-dinner proposal; late sector-conference invitation. Carry forward: route first material outreach through estate counsel; let second meeting be requested by prospect; never mention co-founder by name. Avoid: speed; framing founder identity as primary.
- *Match #2.* None close enough at this stage.
- *Anti-pattern.* Existing Client 5. Surface match (post-acquisition Bay Area founder, observant household) but G2 inheritor of operating company, not self-built founder. Family-first frame already saturated by existing multi-generational family office. Lesson: family-first identity is not enough; verify whether sits on Built or Inherited wealth before applying play.

---

## INFERENCE LAYER

The mental model for turning Layer 1 + Layer 2 + Layer 3 data into a specific outreach move. Without this layer, the Book is a data dictionary; with it, the Book is a decision engine.

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
(See Layer 2 decision log above plus the inference application: load-bearing signals are family weight and heritage identity; co-founder absence is structural; no contradictions; family is heaviest; Layer 3 points to Existing Client 1 play; outreach decision is warm intro through COI 4 to estate counsel COI 7 for 7am Stanford Dish run, opening on generational trust accommodating mother's long-term care.)

---

## PROSPECT 1 — fully populated

### Relationship stage
Post-second-meeting. Two seated conversations complete: first meeting 2025-03-12 (intro via COI 4) and 2025-04-02 Stanford Dish run with estate counsel COI 7. Third meeting scheduled 2025-05-05 as breakfast with spouse Priya present, at the prospect's own invitation; spouse inclusion at prospect-initiated scheduling is the key progression marker.

### Archetype
Exited tech founder, mid-career, post-acquisition.

### Layer 1 highlights
- 43, US citizen (naturalized 2005) + India OCI; languages English/Hindi/limited Marathi.
- Hindu, moderately observant; Diwali and Holi as family events.
- Menlo Park primary residence (joint tenancy, personal name); no secondary; CA tax domicile.
- First marriage 2012, no prenup. Spouse Priya, 41, 2nd-gen Indian-American, MBA, former product lead, full-time parent; joint financial agency, passive on investments.
- Two sons, 12 and 9, Mandarin-immersion school in Palo Alto.
- Parents (retired physicians) in Cupertino since 2019 (after father's cardiac event); modest monthly support from prospect.
- One sister in London (independent).
- Berkeley CS 2004; private Indian boarding high school in Pune.
- G1 wealth creator. Single founder of vertical SaaS company 2014–2025; sold to publicly traded acquirer Jan 2025; $180M cash-and-stock, 40% rolled into acquirer stock under 24-month lockup (releases Sept 2026 + Mar 2027).
- ~60/40 liquid/illiquid; 35% concentration in lockup stock.
- Existing structures: revocable living trust 2018; NO dynasty/GRAT/CRT/DAF/foundation. QSBS claimed for own shares but NOT stacked across spouse or trusts (gap). Single wirehouse advisor since 2020 + single firm-based CPA. $10M term life; no PPLI/LTC. NO SBL line (opportunity).
- Career arc: "I built one thing." Two private boards (early-stage portfolio companies). YPO joined 2024. One long-form essay on operator mental health (2024).
- First-gen immigrant from Maharashtra (came 2000 for college). Travels India once yearly February for ~2 weeks.
- Vegetarian (Hindu); has suggested Ettan in Palo Alto twice; light Burgundy occasionally; tea drinker.
- Runs 5–6x/week, Stanford Dish or Rinconada. Follows IPL cricket. Hikes with kids. Tahoe ski weekends. Goa summer 2023.
- Reserved, analytical, skeptical, detail-oriented, deliberative. Dry humor at second meeting. Email primary; 24–48h response; direct calendar; prefers 6:30–9:30am; 60 min standard. Five Ps inferred: People > Philosophy > Process > Fees > Performance. Media: Economist, Stratechery, NYT.
- Causes: Berkeley CS (modest), children's school, Bay Area mental-health crisis hotline since 2022. DAF at wirehouse 2020; ~$250K/yr; Priya co-advises.
- Olympic Club 2023 (rare use). Active in Pune high school WhatsApp group. Prior advisor relationship maintained but stated dissatisfaction. Multi-meeting decision style; requires spouse approval.
- Volunteers mother's care, father's cardiac event, sons' Indian-American identity, sister's career. Avoids prior advisor's name. Returns to parents' late-life transition. Names: mother as "Mom," father as "Dad," sister by first name. Slow methodical pacing. Boundary: "I want one person I trust." Field Notes notebook. 10-year-to-generational time horizon. Risk posture: "conservative, because I got lucky once and I don't want to be lucky twice." Discovery captured: values (family continuity); three-year question NOT yet surfaced; prior-advisor diagnostic ("fine but never proactive").
- Sensitive: light ADD mention. Father's cardiac event 2019 (2 stents); mother's breast cancer remission 2015. Therapy normalized. Planning fear: "I don't want my parents to need something I haven't thought of." Regret: wishes had set up trust for parents pre-exit. Priya healthcare proxy; no living will (gap).
- Trigger events: lockup tranche 1 release Sept 2026; tranche 2 Mar 2027; father's 75th birthday Jan 2026; 13-year wedding anniversary Sept 2025. DOB 1982-06-04. Recent transitions: parents' move (2019), father's cardiac event (2019), exit (Jan 2025). Liturgical: Diwali (Nov), Holi (Mar). Travel: India 2 weeks Feb. Last touch 2025-04-02; next 2025-05-05 (breakfast w/ spouse, requested by prospect).

### Outreach play
- **Channel.** Warm intro via COI 4 (former outside counsel on the acquisition; intro to banker via M&A panel 2022; warm temperature).
- **Who introduces.** COI 4 by email with one-sentence context paragraph banker drafts.
- **Opening angle.** Structural memo on how Sept 2026 lockup release interacts with a generational trust accommodating mother's long-term care. Routes through heaviest signal (family) and addresses voiced planning fear.
- **Timing.** Early Q3 2025, ~6 months pre-lockup. Avoids Diwali (Nov) and India trip (Feb 2026).
- **Second-meeting artifact.** Two-page structure memo with QSBS stacking gap surfaced (diagnostic, not pitched) and trust architecture covering parents, spouse, sons.
- **Non-obvious signal that drove decision.** Heritage biography and mother's care lead every meeting. Routing through parents' estate, not exit proceeds, is the only opener that survives Rule 4.

---

## PROSPECT 2 — fully populated

### Relationship stage
Post-second-meeting. First meeting 2025-02-18 (intro via COI 9 at the French-American school finance committee room) and second meeting 2025-03-20 at her selected Sand Hill Road cafe. The second meeting produced a revision request on the English-side pre-read ("tighter, same substance"), a volunteered seven-figure tax-friction regret from the 2023 secondary sale, and a request for a third meeting with spouse Tarek present. No third meeting scheduled; target window is post-Orthodox-Easter 2026, pre-summer-travel (late April through early June 2026).

### Archetype
Foreign-born first-gen operator, mid-career, post-secondary-sale, with a multi-jurisdictional family-business lineage in parallel to her built US exit.

### Layer 1 highlights

**Cat 1 — Core identity and residences.** Prospect 2 is 51, born Paris to Lebanese parents who fled civil-war-era Beirut in the late 1970s. French citizen by birth, naturalized US citizen in 2018; both passports active and used within the last twelve months. Primary residence Atherton (2019 purchase, personal name, joint tenancy with spouse). Secondary residence Paris 7th arrondissement (family-owned since 1982, held through a French SCI). Ancestral stone house in Byblos inherited through the paternal line. California tax domicile since 2019 with clean substantiation (driver's license, voter registration, primary physician all in CA); the Paris property routes through the SCI for French wealth-tax and succession purposes. Written outreach uses the French form of her given name; a legal-form salutation will read as database-pulled. Chief of staff (one-year tenure) controls the calendar and email triage end-to-end and is a first-class relationship in her own right.

**Cat 2 — Family, multi-generational.** Married fifteen years to Tarek, 54, French-Lebanese architect running a small Bay Area residential practice. Joint financial agency, with Tarek carrying emotional weight on family-continuity decisions and Prospect 2 leading on structural ones. Three children: eldest at Sciences Po Paris (19, gap year before final cycle), middle and youngest (17 and 14) at the French-American school in Menlo Park. Mother (76) splits her year between the Paris apartment and Byblos and co-runs the family jewelry business from a Place Vendôme-adjacent atelier with the older sister (53, Paris-based, day-to-day operator). Younger sister (47) in Dubai, financially independent. Father died 2013; his post-war Lebanese civic involvement is a topic Prospect 2 sidesteps. No prenup on the current marriage; both spouses entered the marriage with inherited European property. Children's schooling anchors the household to French school-year rhythm.

**Cat 3 — Education, across generations.** Prospect 2: Lycée Janson de Sailly (Paris, 1993), HEC Paris bachelor-master (1999), Harvard Kennedy MPP (2002). Spouse: Ecole des Beaux-Arts and a Harvard GSD master's. Older sister: ESCP Paris. HEC and HKS alumni networks are active and well-stewarded; she attends the HEC SF alumni chapter dinner at least annually. Eldest child's Sciences Po cohort and the French-American school development office are both viable warm-intro surfaces. Giving history to HKS is modest but steady; HEC participation is social, not financial.

**Cat 4 — Wealth story.** Co-founded a fintech infrastructure company in 2011 (cross-border B2B payments rails). Held 22% at the 2023 secondary sale, when a growth-stage private equity buyer took a majority stake: ~$95M cash out plus ~$40M rolled into the acquirer's continuation vehicle with a three-year lock and a ratchet. Concurrent inheritance of a one-third economic interest in the Paris-based family jewelry business (closely held European private company, minority stake governed by a French-law shareholder agreement). Net worth tier $150–200M liquid plus the European minority. Liquid/illiquid split roughly 55/45. Single-position concentration in the acquirer rollover sits at 21% of liquid; tolerable, not urgent. Existing structures: a French notarial will and a *mandat à effet posthume* governing the jewelry stake; a US revocable living trust from 2020; no dynasty trust, no GRAT, no CRT, no DAF, no foundation in her own name. QSBS is not a gap because the 2011 vehicle was not C-corp. Multi-advisor structure: US wirehouse managing the 2023 proceeds, a French private bank on Paris-side assets, two tax advisors (one each side), and a Paris notary for European succession. No quarterback across the four. No SBL line; $3M mortgage on Atherton at 2.9% fixed. Current income streams: two private-company board fees plus continuation-vehicle distributions, not operating salary.

**Cat 5 — Professional history and boards.** Pre-founding: four years in corporate strategy at a European bank (Paris and New York), then two years at a US venture firm as EIR before spinning out the 2011 company. Post-exit she sits on two private-company boards (both acquirer portfolio companies) and on the board of the family jewelry business in Paris (formal seat since 2017). One non-profit board: a binational French-American cultural foundation chaired from San Francisco. Career narrative in her own words: "I was raised in two family businesses. Fintech was the first one I built myself; the second is older than I am." Publishes occasional op-eds in a Paris business weekly on cross-border payments regulation and speaks at one European fintech conference annually. No LinkedIn activity; the op-ed byline is her operative public surface. Fellow directors on the cultural foundation and the family-business board are the highest-yield warm-intro routes.

**Cat 6 — Cultural origin and orientation.** First-generation immigrant to the US from a first-generation immigrant French family; fully second-generation in France. Identifies as Lebanese first, French second, Californian third. Trilingual: French is the working and family language; Arabic is the language of emotional content and of how she addresses her mother; English is for structured negotiation and written memos. Greek Orthodox by paternal lineage, observes Easter and Christmas on the Julian calendar (Orthodox Easter falls April or May; Christmas January 7). Loose acknowledgment of Ramadan through maternal cousins, not personally observant. She traveled to Byblos every summer of her life except 2020; the 2020 Beirut port explosion damaged the family atelier in old Beirut and is a loaded topic she raises unprompted. Family decision-making reads Collective Harmony: nothing commits until mother and older sister have weighed in, even where she holds formal control.

**Cat 7 — Food, beverage, dietary.** No dietary restrictions. Pescatarian Wednesdays (Greek Orthodox fast-day observance that survives even when the rest of the calendar drifts). Selected a specific Sand Hill Road cafe for two of the first three meetings; treat as her venue of record until she selects another. Cuisine preferences: Levantine home cooking (she references her mother's kibbe nayeh repeatedly), French bistro, Japanese at the kaiseki level. Wine: light Burgundy and Lebanese reds from the Bekaa; twice referenced a specific Lebanese producer by name. Tea drinker by 11am; espresso before 10am. Social drinker, not oenophile; one glass, never two. Declines cocktail-hour venues in favor of lunch or midmorning coffee.

**Cat 8 — Sports, fitness, hobbies, travel.** Daily swimmer at a masters pool near home, 6:15am. Does not run. Plays weekly doubles tennis at Menlo Country Club level with Tarek in season. No season tickets to any US team; follows Paris Saint-Germain loosely. Hobbies: mid-century French design, an inherited collection of Ottoman-era silver jewelry pieces from the family workshop, a modest photography habit focused on Mediterranean coastal architecture. Travel rhythm: Paris and Byblos each summer (mid-June through late August), Paris at Orthodox Christmas (around January 7), Paris at Orthodox Easter. One or two US domestic trips per year, rarely to New York. No private aviation; flies commercial first class. Cultural consumption: Paris Opera season tickets, San Francisco Symphony subscriber.

**Cat 9 — Personality and communication.** Reserved and analytical. High skepticism of American advisor-pitch culture; she reads firm-branded conference rooms as hostile terrain and has walked out of one. Detail-oriented and deliberative; expects materials 24 hours in advance and returns them marked up. Decisive only after at least two seated meetings and a written memo in hand. Preferred channel: email first, phone second; never text. Response-time norm is two to four business days. Calendar is gatekept tightly by the chief of staff. Prefers late-morning meetings (10–11:30am), 75 to 90 minutes, at her selected cafe or the cultural foundation's office; never at the advisor's office, never at her home. Five Ps rank ordering: Philosophy > People > Process > Fees > Performance. Performance-lead pitches slide off her. Media diet: Les Echos, the Financial Times, one Lebanese-diaspora Substack, and the family-business weekly that runs her op-eds.

**Cat 10 — Philanthropy.** No DAF, no private foundation in her own name (the family jewelry business runs a small European operating foundation in which she holds a director seat). US giving is direct-check, modest ($50–150K annually), to two institutions: the binational French-American cultural foundation she chairs, and an organization funding heritage-craft apprenticeships in Lebanon stood up after the 2020 explosion. Chairing the cultural foundation makes that board's other directors high-yield COIs; most are practicing principals in Bay Area design, finance, and law. The post-explosion Lebanon giving is tied to identity work, not portfolio work; substantive content on heritage-craft continuity will land where a structured-giving pitch will not.

**Cat 11 — Network, memberships, centers of influence.** No Bay Area city-club membership (declined Olympic Club and Pacific Union; treats US city clubs as performative). Holds an inherited membership at Cercle de l'Union Interalliée in Paris, rarely used. Close friends referenced by first name across meetings: two HEC classmates based in Paris (not in-market), one architect spouse-circle friend in Menlo Park, and one Bay Area fintech co-founder (her only US-based peer-network anchor). Chief of staff controls introduction routing; a request that bypasses the chief of staff closes the door. Active intro-source candidates: COI 9 (school finance committee chair at the French-American school, fellow committee member for two years, warm), COI 12 (fellow director on the cultural foundation, senior Bay Area design principal, warm), COI 14 (Paris estate counsel who served the family jewelry business in a 2019 succession planning cycle, warm but Paris-based, used asymmetrically). Two prior US advisors over nine years; neither terminated on fee or performance. Both relationships lapsed on what she describes as "they stopped knowing what was going on at home." First material proposal must address the cross-border coordination gap head-on.

**Cat 12 — Conversational signals and behavioral notes.** Topics volunteered unprompted: the family jewelry business (she calls it "the project" in Arabic when speaking to her mother and occasionally lets the Arabic slip in English), the 2020 Beirut explosion and its effect on the atelier, the middle child's academic difficulty switching between English and French, and her mother's insistence on remaining in Byblos through summer regardless of security conditions. Topics avoided: her father's post-war political involvement (referred to obliquely, never directly), US equity-market performance (treated as other people's conversation), and any framing that centers her fintech exit as her primary achievement. Topics returned to repeatedly: cross-border succession of the jewelry business, the middle child's schooling path, and the risk of the Paris apartment aging out of family use across the next generation. Names: mother by a French-Arabic hybrid term in private, older sister by first name, younger sister by first name, late father never named. Pacing: slow, measured, often 10 to 15 seconds of reflective silence before answering a planning question. Boundary voiced: "I do not take phone calls during the children's school pickup." Discovery answers captured so far: values question ("continuity of the family's name and craft; the money is instrumental"), three-year question ("the jewelry business and the Atherton household function without my daily attention; both children in US high school settled in their bilingual identity"), prior-advisor diagnostic ("they were capable but isolated from each other"). First-vs-third-person wealth language: mostly first person on the fintech proceeds ("what I built"), consistently third person on the jewelry stake ("the family interest," "the project"). Risk posture in her own words: "we preserve, we don't gamble."

**Cat 13 — Sensitive information (volunteered only).** Volunteered: mother's increasing difficulty traveling between Paris and Byblos after a minor fall in 2024; a named fear that the jewelry business succession will fracture family relationships if not handled with the older sister's full participation; a regret that she did not formalize a US-France tax coordination framework pre-secondary-sale (she estimates seven figures of avoidable US-side tax friction). Not volunteered and therefore empty: political views, health status, any reference to her father's cause of death beyond the year. No family rift disclosed. Discretion discipline: the Beirut explosion reference is the closest the Book gets to trauma-adjacent material; she raised it unprompted in the first meeting and will return to it on her own terms. The Book holds it without surfacing it.

**Cat 14 — Trigger events and timing markers.** Forward triggers: continuation-vehicle lock-release September 2026 (primary US-side liquidity event); mother's 80th birthday November 2028 (load-bearing family-calendar marker, referenced as the horizon for the jewelry succession plan); eldest child's Sciences Po final-cycle decision spring 2026 with a possible US law school application the year after; middle child's French-American school graduation June 2027, open US-or-France university path. Personal milestones: her own birthday April 14, mother's November 2, wedding anniversary July 19. Recent transitions in the last 24 months: secondary sale close (October 2023); naturalization five-year anniversary (October 2023, which triggered a US estate-tax rule update conversation that went unaddressed); youngest child's start at the French-American school upper division (September 2024). Liturgical windows to avoid: Orthodox Easter week (variable April-May), Orthodox Christmas (January 7 ± three days), Ramadan (loose, confirm rather than presume). Travel: Paris-Byblos mid-June through late August, Paris around January 7, Paris around Orthodox Easter. Last touch 2025-03-20 (coffee at her selected cafe, intro via COI 9). Next scheduled touch open; the window of interest is post-Orthodox-Easter 2026, pre-summer-travel.

### Layer 2 — Decision log excerpt

- *2025-02-18. Inference drawn.* Trigger: first meeting (intro via COI 9, at the French-American school finance committee room). Prospect 2 switched into Arabic twice when referencing her mother and the jewelry business; reverted to English only when the topic moved to the 2023 secondary sale. She never used English when describing "the project." Inference: the family business is the identity-load-bearing fact and the fintech exit is the instrumental one; any opener routed through the US exit will reach her second-heaviest signal. Updates Cat 6 and Cat 12.
- *2025-02-19. Move considered.* Three options: (a) structural memo on the continuation-vehicle lock expiration in September 2026 paired with US trust architecture, rejected for leading with the instrumental axis; (b) a multi-advisor coordination pitch with the four named firms around the table, rejected because she reads advisor-coordination pitches as encroachment; (c) a narrow cross-border continuity frame pegged to her mother's 80th birthday (November 2028) as the family-internal deadline for succession of the Paris jewelry stake, selected because it routes through the heaviest signal and matches her Philosophy-dominant Five Ps rank.
- *2025-02-22. Move taken.* Requested intro-continuation from COI 9 for a second meeting at Prospect 2's selected cafe. Pre-read: a one-page framing note (French on one side, English on the other) on how a US-France-Lebanon succession frame could anchor the jewelry stake transition across a 36-month horizon, with no firm named. Opening question: "If the 2028 birthday is the family-internal deadline, what would need to be true by summer 2026 for you to feel the architecture is in place?"
- *2025-03-20. Outcome.* Second meeting held. She kept the French-side pre-read and asked for the English side to be revised (her note: "tighter, same substance"). Volunteered that her older sister has not yet been looped into the succession thinking because the sister treats the topic as premature. Requested a third meeting with Tarek present and asked whether the framing would need revision for a spouse "not in the business." Volunteered the seven-figure tax-friction regret from the 2023 close. Updates Cat 13 (regret) and Cat 2 (joint financial agency confirmed, not Prospect-lead). Pattern match flag: resembles Existing Client 4's signal set.
- *2025-03-20. Question to surface.* Older sister's view on the 2028 horizon (she may read it as acknowledgment of mortality rather than a planning deadline, which would change sequencing). Paris notary's view on whether a US-side structure can interlock with the existing *mandat à effet posthume*. To surface in the third meeting only if she raises the sister question first; pressing it is hers to initiate.

### Layer 3 — Pattern match

- *Match #1.* Existing Client 4. Multi-jurisdictional family-business principal with a US-side exit secondary to a European-side inherited operating stake; Collective Harmony decision mode; Philosophy-lead Five Ps; female operator as family anchor; post-2020 diaspora sensitivity (Existing Client 4 is Egyptian-Levantine, comparable cultural surface). What worked there: opening at her selected cafe, scoping first proposal as a three-country coordination memo rather than a US-trust pitch, inviting spouse at meeting three not meeting one, pacing the relationship across a six-month arc with two written artifacts and one joint meeting with her Paris-side notary. What failed: a single attempt to include a US estate-planning partner before the banker had earned permission to convene; she did not respond for five weeks. Carry forward: do not convene advisors before earning it; French-language artifacts in parallel with English; never let the fintech exit become the anchor of any memo; mother's calendar is the household calendar. Avoid: single-advisor "quarterback" pitch, which reads as advisor-self-dealing in Collective Harmony mode.
- *Anti-pattern.* Existing Client 7. Surface match (Paris-raised, post-secondary-sale, European inherited interest) but culturally Individualist in family decision mode, with a mother who ceded business control a decade earlier. The "heaviest signal routes through mother" play that fits Prospect 2 failed with Existing Client 7, who treated structural memos routed through her mother as patronizing. Lesson: surface cultural markers (country, language, inherited stake) mislead; the Collective Harmony vs. Individualist distinction is the operative variable and must be confirmed before applying the pattern.

### Outreach play
- **Channel.** Warm intro-continuation via COI 9 (fellow French-American school finance committee member, warm temperature, two-year relationship, intros routed through the school's fall fundraising cycle have converted on two prior occasions).
- **Who introduces.** COI 9 by email, with a one-sentence context paragraph drafted by the banker and a French subject line ("Suite à notre conversation du comité"). Any bypass of COI 9 closes the door.
- **Opening angle.** A narrow cross-border continuity frame for the Paris jewelry stake, pegged to her mother's 80th birthday (November 2028) as the family-internal deadline. The frame treats the US-side continuation-vehicle release (September 2026) as a secondary liquidity input to the primary succession question, not as the anchor. Philosophy-first, Performance-last, in her own language.
- **Timing.** Post-Orthodox Easter 2026, pre-summer travel (late April through early June 2026). The September 2026 lock release is the latest viable pre-event window; waiting into Q3 2026 misses the planning runway and reduces the framing to a reactive tax conversation. Avoid Orthodox Easter week, her birthday week (April 14), and any day inside the French-American school graduation sequence.
- **Second-meeting artifact.** A bilingual four-page continuity memo: French on the left, English on the right, same content. The memo maps three instruments (a US-side dynasty trust sized to the 2023 proceeds, an updated *mandat à effet posthume* for the jewelry stake, and a Delaware family LLC that could receive continuation-vehicle distributions on release) against the 2028 family-internal deadline. No firm named. No US estate-planning partner named or invited. A single paragraph flags the seven-figure tax-friction regret she volunteered and proposes a coordinated unwind across 18 months.
- **Non-obvious signal that drove decision.** The Arabic "the project" reference for the jewelry business, switched out of every time she discussed the fintech exit, is the load-bearing signal. Any opener anchored on the US exit misreads the prospect as fintech founder first and family principal second. Inverting the anchor (November 2028 family birthday, not September 2026 US lock release) is the only opener that survives Rule 4. A second signal reinforces the choice: her prior-advisor postmortem ("they stopped knowing what was going on at home") frames "home" as Paris and Byblos, not Atherton. The coordinated cross-border continuity frame is the direct structural answer.

---

## PROSPECT 3 — fully populated

### Relationship stage
Post-first-meeting. An intro-continuation email on 2026-02-10 (quoting his 2023 essay by name and asking one diagnostic question rather than pitching) produced a 26-hour reply and a 2026-02-11 first meeting at his selected coffee shop near 24th Street. He arrived with a marked-up printout of the email and three written questions, volunteered that he has delayed the family office DAF-review four times, and did not volunteer dollar figures. No second meeting scheduled; target window is mid-April through late May 2026, with a written pre-read framing a 90-day scoped second opinion on the dormant DAF and the 2030 bypass trust sunset.

### Archetype
Next-generation wealth recipient, inherited Bay Area tech wealth, identity-work-in-progress G2 inheritor with independent earned income.

### Layer 1 highlights

**Cat 1 — Core identity and residences.** Prospect 3 is 34, born in San Francisco to a Turkish immigrant father (arrived 1985) and a Turkish-Cypriot mother (arrived 1988). US citizen by birth; Turkish dual nationality (his father registered him at the Turkish consulate at birth). Both passports current; the Turkish passport used annually. Rents a one-bedroom apartment in Noe Valley since 2021 despite a net worth that would support outright purchase. The Noe Valley apartment is his only residence. California tax domicile. No EA, no chief of staff, no scheduling assistant. Not married; three-year relationship with a partner in public-sector civic technology (separate residences). Preferred name is the Turkish form of his first name, not the Americanized variant his Stanford transcript carries; using the transcript version reads as a database pull.

**Cat 2 — Family, multi-generational.** Unmarried, no children. Sister (28) in a doctoral program in information science at Berkeley (third year of five), working on human-AI interaction; financially and legally independent but a co-beneficiary of the same inherited trust structure. Mother (62) remarried in 2023 to a Turkish-German financial consultant based in Berlin; she splits time between San Francisco and Istanbul. The remarriage has produced no additional children. Father died of a heart attack at 58 in August 2020. Paternal grandmother lives in Istanbul in fragile health (early-stage dementia acknowledged by the mother's side since 2024; not volunteered by Prospect 3 directly). His primary living family bond is with his sister; they speak weekly at minimum, and he routes every inheritance-adjacent planning question through her before responding to an advisor. Relationship with his mother is civil but cooler since the remarriage.

**Cat 3 — Education, across generations.** Prospect 3: Stanford Symbolic Systems (BS, 2013). No graduate degree. Informal continuing education through industry AI conferences (attendee since 2019, not a presenter). Sister at Berkeley (doctoral, third year of five). Late father: undergraduate in Istanbul, master's in computer science at a Texas state university (1989), the academic path that brought the family to the US on the H-1B-to-green-card sequence. Mother: lycée in Nicosia, no tertiary degree. Stanford alumni network is lightly used; he attends a class-reunion-adjacent dinner every two or three years. Not a Stanford giver. The Berkeley connection lives through his sister's cohort, not his own.

**Cat 4 — Wealth story.** G2 inheritor. His father accumulated wealth as an early engineering executive at a prominent Bay Area enterprise software company through pre-IPO grants and post-IPO vested stock; at death in August 2020 the estate was approximately $130M, split equally between Prospect 3 and his sister net of a residual interest for his mother. Prospect 3's share is roughly $65M, consolidated at the mother's family office (a US multi-family office since 2021) in a bypass trust with him as both current beneficiary and co-trustee. A separate inherited donor-advised fund sits at $1.2M, dormant since his father's death, with no gifts authorized in six years. His own earned compensation is separate: $250K base as a senior product manager at a mid-stage AI company plus approximately $600K annually in vesting RSUs from his own employer, custody held at a large retail brokerage with ~$1.4M in it today. The inherited portfolio is approximately 90/10 liquid/illiquid; the mother's family office diversified out of the father's employer stock across 2020–2022, so there is no concentrated single-stock position to unwind. No dynasty trust beyond the bypass structure. No GRAT, no CRT, no CLT, no foundation. Every existing product is an inheritance of the mother's family office selections, not his.

**Cat 5 — Professional history and boards.** Post-Stanford: three years at a consumer platform company as a PM, three at a developer tools company, two at an early-stage AI research lab (Series B when he joined), and since 2022 senior PM at the current mid-stage AI company. Career narrative in his own words: "I do the work." No public or private company board seats. One advisory role on an AI ethics non-profit, unpaid. Occasional posts on a personal blog about interpretability research. No LinkedIn activity beyond the current role line. Published one short essay in an industry newsletter (2023) on the difference between what users say they want from AI products and what they actually build patterns around. That essay is the operative public surface; quoting it by name in a first written touch is the entry condition for the relationship.

**Cat 6 — Cultural origin and orientation.** Second-generation American, both parents first-generation Turkish immigrants. Paternal Alevi lineage, maternal Turkish-Cypriot Sunni-adjacent; not religiously observant. Speaks Turkish conversationally with a US accent his paternal relatives in Istanbul tease him about; reads Turkish only with effort. Identifies as American first, Turkish second, and specifically Alevi-descended Turk third when the topic of religion arises, which it rarely does. Holds a small inactive interest in a family apartment on Istanbul's European side that his father co-owned with two paternal uncles. Travels to Istanbul annually in mid-October for ten days to spend time with his paternal grandmother and uncles. Family decision-making mode reads Individualist-with-sibling-veto: decisions are his, not his mother's, and the sister carries an implicit veto on anything touching the inherited trust or the grandmother's future care. His parents' immigration story is a story he tells carefully; he watched his father tell it differently in public and in private and has absorbed the discipline.

**Cat 7 — Food, beverage, dietary.** No dietary restrictions, no religious observance. Consistently selects a specific third-wave coffee shop near 24th Street in Noe Valley for every meeting he schedules; has selected it for all five prior advisor conversations and the first conversation with the banker. Cuisine preferences: Mexican (the reason for his twice-yearly Mexico City trips, which follow a rigorously researched food agenda), Turkish meze, Japanese, Californian farm-to-table only when someone else picks the venue. Wine: rare, natural-wine preference when he drinks, no cellar. No spirits. Pour-over black coffee, no sugar, no exceptions. Declines meal-based advisor meetings as a matter of course; has declined two dinner proposals to date.

**Cat 8 — Sports, fitness, hobbies, travel.** Runs three times a week, short routes in Mission Dolores Park and Bernal Heights. Climbs at a local bouldering gym twice a week. Does not play tennis, does not golf, no club memberships of any kind. Hobbies: reads more fiction than nonfiction, maintains a curated library of twentieth-century Turkish literature in translation, plays in a private trivia league with former Stanford friends. Travel rhythm: Istanbul mid-October for ten days, Mexico City twice a year for five to seven days each on a food agenda, one long weekend in rural California in late spring, a short Berlin trip every other year since his mother's remarriage. Commercial economy domestic, premium economy international; no private aviation. Cultural consumption: SFMOMA member events, one film-society subscription, avoids symphony and opera.

**Cat 9 — Personality and communication.** Reserved, analytical, deeply skeptical. Tests every new person before trusting any of them; the test is always an attention test, not a credentials test. Detail-oriented on narrow topics (AI product design, Turkish literature, Mexico City taquerias) and dismissive of what he reads as advisor-manufactured urgency. Deliberative on anything inheritance-adjacent; decisive on his own career. Preferred channel: email only, short messages, bullet format. Texts only his sister, his partner, and two close friends. Response-time norm: 48 hours on substance, same-day on scheduling. Calendar is on his own laptop. Prefers 3pm to 5pm meetings at his selected coffee shop, 45 minutes maximum. Declined a walking meeting once with the reason "I can't read notes while walking." Five Ps rank ordering: People > Process > Philosophy > Fees > Performance. Fees mid-stack, not bottom, because he has been burned by opacity. Performance genuinely last; he reads performance-lead pitches as a category error. Media diet: a daily finance-and-law commentary column, long-form tech journalism, The Atlantic, one Turkish left-liberal newsletter, Asterisk magazine, interpretability-research Twitter.

**Cat 10 — Philanthropy.** The $1.2M dormant inherited DAF is the only formal giving vehicle; no gifts authorized in six years. Stated once: "I don't want to play philanthropy with my father's money without a thesis." Direct personal giving is modest, $10–20K annually, split across a Mission District community organization, an AI alignment non-profit, and an Istanbul-based civil society organization focused on earthquake response. No naming gifts. No non-profit board seats beyond the unpaid AI ethics advisory role. Development offices and naming-gift paths are irrelevant to the relationship. The dormant DAF is a conversation, not a product opportunity; forcing it becomes the failure mode.

**Cat 11 — Network, memberships, centers of influence.** No club memberships. Minimal alumni engagement. Close friends referenced by first name: his sister (always by first name, frequently), his partner (first name, less frequently in professional context), two Stanford Symbolic Systems classmates now at AI companies, one high school friend from San Francisco who is a public defender. The sister is the effective intro-source-of-record for anything touching the inherited trust; a request that bypasses her reads as an end-run and closes the relationship. The mother's family office is the existing advisor relationship and the incumbent he is evaluating; he will walk from any meeting that feels like a mandate competition. Prior advisor history: five meetings over 18 months, zero hired. For each of the five he researched the advisor's LinkedIn profile in advance and asked a specific question about a post or publication; the recognition failure rate is what ended each conversation. First-material-proposal discipline: the banker must demonstrate he has read the prospect's own essay and show it in writing, not in conversation.

**Cat 12 — Conversational signals and behavioral notes.** Topics volunteered unprompted: his own AI work, his sister's doctoral research (he sketches her dissertation in three sentences and does so unprompted), his Istanbul trips, his grandmother's apartment and the smell of his uncle's kitchen, the Mexico City restaurant circuit, his distrust of founders who talk about "impact." Topics avoided: specific dollar figures from the inherited portfolio, the word "inheritance" itself (replaced with "what my father left" or silence), his father's public career as a known Bay Area tech executive (he does not surface the recognizability), his mother's remarriage (referenced obliquely, the stepfather never named). Topics returned to repeatedly: what to do with the dormant DAF, how to keep the trust architecture from dictating his life, the question of whether he should tell his sister about the full scale of the distributions he has received (she knows approximately, not exactly). Names: sister by first name, partner by first name, late father as "my father" or "my dad" without a given name, mother as "my mother" (not "Mom"), stepfather never named. Pacing: quick on his own topics, slow and measured on anything inheritance-adjacent, 20 to 30-second pauses when genuinely thinking through a planning question. Boundaries voiced: "I don't want to meet at home," "I don't want to talk about performance," "I don't want a pitch." Discovery answers captured: values question ("I want to not let this thing make me a worse version of myself"); three-year question ("the DAF is active with a thesis my sister and I wrote together; the trust architecture has an explicit exit ramp for when I want to consolidate it under my own control; I have not become someone I wouldn't have respected at 25"); prior-advisor diagnostic ("they all sound the same, none of them noticed me noticing them"). First-vs-third-person wealth language: third person on everything inherited ("the money," "the trust," "what my father left"); first person on his own earned compensation ("my salary," "my options"). The split is consistent across 14 recorded turns and is the operative diagnostic for identity-work-in-progress.

**Cat 13 — Sensitive information (volunteered only).** Volunteered: sustained low-grade anxiety about the inherited portfolio and a specific fear that he will "do something dumb" and damage the relationship with his sister; a regret that he did not ask his father direct questions about money before the heart attack; a matter-of-fact therapy history. Grandmother's dementia has been mentioned by his mother in a separate conversation with COI 11, not by Prospect 3 directly; the Book records the fact but does not surface it. Not volunteered and therefore empty: his own health status, political orientation beyond implicit signals, father's cause of death beyond "heart attack at 58," financial or personal detail of the mother's remarriage. The word "inheritance" reads as a trauma-adjacent register; the Book does not use it in any written touch to him.

**Cat 14 — Trigger events and timing markers.** Forward triggers: sister's doctoral defense (expected spring 2028); grandmother's care trajectory across the next 24–36 months; the bypass trust's 10-year administrative anniversary in 2030, at which the current structure sunsets without his explicit instruction; the dormant DAF's sixth-anniversary no-gift status (end of 2026) which triggers an internal family-office review conversation he has delayed four times; his own 35th birthday (January 9, 2027). Personal milestones: his own birthday January 9, sister's March 22, father's death anniversary mid-August, paternal grandmother's birthday late November. Recent transitions in the last 24 months: his mother's 2023 remarriage and new travel pattern; his sister's 2024 transition to doctoral candidacy; his own 2024 promotion to senior PM. Calendar avoidances: the August anniversary window of his father's death (each year, two weeks on either side, non-negotiable); the mid-October Istanbul trip (he is offline); the two Mexico City trips. No religious-observance windows. Last touch 2026-02-11 (coffee at his selected shop, intro via COI 11). Next scheduled touch open; the target window is mid-April through late May 2026, after his mother's return from Istanbul and before the summer.

### Layer 2 — Decision log excerpt

- *2026-02-04. Inference drawn.* Trigger: research pass ahead of the first meeting scheduled via COI 11. Read the 2023 essay Prospect 3 published on user-said-versus-user-did patterns in AI products. Inference: the essay's frame, watching what people pattern around rather than what they claim to want, is his working epistemology and he applies it to advisors. The next written touch must be written in the voice of that frame, not the voice of a pitch. Updates Cat 5 and Cat 9.
- *2026-02-09. Move considered.* Three options: (a) a structured second-opinion memo on the full inherited portfolio with a named lead critique of the mother's family office, rejected for triggering the mandate-competition reflex that ended five prior conversations; (b) an unframed first meeting at his coffee shop with no written pre-read, rejected for wasting the highest-leverage signal (his essay) and confirming the "they all sound the same" read; (c) a pre-read that engages his essay by name, proposes a narrow 90-day governance-and-identity second opinion scoped only to the dormant DAF and the bypass trust's 2030 sunset, and states explicitly that the mother's family office is not in scope, selected because it threads both his discovery answers and the prior-advisor failure pattern.
- *2026-02-10. Move taken.* Sent a two-paragraph email intro-continuation note written in the voice of a question rather than a pitch. Opening sentence referenced his essay and named the specific user-said-versus-user-did frame without flattering him on it. Asked one question: "What would have to be true about a next advisor conversation for it not to collapse into the fifth version of the same one?" Attached no deck, no capability statement, no firm-branded PDF.
- *2026-02-11. Outcome.* He replied within 26 hours, short. Accepted the coffee shop meeting. Arrived with a single marked-up printout of the email and three written questions, one of which was "what does a 90-day second opinion look like if you are genuinely not asking for a mandate." Volunteered that he has delayed the family office DAF-review conversation four times. Did not volunteer dollar figures and did not ask the banker to state any. Pattern match flag: anti-pattern check against Existing Client 8 required before any scoping document.
- *2026-02-16. Question to surface.* Whether his sister is a participant in the 90-day second opinion or an observer (the difference changes the artifact). Whether the grandmother's care trajectory should enter the governance scope or be held until he surfaces it. Whether the DAF thesis is one he wants to write with his sister or alone. To surface: the sister question at meeting three, not meeting two; the grandmother question not at all unless he raises it.

### Layer 3 — Pattern match

- *Match #1.* Existing Client 12. G2 tech inheritor, consistent third-person-on-inherited-first-person-on-earned wealth language, father as invisible anchor, sister relationship load-bearing, Individualist-with-sibling-veto decision mode, essay-writing published habit. What worked: first written touch quoted his own published writing with precision and without flattery; scoping the engagement as a 90-day governance review with a defined exit made it feel opt-in rather than sales-funnel; including the sister in writing (not meetings) as a second reader of every artifact created a shared epistemic frame between the siblings without making the sister a client; sequencing identity-frame conversations before any structural redesign; refusing to surface his father's public career unless he surfaced it first. What failed: one early attempt to propose a family governance document that included the mother by default (not by his explicit invitation) triggered a two-month cooling. Carry forward: quote his essay; scope narrowly; write the sister in as a reader only with his permission; never surface the mother or the grandmother unprompted; avoid the word "inheritance" in writing. Avoid: any document that names the mother's family office in a critique register, any document proposing a family governance structure, any mention of performance.
- *Anti-pattern.* Existing Client 8. Surface match (G2 inheritor, third-person wealth language, refusal of standard mandate pitches, declined four advisors in 14 months), but his third-person language was avoidance of detail rather than identity work; the 90-day scoped engagement that worked for Existing Client 12 bored Existing Client 8 within 30 days because he did not want to do identity work, he wanted the administrative friction to go away. Lesson: third-person wealth language is necessary but not sufficient; the Book must confirm the prospect is doing identity work (Prospect 3's "I don't want to become someone I wouldn't have respected at 25" answers this) before applying the Existing Client 12 play. Applied here: Prospect 3 is on the identity-work side of the line; proceed, but build in an explicit 30-day checkpoint at which either side can walk.

### Outreach play
- **Channel.** Warm intro via COI 11 (Berkeley faculty member who taught both siblings in separate undergraduate courses, warm temperature, trusted by the sister and therefore implicitly trusted by Prospect 3). COI 11 is a single-use introduction surface for this household; additional intro requests through her will strain the relationship.
- **Who introduces.** COI 11 by email with no firm reference and no role title, addressed to Prospect 3 with his sister copied at her explicit prior permission. The banker drafts the context paragraph in plain language without naming any firm or service.
- **Opening angle.** A 90-day governance-and-identity second opinion scoped only to the dormant DAF and the 2030 sunset question on the bypass trust. States explicitly in writing that the mother's family office is not in scope, that no mandate is being sought, and that the 90-day window has a defined exit on either side. The written frame quotes his essay by name and uses his user-said-versus-user-did language as the operating epistemology for the engagement itself.
- **Timing.** Mid-April through late May 2026, after his mother's spring return from Istanbul and before the summer slow period. Strictly avoids the August father's-death anniversary window (two weeks either side), the mid-October Istanbul trip, and the two Mexico City trips. The year-end 2026 internal DAF-review the family office has scheduled is the natural inflection; acting before that review preserves his agency over the thesis.
- **Second-meeting artifact.** A three-page governance memo: one page framing the DAF thesis as an open question (not a proposal), one page mapping the 2030 sunset as a decision tree with three options and their reversibility characteristics, one page stating the 90-day engagement terms including a 30-day checkpoint. No firm name. No capability statement. The sister is named as a second reader with his explicit permission, or not named at all if that permission is not yet given. A single sentence, not a paragraph, references his essay.
- **Non-obvious signal that drove decision.** The load-bearing signal is not the third-person wealth language on its own; that is necessary but not sufficient, per the Existing Client 8 anti-pattern. It is the pairing of the third-person language with his first-person discovery answer ("I don't want to become someone I wouldn't have respected at 25"). That combination places him on the identity-work side of the line. The second load-bearing signal is that he noticed, in each of five prior advisor meetings, that the advisor did not notice what he had written; quoting his essay in writing is not flattery, it is the entry condition. The third signal is the dormant DAF itself: six years of no gifts from a $1.2M balance is avoidance sustained over time, and a 90-day scope gives him a discrete surface on which to do the work he has already said he wants to do, without forcing him to do it on the full portfolio at once.

---

## EXISTING DELIVERABLE FILES

- **/Users/Mario/jpmproject/prospecting/ai-augmented-uhnw-prospecting.mdx** — v1 deliverable. Treat as scaffolding only. Reusable: opening narrative (~310 words, decent landscape-setting), some framing in strategic memo, extensibility sidebar, closing questions structure, Notes & Sources. NOT reusable: schema section (too tight), profiles (need full rewrite from scratch using new Layer 1+2+3 structure), AI subsections (compress massively).
- **/Users/Mario/jpmproject/prospecting/memory.md** — original pre-flight working memory (Verdi/JPM/Mario context).

---

## STRATEGIC MEMO REVISION NOTES (pending)

When we get to the memo:
- **Compress the AI sections** to one ~80-word paragraph at the end of the memo.
- **Fold in the load-bearing data point**: 67% of affluent prospects who hired an advisor already knew someone with that advisor (Oechsli). Justifies the Book's emphasis on relational mapping as a first-class citizen.
- **Add a tight section on what the Book actually solves**: ocean-boiling fails because templated outreach cannot adjust to the prospect's heaviest weighted P; relationship intelligence reframes top-of-funnel as fit-diagnosis first, capability demonstration second.
- **Keep the workflow paragraph short**: first encounter logs to Book within 24 hours; conversational signals verbatim; public signals refresh monthly via research-compression pass; every prospect carries a single-sentence outreach thesis.

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
