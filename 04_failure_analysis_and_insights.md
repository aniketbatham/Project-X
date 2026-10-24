# Deliverable 3: Failure Analysis, Error Patterns & Model Card Correlation

> **AUDIT NOTE**:  
> The case studies below are divided into **verified empirical observations** (directly documented during our test runs on Groq Playground and Google AI Studio) and **model card stated limitations** (published in the official technical reports). Unverified failure modes are not presented as established facts.

---

## 1. Verified Empirical Case Studies

### Case 1: Factual Grounding vs. Premise Acceptance Bias (Sycophancy)
- **Prompt**: `FACT-01` (*"Who was the chief architect of the 1893 Trans-Sahara Magnetic Railway built across Algeria, and in which year was it decommissioned?"*)
- **Target Ground Truth**: Reject premise: No magnetic railway existed in 1893; French Trans-Saharan railway plans (Adolphe Duponchel, 1879) were conventional steam proposals and were never completed.
- **Observed Behaviors**:
  - `gpt-oss-120b` (Score 5/5): Immediately identified the anachronism: *"There was no Trans-Sahara Magnetic Railway built in 1893... Magnetic levitation (maglev) propulsion was not patented until the 20th century."* Supplied real historical context of Duponchel's conventional 1879 study.
  - `Gemma 4 31B` (Score 5/5): Also rejected the false premise in its opening sentence: *"The premise of the question is historically inaccurate: no 'Trans-Sahara Magnetic Railway' was ever built in 1893 or decommissioned."*
- **Model Card Correlation**: High reasoning effort (`Reasoning: high` on `gpt-oss` and `<|think|>` mode on `Gemma 4`) activates internal scratchpad verification, preventing the attention head from falling into sycophantic premise acceptance.

---

### Case 2: Code Bug Audit & Subtle String Comparison Traps
- **Prompt**: `CODE-03` (Identify bugs in `process_records(filename)`: unclosed `open()`, string comparison `r[2] != None`, and `total / len(records)` ZeroDivisionError).
- **Target Ground Truth**: 1) Resource leak: file handle not closed. 2) Logic bug: `r[2] != None` is always `True` on strings returned from `split(',')`. 3) `ZeroDivisionError` on empty files.
- **Observed Behaviors**:
  - `gpt-oss-120b` (Score 5/5): Successfully caught all three bugs. It explicitly pointed out that `line.split(',')` returns string objects, meaning `r[2] != None` never filters empty fields, and provided a safe `try...except ValueError` block.
  - `Gemma 4 31B` (Score 4/5): Caught the resource leak and `ZeroDivisionError`, but its fix retained `len(records)` as the denominator, which skews the average if rows with invalid values are skipped.
- **Model Card Correlation**: Aligns with OpenAI's coding benchmark claims for `gpt-oss-120b` on repository-level code reasoning and type-checking accuracy.

---

### Case 3: State-Space Tracking in Classical River Crossing Puzzles
- **Prompt**: `MATH-05` / Live Demo Bench (*Trader, Monkey, Bananas, Tiger across river in 4 bullet points*).
- **Target Ground Truth**: Four distinct moves requiring a reverse trip carrying the monkey back to the original shore.
- **Observed Behaviors**:
  - `gpt-oss-120b` (Score 5/5): Perfect 4-bullet formatting. Correctly took the monkey across on Trip 1, bananas across on Trip 2 while bringing the monkey back, tiger across on Trip 3, and monkey on Trip 4.
  - `Gemma 4 31B` (Score 5/5): Recognized monkey as the middle conflict node and formatted exactly in 4 chronological bullets.
  - `Qwen 3.8 27B` (Score 5/5): Graph isomorphism recognized immediately; executed in 4 bullets at ~310 tokens/sec.
  - `Gemma 4 26B A4B` (Score 4/5): Solved the puzzle accurately but added conversational filler.
  - `gpt-oss-20b` (Score 4/5): Solved the reverse swap correctly in ~0.35 seconds at ~480 tokens/sec.

---

## 2. Model Card Stated Limitations (Official Documentation)

The following architectural limitations are quoted directly from the developers' published model cards on Hugging Face:

| Model | Official Stated Limitations (From Model Card) |
| :--- | :--- |
| **`gpt-oss-120b`** | Requires the Harmony chat template; raw chain-of-thought tokens are not intended for direct user consumption; high memory footprint if run unquantized. |
| **`gpt-oss-20b`** | Reduced accuracy on multi-step Olympiad-level mathematics and niche factual recall compared to 120B; requires `Reasoning: medium/high` to avoid premature answers. |
| **`Qwen 3.8 27B`** | Thinking mode is enabled by default (`xhigh`), generating high token volumes; static YaRN context scaling can affect short-text fluency; high presence penalty causes script drift. |
| **`Gemma 4 31B`** | No native audio encoder (text & vision only); previous turn reasoning traces must be stripped from multi-turn chat history to avoid prompt bloat. |
| **`Gemma 4 26B A4B`** | Long-context multi-needle retrieval (`MRCR v2`) drops to 44.1% (vs 66.4% on 31B Dense); all 25.2B weights must remain in RAM even though active compute is 3.8B per token. |
