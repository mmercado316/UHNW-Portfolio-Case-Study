# JPM Private Bank Prospecting Project — Working Memory

Working context document for the UHNW client prospecting playbook case study. Kept separate from the final specification prompt.

---

## Context

- **Project**: mock "client book" / prospecting playbook, published as a new case study on mario-mercado.com
- **Audience**: Verdi Disesa, Executive Director, JPM U.S. Private Bank (no direct mention of him or JPM anywhere in the deliverable)
- **Target role**: Senior Associate, U.S. Private Bank (one level below the posted VP role)
- **Target outcome**: Verdi sees Mario as someone who already thinks like a JPM Private Banker, not a candidate who needs training. Drives a second-round interview.

## Stakes

- Differentiator in a competitive field. Not do-or-die but "iffy" without it.
- Must actually land. A generic mock hurts more than it helps because it signals Mario heard Verdi but did not understand him.

## Definition of Done

- New project card on mario-mercado.com, following the existing card format (title, 2-3 sentence description, tech stack badges, domain tags, tool combinations, link to detail page).
- Detail page contains three integrated components:
  - Polished case study (narrative framing and thesis)
  - Small working prototype (the client book itself)
  - Strategic memo
- Single vertical: Bay Area tech UHNW (founders, early employees, exited operators).
- Zero mention of JPM or Verdi. Reads as generally applicable to UHNW advisory.
- Tight, not sprawling.
- Reader finishes impressed.

## Definition of Wrong (the failure modes to avoid)

- CRM schema dump instead of a prospecting playbook.
- Frames the work as data harvesting instead of relationship intelligence captured from attentive listening.
- Focused on "finding them" when Verdi's pain is "converting them."
- Generic mock profiles instead of non-obvious insights that drive the outreach angle.
- Strategic memo reads like a SaaS pitch deck instead of a banker's operating framework.
- Polished but shallow: a practicing UHNW banker reads three lines and knows the author has not done the work.

## Thesis / Core Frame

- **Verdi's line**: "If you speak to a client and you don't know what they want and what they're looking to solve, then we can't get them a solution."
- **Verdi's pain**: senior associates and VPs boiling the ocean with generic templated outreach. He wants bespoke outreach that "gets them to click."
- **The prospecting goal**: get the first meeting. Not close business, not sell a product. Convert a cold or warm lead into a seated conversation.
- **Data source**: attentive listening in conversation, cross-referenced with public signals (news, LinkedIn, board seats, philanthropic activity). Not forms. Not covert collection.
- **The "book"**: a memory and pattern system that turns conversation fragments into a coherent outreach decision.

## Mario's Angle / Credibility

- Analytical background.
- Language skills.
- Cultural fluency.
- Modest network. Do not oversell.

## Dimensions the Client Book Should Capture

- Financial profile (net worth tier, liquidity event history, asset concentration)
- Family structure (spouse, kids, schools, extended family in market)
- Cultural origin and orientation (first-gen immigrant, country of origin, language, ties)
- Personality axis (reserved/outgoing, analytical/intuitive, skeptical/receptive)
- Preferred social modality (dinner, sporting event, office meeting, phone)
- Food and wine preferences, dietary restrictions
- Spirituality and religious observance
- Professional history, board seats, portfolio companies
- Philanthropic interests
- Conversational signals and behavioral notes (what they volunteer, what they avoid)

## Decomposition (locked)

1. **Research** — how elite UHNW advisors actually prospect (channels, COIs, referrals, events, AI tooling usage)
2. **Strategic memo** — the thesis on modern UHNW prospecting and how relationship intelligence beats ocean-boiling
3. **Client book schema** — data model with rationale per field and how each field drives an outreach decision
4. **Mock profiles** — **3** fictional Bay Area tech UHNW profiles, each a distinct archetype, each paired with a recommended outreach play
5. **Extensibility sidebar** — short callout (~150 words) showing how the schema adapts to 2-3 other verticals (e.g., Latin American family office, legacy industrial family, next-gen wealth)
6. **Case study narrative** — the read-through that ties research + memo + schema + profiles + sidebar together
7. **Website integration** — new project card and detail page matching existing format
8. **Polish pass** — does it sound like a banker wrote it

## Scope Decisions (locked)

- **Profile count**: 3, not 5. Three is the minimum to show pattern; five risks filler. Add a 4th or 5th only if a meaningfully different archetype emerges that the first 3 do not cover.
- **Vertical**: single vertical (Bay Area tech UHNW). Depth over breadth. Mario has genuine cultural fluency here. Extensibility sidebar proves the framework generalizes without diluting the main case.
- **Profile archetype targets** (to maximize differentiation across 3):
  - Exited tech founder (mid-career, post-IPO or acquisition)
  - Foreign-born first-gen operator (immigrant wealth with multi-jurisdictional family)
  - Next-gen wealth recipient (inherited Bay Area tech wealth, generational transition)

## Hard Parts (Q7 answers)

1. **Voice authenticity**: writing like a practicing UHNW banker without being one yet
2. **Profile specificity without caricature**: avoiding Patagonia vest / Stanford MBA / Napa vineyard cliches; details must feel observed
3. **Schema-to-action inference layer**: every field must drive an outreach decision, not just exist
4. **AI tooling point of view**: showing where AI augments (signal gathering, pattern recognition) and where it must not replace (the listening, the judgment, the trust)
5. **Length discipline**: the topic wants to sprawl; cutting is the hard part of the writing

## Related Existing Work

- **UHNW Portfolio Transition Analysis** (already on site). This new project is the "find them" companion to that project's "serve them." Together they demonstrate full UHNW workflow competency.

## Status

- Prompt 0 pre-flight: complete
- Specification prompt: approved. Ready to execute in a fresh session.

## Final Spec Key Decisions

- **Research emphasis**: top 1% performers only. The characteristic-to-approach inference layer. Named practitioners and firms (Bessemer, BBH, Rockefeller, Goldman PWM, Cresset, Pathstone) plus figures like Charlotte Beyer, Tim Kochis, Jim Grubman. Do NOT name JPM in the deliverable.
- **Word count**: 2,000 to 3,000 target, up to 3,500 allowed only when cutting would compromise a load-bearing argument.
- **Traceability bar**: at least 3 distinct inferences in the memo and schema rationales must be sourced to specific practitioner content, listed in Notes & Sources.
- **Deployment**: mario-mercado.com is deployed via Vercel. Output should be structured for a Next.js / Vercel workflow (Markdown or MDX, ready to commit and deploy). The executing agent should confirm the site's specific content format before writing final files.
