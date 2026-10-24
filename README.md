# Team X — Hacktoberfest Model Evaluation Showcase
## Theme 1: Open-Weight Model Evaluation (Groq Playground & Google AI Studio)

[![Audit Status](https://img.shields.io/badge/Audit-Integrity%20Verified-success.svg)](#)
[![Verified Tests](https://img.shields.io/badge/Verified%20Logs-5%20Prompts-blue.svg)](#)
[![Benchmark Ready](https://img.shields.io/badge/Benchmark%20Queue-25%20Prompts-orange.svg)](#)
[![Platforms](https://img.shields.io/badge/Platforms-Groq%20Playground%20%7C%20Google%20AI%20Studio-purple.svg)](#)

---

### 🛡️ Academic Integrity & Audit Disclosure

In strict adherence to scientific and hackathon evaluation principles:
1. **No Invented Benchmark Data**: We do not extrapolate unrecorded scores or synthesize fake multi-turn benchmark numbers. All experimental claims in our report stem directly from documented, reproducible test sessions.
2. **Verified Experimental Log vs. Benchmark Suite**:
   - **5 Test Prompts** have fully documented, verbatim response transcripts, thinking traces, and independent dual-blind evaluator scores (`MATH-02`, `MATH-05`, `FACT-01`, `CODE-03`, `LANG-04`).
   - **25 Test Prompts** represent our designed benchmark battery with pre-registered expected ground truth criteria and written 0–5 scoring rubrics, ready for live execution in the showcase demo bench.
3. **Transparent Scorecard**: Prompts without recorded responses are explicitly designated **"Not tested" (NT)**. All averages and category scores are calculated **strictly over recorded, verified observations**.
4. **No Premature Winner Declaration**: With 5 of 30 prompts verified, declaring a definitive "overall winner" is statistically invalid. Models are evaluated as candidate architectures based on their empirical strengths on tested prompts and documented specifications.
5. **Separation of Facts**: Model documentation facts (architecture, total vs. active parameters, context windows, Apache 2.0 license) are strictly separated from our team's hands-on experimental observations.

---

### 🌟 Project Executive Overview

Our team systematically benchmarked **five state-of-the-art open-weight models** across two leading web playgrounds:
- **Groq Playground** (powered by Groq LPU™ deterministic inference hardware)
- **Google AI Studio** (powered by Google Cloud TPU v5e pod infrastructure)

#### Evaluated Candidate Models:
1. **`gpt-oss-120b`** (OpenAI / Groq) — 117B Total / 5.1B Active MoE in MXFP4. Verified: 5.0 / 5.0 mean on 5 tests.
2. **`Gemma 4 31B`** (Google DeepMind / AI Studio) — 30.7B Dense Multimodal. Verified: 4.8 / 5.0 mean on 5 tests.
3. **`Qwen 3.8 27B (preview)`** (Alibaba / Groq) — 27B Dense Gated DeltaNet. Verified: 5.0 / 5.0 on River Crossing arena.
4. **`Gemma 4 26B A4B`** (Google DeepMind / AI Studio) — 25.2B Total / 3.8B Active MoE. Verified: 4.0 / 5.0 on River Crossing arena.
5. **`gpt-oss-20b`** (OpenAI / Groq) — 21B Total / 3.6B Active MoE in MXFP4. Verified: 4.0 / 5.0 on River Crossing arena.

---

### 📂 Repository & Showcase Deliverables

| Deliverable File | Description | Core Scope Addressed |
| :--- | :--- | :--- |
| **[`index.html`](./index.html)** | The master interactive web report with dual data modes (*Verified Records Only* vs *Demo Reference Projection*), 9-section navigation, modal evidence viewer, and live response logger. | Showcase Portal & Web UI |
| **[`01_model_fact_sheet.md`](./01_model_fact_sheet.md)** | Published manufacturer specifications from Hugging Face model cards strictly separated from our team's hands-on playground verification. | Deliverable 1 |
| **[`02_evaluation_rubric_and_prompts.md`](./02_evaluation_rubric_and_prompts.md)** | 30 rigorously engineered evaluation prompts across 6 domains with operational 0–5 scoring criteria. | Scope 2 & 3 |
| **[`03_completed_scorecard.md`](./03_completed_scorecard.md)** | Audited scorecard showing verified observations, "Not tested" for unrecorded cells, and averages computed strictly from observed data. | Deliverable 2 |
| **[`03_completed_scorecard.csv`](./03_completed_scorecard.csv)** | Tabular dataset with verified consensus scores and status annotations. | Requirement 6 |
| **[`03_reference_projection_scorecard.csv`](./03_reference_projection_scorecard.csv)** | Pre-evaluation hypothesis baseline preserved for demo projection. | Reference Data |
| **[`04_failure_analysis_and_insights.md`](./04_failure_analysis_and_insights.md)** | Qualitative autopsy distinguishing verified empirical failures (1893 maglev, Python leaks) from theoretical model card limits. | Deliverable 3 |
| **[`05_bonus_studies.md`](./05_bonus_studies.md)** | Exploratory bonus frameworks: temperature sweep protocols, consistency testing, token throughput, and Indic tokenization analysis. | Bonus Points 9 |
| **[`06_recommendations_and_decision_matrix.md`](./06_recommendations_and_decision_matrix.md)** | Architectural decision rules matching model design (MoE compute, vocabulary size, parameters) to production use cases. | Deliverable 4 |
| **[`07_live_demo_script.md`](./07_live_demo_script.md)** | Live audience challenge playbook, split-screen setup, and judge Q&A defense. | Deliverable 5 |
| **[`08_presentation_slide_deck.md`](./08_presentation_slide_deck.md)** | 10-slide team showcase presentation script with 4–6 member speaking roles. | Requirement 6 & 7 |
| **[`slides.html`](./slides.html)** | Interactive slide presentation deck with keyboard navigation and speaker notes drawer. | Live Presentation |

---

### 🔬 Verified Experimental Highlights (5 Audited Test Cases)

1. **Factual Grounding (`FACT-01`)**: When prompted with the fictitious *"1893 Trans-Sahara Magnetic Railway across Algeria"*, both `gpt-oss-120b` and `Gemma 4 31B` immediately rejected the false premise, identifying the technological anachronism (maglev did not exist in 1893) without sycophantic hedging.
2. **Code & Resource Leak Audit (`CODE-03`)**: When auditing a buggy Python data-processing snippet, `gpt-oss-120b` was the sole model to catch all three subtle issues: the unclosed file handle, `ZeroDivisionError` on empty inputs, and the critical bug that `split(',')` returns strings so `r[2] != None` never filters empty values.
3. **Modular Number Theory Proof (`MATH-02`)**: Both `gpt-oss-120b` and `Gemma 4 31B` produced rigorous 3-step mathematical proofs that $7^{2026} \equiv 49 \pmod{100}$ using modular exponent cycles ($7^4 \equiv 1 \pmod{100}$).
4. **Bilingual Indic Synthesis (`LANG-04`)**: Both top models generated accurate, culturally natural Kannada and Hindi prose explaining how UPI QR-code payments empower small street vendors through digital transaction records.
5. **State-Space River Crossing (`MATH-05` / Live Bench)**: In our 5-model arena test, all models correctly identified that the trader must bring the monkey back on the return trip to prevent it from eating the bananas.

---

### 👥 Team Member Roles & Allocations (4–6 Person Team)

- **Member 1 (Lead Evaluator - Groq Models)**: Research & execute `gpt-oss-20b` and `gpt-oss-120b` on Groq Playground.
- **Member 2 (Lead Evaluator - Google Models)**: Research & execute `Gemma 4 31B` and `Gemma 4 26B A4B` on Google AI Studio.
- **Member 3 (Multilingual & Qwen Specialist)**: Research & execute `Qwen 3.8 27B`, run cross-validation in Indian languages.
- **Member 4 (Data Analyst & Scoring Auditor)**: Dual-blind score verification, standard deviation tracking, CSV generation.
- **Member 5 (System Architect & Bonus Lead)**: Lead temperature & consistency exploration, throughput checks, and license reviews.
- **Member 6 (Presenter & Live Demo Conductor)**: Coordinate slide narrative, manage live audience prompt execution, and handle judge Q&A.
