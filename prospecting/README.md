# Client Book Project — Hub

UHNW prospecting case study ("The Client Book") to publish on mario-mercado.com. Three prospects across three Bay Area tech archetypes, grounded in a 14-category schema, three-layer architecture, and a documented inference model.

Read this file first every session. It is the orientation layer.

---

## Status

**Phase:** Substance-locking. Three prospects fully drafted. All three pending Mario's revision notes.

**Drafted, pending revision notes (4 prospects, staggered across the BD funnel):**
- Prospect 4 — pre-liquidity Bay Area tech early employee at a large pre-IPO AI company; mid-career, first-in-family $20M+ wealth; American-born Mexican-American; pre-M1 (qualification stage, no outreach executed). See `website/prospect_4.md`.
- Prospect 3 — next-gen wealth recipient, multi-generational US white American, inherited Bay Area tech wealth; post-M1 (first-touch executed, M2 not yet scheduled). See `website/prospect_3.md`.
- Prospect 1 — exited tech founder, mid-career, post-acquisition; Indian-American naturalized US citizen; post-M2 (M3 scheduled with spouse). See `website/prospect_1.md`.
- Prospect 2 — foreign-born first-gen operator, French-Lebanese, multi-jurisdictional family business; post-M2 (M3 requested by prospect with spouse). See `website/prospect_2.md`.

The four prospects map to the BD funnel: **Prospect 4** demonstrates qualification (the Prospect File identifies the candidate, plans outreach, decides timing); **Prospect 3** demonstrates first-touch outreach (the click that lands M1); **Prospects 1 and 2** demonstrate post-M1 discovery and multi-meeting depth in two distinct cultural contexts. The four Prospect Files together form the **pipeline**: qualification at the top, multi-meeting depth in the middle, existing-client relationships (referenced in pattern maps) at the far end.

**Locked (do not revisit unless explicitly reopened):**
- Frame: Client Book case study, not a firm-specific playbook.
- Naming convention: Prospect N, Existing Client N, COI N. No fictional names.
- Three-layer Prospect File architecture: Profile / Decision Log / Relational Graph.
- 14-category Layer 1 schema with ~150 fields and if/thens.
- Layer 2 Decision Log (6 entry types).
- Layer 3 Relational Graph (COI Ledger + Pattern Map).
- Inference Layer (5 rules + 3 discovery answers).

---

## Sequence (in order, gated)

1. Incorporate Mario's revision notes on Prospects 1, 2, 3, and 4. **Wait for explicit notes per prospect; do not re-draft without them.**
2. Strategic memo light revision. **Drafted in `drafts/strategic_memo.md`, pending Mario's review.** Compressed AI to one ~80-word paragraph. Folded in Oechsli 67% data point. Added "What the Prospect File actually solves" section. Renamed "the Book" → "the Prospect File" in body throughout the project; "The Client Book" stays as the case-study title.
3. Opening narrative light revision. **Drafted in `drafts/opening.md`, pending Mario's review.** Updated to: Prospect File / pipeline terminology, four prospects not three, four-snapshot framing per option A. Three research-driven updates added: cadence-lengthening note (industry has moved to 10-15 touches with AI personalization, but the fit-diagnosis problem persists), practitioner-canonical four-stage funnel naming (targeting → outreach → discovery → advancement) per Kitces / CEG / Bowen / Prince / Allison, and sharpened "snapshot at a decision point" phrasing tied to the Prospect File.
4. Closing revision. **Drafted in `drafts/closing.md`, pending Mario's review.** Removed the v1 three-question closing entirely; replaced with a one-line bridge into Notes & Sources: *"The framework above synthesizes the practitioner literature named below into one working approach."* Reasoning: declarative craft thesis requires voice-of-craft authority Mario is earning rather than claiming; open-question closers read as essay-literary for this audience; the work already makes its arguments.
5. Extensibility sidebar revision. **Drafted in `drafts/extensibility.md`, pending Mario's review.** Mostly survived v1: three worked verticals intact (Latin American multi-generational family office, legacy industrial family, specialty medical practice family). Added a three-sentence bridge so the reader knows the sidebar is about Layer 1 schema extensibility, not whole Prospect File methodology. Minor phrasing touches (Bogotá accent; partnership buy-in vs. practice buy-in).
6. Project card entry rewrite. **Drafted in `drafts/project_card.md`, pending Mario's review.** Fixed outdated counts (3 archetypes → 4; 9 categories → 14). Rewrote summary to lead with banker craft (Prospect File, outreach discipline, BD funnel staggering); AI line survives but moves to the end. Reordered techStack (plain tools before AI tools). Added banker-craft toolCombinations before the AI pairing.
7. Notes & Sources expansion. **Drafted in `drafts/notes_and_sources.md`, pending Mario's review.** 38 entries across four layers (practitioner mental-model, operational craft, AI tooling positions, industry landscape). Added seven new entries from the step-3 research pass: Oechsli 2023 Affluent Research, Kitces 5-Step Prospecting Process, Kitces Marketing KPIs, Kitces with John Bowen on HNW prospects, Kitces Advisor Marketing Strategies, Cerulli 2026 Advisor Metrics, Schwab 2025 RIA Benchmarking Study. URLs verified at time of drafting.
8. Fresh full draft of the deliverable. **Drafted in `website/deliverable.mdx`, pending Mario's review.** Assembled from the approved drafts (frontmatter, opening, strategic memo, extensibility, closing bridge) plus two newly composed sections (the Prospect File Architecture overview; four condensed prospect profiles). All 35 Notes & Sources citations renumbered into one sequential list. v1 mdx (`ai-augmented-uhnw-prospecting.mdx`) left untouched. Post-draft edit: Layer 3 Relational Graph now carries a client-confidentiality caveat (Pattern Map draws only from banker's directly-served clients; COI Ledger reflects banker's own network within their own book); same caveat mirrored in working_memory_v2.md.
9. Site integration. Locate Next.js repo for mario-mercado.com (not on this machine; Mario provides). Reconcile frontmatter against existing project mdx files. Drop into content/projects/. Add project card entry to homepage enumeration.
10. Vercel deployment via git push.

Do not skip past gate 1 without explicit confirmation that all three prospects are locked.

---

## Active constraints (non-negotiable in body text)

- **No em dashes anywhere.** Use commas, periods, parentheses.
- **Zero firm names in body text.** Firms appear only in Notes & Sources.
- **Zero individual names in body text.** Practitioners appear only in Notes & Sources.
- **Banned phrases:** "basically," "sync up," "push the envelope," "run it up the flagpole," "cadence" (for meetings), "leverage AI solutions," "in today's fast-paced landscape."
- **Naming convention:** Prospect 1, Prospect 2, Prospect 3. Existing Client 1, Existing Client 2, etc. COI 1, COI 2, etc.
- **Voice:** practicing senior UHNW private banker. Active voice. No hedging on data-backed claims.
- **Frame:** every research finding lands as "this is what the Prospect File captures" or "this is the decision the Prospect File drives," not as top-down methodology.

Full constraint discussion and banned-phrase justification live in `working_memory_v2.md` under **VOICE AND CONSTRAINTS** and **FRAME DECISIONS**.

---

## File map

| File | Purpose |
|------|---------|
| `README.md` | This file. Orientation layer. Read first every session. |
| `working_memory_v2.md` | Frame, voice constraints, three-layer architecture, full 14-category Layer 1 schema with ~150 fields and if/thens, Layer 2 / Layer 3 structures and worked examples (COI 4 on the Ledger), Inference Layer, strategic memo revision notes, acronym glossary, Notes & Sources. |
| **`website/`** | **Upload-bound folder. Every file Mario will upload to mario-mercado.com via Vercel lives here; nothing else.** |
| `website/deliverable.mdx` | **Step-8 fresh full draft of the deliverable.** The main case-study page. Assembled from all approved drafts plus architecture overview and four condensed prospect profiles. 35 sequential citations in Notes & Sources. |
| `website/prospect_1.md` | Prospect 1 (post-M2). Full profile: relationship stage, archetype, Layer 1 highlights, Layer 2 decision log, Layer 3 pattern match, outreach play, provenance ledger. |
| `website/prospect_2.md` | Prospect 2 (post-M2). Same structure. |
| `website/prospect_3.md` | Prospect 3 (post-M1). Same structure. |
| `website/prospect_4.md` | Prospect 4 (pre-M1, qualification stage). Same structure; Direct bucket in provenance ledger is empty by design. |
| `drafts/strategic_memo.md` | Step-2 strategic memo light revision. Compressed AI to one ~80-word paragraph; folded in Oechsli 67% data point; new "What the Prospect File actually solves" section. Incorporated into `website/deliverable.mdx`. |
| `drafts/opening.md` | Step-3 opening narrative light revision. Updated terminology, prospect count, four-snapshot framing, research-driven cadence + funnel-stage updates. Incorporated into `website/deliverable.mdx`. |
| `drafts/closing.md` | Step-4 closing revision. Removed v1's three-question structure; replaced with a one-line bridge into Notes & Sources. Incorporated into `website/deliverable.mdx`. |
| `drafts/extensibility.md` | Step-5 extensibility sidebar revision. Three verticals (Latin American family office, legacy industrial, specialty medical practice) preserved; added a three-sentence bridge at the top. Incorporated into `website/deliverable.mdx`. |
| `drafts/project_card.md` | Step-6 project card frontmatter rewrite. Updated counts, banker-craft-first summary, reordered techStack and toolCombinations. Incorporated into `website/deliverable.mdx`. |
| `drafts/notes_and_sources.md` | Step-7 Notes & Sources expansion. 38 entries across four layers (practitioner mental-model, operational craft, AI tooling positions, landscape). URLs verified. Incorporated (renumbered to 35 sequential citations) into `website/deliverable.mdx`. |
| `memory.md` | Original pre-flight context (audience, stakes, definition of done, definition of wrong). Frozen. |
| `RESUME_PROMPT.md` | Session-bridging artifact from a prior session. Frozen, do not edit. |
| `ai-augmented-uhnw-prospecting.mdx` | v1 deliverable at project root. Scaffolding only. Do not edit unless explicitly told. `website/deliverable.mdx` supersedes this; v1 stays as historical reference. |
| `~/.claude/CLAUDE.md` | Mario's voice and style guide. Critical for the writing. |

---

## Last updated

2026-04-23. Reorganized prospect content into `prospects/` directory; created this hub; rewrote Prospect 3 from Turkish-American to multi-generational US white American to rebalance the trio's heritage distribution; added Provenance ledger section to all prospect files (two top-level buckets: Public information and Direct interaction, with per-meeting chronology inside Direct); added an Acronyms and Terms glossary to working_memory_v2.md; added Prospect 4 (pre-liquidity AI-co early employee, American-born Mexican-American, qualification stage) to make the prospect set stagger across the BD funnel; drafted the strategic memo light revision (`drafts/strategic_memo.md`); fixed Prospect 1's pre-lockup timing math; renamed "the Book" → "the Prospect File" in body throughout (with "The Client Book" preserved as the case-study title) and added pipeline framing.

2026-04-24. Consolidated upload-bound files into `website/` folder: `deliverable.mdx` (main case-study page) + `prospect_1-4.md` (full prospect profiles). Nothing else in `website/`; these five files are the exact set for upload to mario-mercado.com via Vercel. `prospects/` directory removed (empty after moves). Drafts and working memory remain in place as revision artifacts and internal reference.
