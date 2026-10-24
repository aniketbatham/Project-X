# Team X — Hacktoberfest 2026 Model Evaluation Showcase
## Theme 1: Open-Weight Model Evaluation (Groq Playground & Google AI Studio)

[![Evaluation Status](https://img.shields.io/badge/Evaluation-Complete-success.svg)](#)
[![Prompts Evaluated](https://img.shields.io/badge/Prompts-30%20(6%20Categories)-blue.svg)](#)
[![Platforms](https://img.shields.io/badge/Platforms-Groq%20Playground%20%7C%20Google%20AI%20Studio-orange.svg)](#)
[![License](https://img.shields.io/badge/Models%20License-Apache%202.0-brightgreen.svg)](#)

---

### 🌟 Project Executive Overview

This repository and interactive web application represent Team X's complete deliverable for **Theme 1: Open Model Evaluation** at **Hacktoberfest 2026**.

Our 4–6 member team systematically researched and benchmarked **five open-weight models** across **Groq Playground** (`console.groq.com/playground`) and **Google AI Studio** (`aistudio.google.com`), combining official Hugging Face model card documentation with 30 rigorous hands-on test prompts:

| Model | Developer | Platform | Architecture (from Official Model Card) | Context | License | Model Card |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`gpt-oss-120b`** | OpenAI | Groq Playground | **117B Total / 5.1B Active MoE** (MXFP4, Harmony format) | 128K | Apache 2.0 | [hf.co/openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| **`gpt-oss-20b`** | OpenAI | Groq Playground | **21B Total / 3.6B Active MoE** (MXFP4, fits 16GB RAM) | 128K | Apache 2.0 | [hf.co/openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) |
| **`Qwen 3.8 27B (preview)`** | Alibaba | Groq Playground | **27B Dense VLM** (`16×(3×Gated DeltaNet → 1×Gated Attn)`) | 262K (1M YaRN) | Apache 2.0 | [hf.co/Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) |
| **`Gemma 4 31B`** | Google | Google AI Studio | **30.7B Dense Multimodal** (Hybrid Local/Global p-RoPE) | 256K | Apache 2.0 | [hf.co/google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) |
| **`Gemma 4 26B A4B`** | Google | Google AI Studio | **25.2B Total / 3.8B Active MoE** (8/128 routed + 1 shared) | 256K | Apache 2.0 | [hf.co/google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) |

---

### 🌐 Interactive Website & Deliverables

- **[`index.html`](./index.html)** / **[`interactive_dashboard.html`](./interactive_dashboard.html)**: Full-featured interactive web application containing:
  1. **Executive Overview, Key Terms Glossary & Fair Testing Protocol**
  2. **Model Fact Sheet & Architecture Comparison Matrix** (with direct links to Hugging Face model cards & arXiv technical papers)
  3. **Evaluation Rubric & 30-Prompt Explorer** (across Reasoning & Math, Factual Accuracy, Instruction Following, Coding, Indian Languages, and Safety)
  4. **Interactive Completed Scorecard & Deep Response Inspector** (inspect exact model outputs, Rater A & Rater B scores, ground truth, Radar & Speed charts, and CSV export)
  5. **Failure Analysis & Model Card Correlation** (forensic breakdown of sycophancy, lipogram BPE constraint leaks, Indic tokenizer inflation, and MoE long-context drift)
  6. **All 6 Bonus Studies Lab** (Temperature/Thinking Settings Simulator, Pass@3 Consistency Study, Speed vs. Active Parameter Efficiency, LMArena & Published Benchmark Comparison, Apache 2.0 License Review, and 6-Language Indic Evaluation including Kannada, Hindi, Tamil, Telugu, Bengali, and Hinglish)
  7. **Interactive Application Recommendation Engine & TCO Calculator**
  8. **Live Demonstration Arena** (side-by-side real-time streaming comparison simulator + custom audience prompt launcher & live dual-rater scorecard calculator)
- **[`slides.html`](./slides.html)**: Interactive 10-slide stage presentation deck with keyboard navigation, fullscreen mode, speaker scripts, and embedded charts.
- **Markdown & CSV Documentation**:
  - [`01_model_fact_sheet.md`](./01_model_fact_sheet.md)
  - [`02_evaluation_rubric_and_prompts.md`](./02_evaluation_rubric_and_prompts.md)
  - [`03_completed_scorecard.md`](./03_completed_scorecard.md) & [`03_completed_scorecard.csv`](./03_completed_scorecard.csv)
  - [`04_failure_analysis_and_insights.md`](./04_failure_analysis_and_insights.md)
  - [`05_bonus_studies.md`](./05_bonus_studies.md)
  - [`06_recommendations_and_decision_matrix.md`](./06_recommendations_and_decision_matrix.md)
  - [`07_live_demo_script.md`](./07_live_demo_script.md)
  - [`08_presentation_slide_deck.md`](./08_presentation_slide_deck.md)
