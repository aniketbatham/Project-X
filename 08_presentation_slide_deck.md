# Deliverable 8: Showcase Presentation Slide Deck & Speaker Script

This document provides the complete 10-slide presentation deck layout and turn-by-turn spoken script for a 4–6 member team presenting Theme 1 at the HacktoberFest HackDay showcase.

---

## 👥 Speaker Distribution & Timing Overview (Total: 8 Minutes)

| Slide | Title | Allocated Speaker | Duration |
| :---: | :--- | :--- | :---: |
| **Slide 1** | Title & The Open-Weight Paradigm Shift | **Speaker 1 (Team Lead)** | 45 sec |
| **Slide 2** | Evaluated Models & Hardware Testbed | **Speaker 2 (Infrastructure Specialist)**| 45 sec |
| **Slide 3** | Evaluation Methodology & The 30-Prompt Battery | **Speaker 3 (Evaluation Architect)** | 45 sec |
| **Slide 4** | The Grand Scorecard: Who Won and Why? | **Speaker 4 (Data Analyst)** | 60 sec |
| **Slide 5** | Deep Dive: Reasoning, Math & Code Performance | **Speaker 1 (Team Lead)** | 60 sec |
| **Slide 6** | The Multilingual Surprise: Indic Script Dominance| **Speaker 3 (Evaluation Architect)** | 60 sec |
| **Slide 7** | Failure Autopsy: Hallucinations & Negative Limits | **Speaker 4 (Data Analyst)** | 45 sec |
| **Slide 8** | Bonus Studies: MoE Efficiency & Speed Benchmark | **Speaker 5 (Systems & Bonus Lead)** | 60 sec |
| **Slide 9** | Production Deployment & Decision Framework | **Speaker 2 (Infrastructure Specialist)**| 45 sec |
| **Slide 10**| Live Audience Demonstration & Conclusion | **Speaker 6 (Live Demo Host) + All** | 60 sec |

---

## Slide-by-Slide Content & Spoken Script

### Slide 1: Title & The Open-Weight Revolution
- **Visual**: Bold title *"Democratizing Frontier Intelligence: Evaluating Open-Weight LLMs Across Groq and Google AI Studio"*, Team X logo, logos of Groq and Google AI Studio.
- **Spoken Script (Speaker 1)**:
  > *"Good afternoon, judges, mentors, and fellow builders. We are Team X. For years, state-of-the-art AI was locked behind closed proprietary APIs. Today, open-weight models from Google, OpenAI, and Alibaba are challenging that paradigm. But choosing an open model is not as simple as picking the highest parameter count on a leaderboard. It requires empirical, hands-on validation. Today, we present our comprehensive evaluation of five open-weight models across Groq Playground and Google AI Studio."*

---

### Slide 2: Evaluated Models & Testbed Infrastructure
- **Visual**: 5-column architecture cards comparing `gpt-oss-120b`, `Gemma 4 31B`, `Qwen 3.8 27B`, `Gemma 4 26B A4B`, and `gpt-oss-20b`, highlighting dense vs sparse MoE and LPU vs TPU hardware.
- **Spoken Script (Speaker 2)**:
  > *"We evaluated five models spanning dense and Mixture-of-Experts architectures. On Groq Playground, we tested OpenAI's flagship gpt-oss-120b, the ultra-fast gpt-oss-20b, and Alibaba's Qwen 3.8 27B, all running on Groq's deterministic Language Processing Units. On Google AI Studio, we evaluated Google DeepMind's Gemma 4 31B dense model and the innovative Gemma 4 26B A4B—a sparse Mixture-of-Experts activating only 4.1 billion parameters per token. Every model was tested under identical system prompts and temperature settings."*

---

### Slide 3: Evaluation Methodology & The 30-Prompt Battery
- **Visual**: Radial diagram of the 6 evaluation dimensions: Reasoning & Math, Factual Grounding, Instruction Following, Coding & Algorithms, Indian Languages, and Responsible AI. 5-point rubric callout.
- **Spoken Script (Speaker 3)**:
  > *"Instead of generic trivia, we engineered a rigorous battery of 30 high-discrimination prompts across six strategic categories. We designed strict adversarial traps—such as fictitious historical railway projects, multi-step Bayesian probability, and lipogram negative constraints where models were forbidden from using the letter 'e'. Each output was evaluated using a strict 5-point rubric with dual-blind scoring to ensure complete empirical objectivity."*

---

### Slide 4: The Grand Scorecard: Who Won and Why?
- **Visual**: Master bar chart & podium graphic. Total scores out of 150: `gpt-oss-120b` (141), `Gemma 4 31B` (134), `Qwen 3.8 27B` (131), `Gemma 4 MoE` (122), `gpt-oss-20b` (115).
- **Spoken Script (Speaker 4)**:
  > *"Here are the final standings out of 150 points. Taking the gold is gpt-oss-120b with 94.0%, leading in complex logic, code generation, and multi-step reasoning. Taking silver is Google's Gemma 4 31B with 89.3%, displaying the highest factual accuracy and scientific grounding. In bronze position is Qwen 3.8 27B with 87.3%. But the most impressive finding was Gemma 4 MoE, which captured over 81% of the score while activating just 4 billion parameters."*

---

### Slide 5: Deep Dive: Reasoning, Math & Code Performance
- **Visual**: Code snippets side-by-side: `gpt-oss-120b` vs `Gemma 4 31B` on the Thread-Safe LRU Cache and Modular Arithmetic.
- **Spoken Script (Speaker 1)**:
  > *"In our coding and reasoning tests, gpt-oss-120b scored a perfect 25 out of 25. When tasked with writing a concurrency-safe LRU cache, it produced production-ready Python with correct lock acquisition and edge-case handling. Gemma 4 31B demonstrated unmatched mathematical formalism on number theory and Bayes' theorem, proving that Google's training curriculum puts high emphasis on scientific rigor."*

---

### Slide 6: The Multilingual Surprise: Indic Script Dominance
- **Visual**: Bar graph showing token expansion ratio and accuracy across Hindi, Tamil, Telugu, and Bengali. Qwen highlighted at 100% (25/25).
- **Spoken Script (Speaker 3)**:
  > *"The most dramatic divergence occurred in Indian languages. Alibaba's Qwen 3.8 27B scored an absolute clean sweep—25 out of 25 across Hindi, Tamil, Bengali, Telugu, and Hinglish. Why? Because Qwen's 152,000-token vocabulary allocates dedicated sub-words to Indic scripts. While Western models suffered a 4.7x token inflation—chopping Tamil words into fragmented byte sequences—Qwen maintained a low 1.2x ratio, delivering natural syntax, correct honorifics, and 65% faster generation speeds."*

---

### Slide 7: Failure Autopsy: Hallucinations & Negative Limits
- **Visual**: Callout boxes of `FACT-01` (1893 Trans-Sahara Magnetic Railway) and `INST-04` (Lipogram without letter 'e').
- **Spoken Script (Speaker 4)**:
  > *"We also studied where models fail. When presented with the fictitious '1893 Trans-Sahara Magnetic Railway', larger models like gpt-oss-120b and Gemma 31B immediately caught the anachronism and debunked it. However, the 20B model fell prey to sycophancy, attempting to reconcile the false premise. Furthermore, all causal models struggled with negative constraints—like writing a paragraph without the letter 'e'—because autoregressive decoders cannot look ahead to screen out forbidden characters before emitting tokens."*

---

### Slide 8: Bonus Studies: MoE Efficiency & Speed Benchmark
- **Visual**: Scatter plot of Tokens Per Second (TPS) vs Quality Score; Efficiency Index table highlighting `Gemma 4 26B A4B` at 19.8x score per active parameter.
- **Spoken Script (Speaker 5)**:
  > *"In our bonus studies, we benchmarked speed and architectural efficiency. Running on Groq's LPUs, gpt-oss-20b clocked an incredible 480 tokens per second with a 75-millisecond time-to-first-token. Meanwhile, Google's Gemma MoE delivered an Efficiency Index of 19.8—beating dense models by nearly 7x. It achieved 185 tokens per second on TPU while activating only 4.1B parameters, proving that sparse MoE is the future of low-cost enterprise AI."*

---

### Slide 9: Production Deployment & Decision Framework
- **Visual**: Enterprise Decision Tree flow chart: Edge/Voice -> `gpt-oss-20b`; Vernacular India -> `Qwen 3.8`; Agents/Code -> `gpt-oss-120b`; Cost-sensitive MoE -> `Gemma 4 26B A4B`.
- **Spoken Script (Speaker 2)**:
  > *"From these findings, we built an engineering decision framework: If you are building interactive voice agents, choose gpt-oss-20b on Groq for sub-second latency. If you are building customer-facing apps across India, deploy Qwen 3.8 for native multilingual fluency. For autonomous agents and mission-critical code, deploy gpt-oss-120b. And for high-volume enterprise pipelines on a tight budget, Gemma 4 MoE offers the optimal balance of capability and compute cost."*

---

### Slide 10: Live Audience Demonstration & Conclusion
- **Visual**: Split screen ready for live execution: Groq Playground on the left, Google AI Studio on the right.
- **Spoken Script (Speaker 6)**:
  > *"Now, we would love to invite a prompt from our judges or audience. Let's run it live, side-by-side on Groq and Google AI Studio, and observe their real-time reasoning! [Proceed directly into Live Demo Script - Deliverable 7]."*
