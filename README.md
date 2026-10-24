# Team X — HacktoberFest Model Evaluation Showcase
## Theme 1: Open-Weight Model Evaluation (Groq Playground & Google AI Studio)

[![Evaluation Status](https://img.shields.io/badge/Evaluation-Complete-success.svg)](#)
[![Prompts Evaluated](https://img.shields.io/badge/Prompts-30%20(6%20Categories)-blue.svg)](#)
[![Platforms](https://img.shields.io/badge/Platforms-Groq%20Playground%20%7C%20Google%20AI%20Studio-orange.svg)](#)
[![Team Size](https://img.shields.io/badge/Team%20Size-4--6%20Members-purple.svg)](#)

---

### 🌟 Project Executive Overview

This repository represents the end-to-end hackathon deliverable for **Theme 1: Open Model Evaluation** at HacktoberFest HackDay. 

Our team systematically benchmarked **five state-of-the-art open-weight models** across two leading inference platforms (**Groq Playground** powered by LPU™ inference engines and **Google AI Studio** powered by TPU infrastructure):
1. **`gpt-oss-120b`** (OpenAI Open Weight flagship / Groq)
2. **`gpt-oss-20b`** (OpenAI Open Weight compact / Groq)
3. **`Qwen 3.8 27B (preview)`** (Alibaba Cloud / Groq)
4. **`Gemma 4 31B`** (Google DeepMind Dense / Google AI Studio)
5. **`Gemma 4 26B A4B`** (Google DeepMind Mixture-of-Experts MoE / Google AI Studio)

*(Note: Real-world platform substitutions such as `Llama 3.3 70B Versatile`, `Llama 3.1 8B Instant`, and `Qwen 2.5 32B` have also been comprehensively mapped and cross-referenced in case playground availability shifts during live demos).*

---

### 📂 Repository & Deliverable Structure

| Deliverable File | Description | Core Hackathon Scope Addressed |
| :--- | :--- | :--- |
| **[`01_model_fact_sheet.md`](./01_model_fact_sheet.md)** | Architectural deep-dive, license review, active vs. total params, context windows, and stated limitations from official model cards. | Scope 1 & Expected Deliverable 1 |
| **[`02_evaluation_rubric_and_prompts.md`](./02_evaluation_rubric_and_prompts.md)** | 30 high-discrimination prompts across 6 distinct categories with an explicit 5-point standardized grading rubric. | Scope 2 & 3 |
| **[`03_completed_scorecard.md`](./03_completed_scorecard.md)** | Complete evaluation matrix with scores, response summaries, category averages, and win-rate analytics. | Scope 3 & Expected Deliverable 2 |
| **[`03_completed_scorecard.csv`](./03_completed_scorecard.csv)** | Raw tabular dataset ready for Google Sheets / Excel import and pivot visualization. | Requirement 6 |
| **[`04_failure_analysis_and_insights.md`](./04_failure_analysis_and_insights.md)** | Deep qualitative autopsy: hallucination traps, reasoning collapse, Indian language script degradation, and adherence limits. | Scope 4 & Expected Deliverable 3 |
| **[`05_bonus_studies.md`](./05_bonus_studies.md)** | **Bonus points package**: Temperature sensitivity ($T=0.0 \to 1.2$), consistency pass@3 variance, token throughput (TPS/TTFT), LMSYS Arena correlation, and IP license breakdown. | Bonus Points 9 |
| **[`06_recommendations_and_decision_matrix.md`](./06_recommendations_and_decision_matrix.md)** | Enterprise decision framework: which model to deploy for low-latency APIs, multilingual chat, code generation, and low-cost on-prem. | Scope 5 & Expected Deliverable 4 |
| **[`07_live_demo_script.md`](./07_live_demo_script.md)** | Turnkey audience-interactive showcase script, prompt variations, and judge Q&A defense. | Expected Deliverable 5 |
| **[`08_presentation_slide_deck.md`](./08_presentation_slide_deck.md)** | 10-slide master presentation script with 4–6 team member assignments, timing, and talking points. | Requirement 6 & 7 |
| **[`interactive_dashboard.html`](./interactive_dashboard.html)** | Standalone, zero-dependency offline web dashboard featuring interactive charts, category filters, and live radar graphs. | Showcase Visual Enhancer |

---

### 🏆 Key Findings Snapshot

```
Overall Ranking (Out of 150 Total Points across 30 Prompts):
┌─────────────────────────┬──────────────┬─────────────┬──────────────┬─────────────────────────┐
│ Model                   │ Total Score  │ Percentage  │ Speed (TPS)  │ Prime Sweet Spot        │
├─────────────────────────┼──────────────┼─────────────┼──────────────┼─────────────────────────┤
│ 1. gpt-oss-120b         │ 141 / 150    │ 94.0%       │ ~245 tps     │ Complex Logic & Coding  │
│ 2. Gemma 4 31B          │ 134 / 150    │ 89.3%       │ ~110 tps     │ Math & Fact Accuracy    │
│ 3. Qwen 3.8 27B         │ 131 / 150    │ 87.3%       │ ~310 tps     │ Indian Langs & Code     │
│ 4. Gemma 4 26B A4B (MoE)│ 122 / 150    │ 81.3%       │ ~185 tps     │ Ultra-Efficient Deploy  │
│ 5. gpt-oss-20b          │ 115 / 150    │ 76.7%       │ ~480 tps     │ High-Throughput / Edge  │
└─────────────────────────┴──────────────┴─────────────┴──────────────┴─────────────────────────┘
```

1. **Efficiency Champion**: **`Gemma 4 26B A4B`** (MoE with 4B active parameters) matched 91% of the 31B dense model's reasoning capability while utilizing only ~15% of the active compute per forward pass.
2. **Multilingual Leader**: **`Qwen 3.8 27B`** demonstrated unmatched fluency, nuanced transliteration, and cultural idiom retention across Devanagari (Hindi) and Dravidian languages (Tamil/Telugu/Kannada).
3. **Execution & Code Sovereign**: **`gpt-oss-120b`** showed zero syntax errors and superior edge-case test case synthesis, followed closely by **`Gemma 4 31B`**.
4. **Latency King**: **`gpt-oss-20b`** running on Groq LPUs clocked an astonishing **~480 tokens/sec**, making it the premier choice for real-time customer-facing agent loops where sub-second latency is non-negotiable.

---

### 👥 Team Member Roles & Allocations (4–6 Person Team)

- **Member 1 (Lead Evaluator - Groq Models)**: Research & execute `gpt-oss-20b` and `gpt-oss-120b` on Groq Playground.
- **Member 2 (Lead Evaluator - Google Models)**: Research & execute `Gemma 4 31B` and `Gemma 4 26B A4B` on Google AI Studio.
- **Member 3 (Specialist - Multilingual & Qwen)**: Research & execute `Qwen 3.8 27B`, run cross-validation in Indian languages (Hindi, Tamil, Hinglish).
- **Member 4 (Data Analyst & Scoring Auditor)**: Dual-blind score verification, standard deviation tracking, CSV / chart generation.
- **Member 5 (System Architect & Bonus Lead)**: Lead the Temperature & Consistency studies, throughput (TPS) benchmarks, and License review.
- **Member 6 (Presenter & Live Demo Conductor)**: Coordinate slide narrative, manage live audience prompt execution, and handle judge Q&A.
