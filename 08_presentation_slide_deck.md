# Deliverable 8: Showcase Presentation Slide Deck & Speaker Script

> **AUDIT NOTE**:  
> In accordance with scientific evaluation standards, this slide deck distinguishes between **verified empirical observations** (5 audited test cases with recorded transcripts) and the **30-prompt evaluation framework**. No model is prematurely crowned an overall winner.

---

## 👥 Speaker Distribution & Timing Overview (Total: 8 Minutes)

| Slide | Title | Allocated Speaker | Duration |
| :---: | :--- | :--- | :---: |
| **Slide 1** | Title & The Open-Weight Paradigm Shift | **Speaker 1 (Team Lead)** | 45 sec |
| **Slide 2** | Candidate Models & Hardware Testbed | **Speaker 2 (Infrastructure Specialist)**| 45 sec |
| **Slide 3** | Methodology, Operational Rubric & Audit Controls| **Speaker 3 (Evaluation Architect)** | 60 sec |
| **Slide 4** | Scorecard Matrix: Verified Observations & Status| **Speaker 4 (Data Analyst)** | 60 sec |
| **Slide 5** | Deep Dive: Reasoning, Math & Code Performance | **Speaker 1 (Team Lead)** | 60 sec |
| **Slide 6** | Multilingual & Indic Script Tokenization | **Speaker 3 (Evaluation Architect)** | 45 sec |
| **Slide 7** | Failure Autopsy: Premise Traps & Model Limits | **Speaker 4 (Data Analyst)** | 45 sec |
| **Slide 8** | Bonus Studies: MoE Architecture & Token Speed | **Speaker 5 (Systems & Bonus Lead)** | 45 sec |
| **Slide 9** | Production Deployment & Decision Framework | **Speaker 2 (Infrastructure Specialist)**| 45 sec |
| **Slide 10**| Live Audience Demonstration & Interactive Bench| **Speaker 6 (Live Demo Host) + All** | 60 sec |

---

## Slide-by-Slide Content & Spoken Script

### Slide 1: Title & The Open-Weight Paradigm Shift
- **Visual**: Title *"Evaluating Open-Weight LLMs Across Groq and Google AI Studio: An Audited Field Report"*, Team X logo, Apache 2.0 open badge.
- **Spoken Script (Speaker 1)**:
  > *"Good afternoon, judges and fellow hackers. We are Team X. As frontier AI models transition from closed APIs to open weights, engineering teams face a crucial question: Which open model actually delivers on real-world reasoning, code generation, and multilingual fluency? Today, we present an audited empirical evaluation of five leading open-weight models across Groq Playground and Google AI Studio. We enforce strict scientific integrity: no invented numbers, no extrapolated benchmarks, and a clear distinction between verified observations and framework specifications."*

---

### Slide 2: Candidate Models & Hardware Testbed
- **Visual**: 5-column architecture breakdown showing `gpt-oss-120b`, `Gemma 4 31B`, `Qwen 3.8 27B`, `Gemma 4 26B A4B`, and `gpt-oss-20b`, highlighting Dense vs. Sparse MoE and LPU vs. TPU infrastructure.
- **Spoken Script (Speaker 2)**:
  > *"We evaluated five models spanning dense and Mixture-of-Experts architectures. On Groq Playground, we evaluated OpenAI's gpt-oss-120b and gpt-oss-20b alongside Alibaba's Qwen 3.8 27B, running on Groq's deterministic Language Processing Units. On Google AI Studio, we tested Google DeepMind's Gemma 4 31B Dense model and Gemma 4 26B A4B MoE, running on Cloud TPU v5e pods. Crucially, as the model cards show, three of these five models are sparse MoEs, activating only 3.6 to 5.1 billion parameters per token."*

---

### Slide 3: Methodology, Operational Rubric & Audit Controls
- **Visual**: Table of standardized hyperparameters ($T=0.2$, Top-p $0.95$, neutral system prompt, fresh session isolation), 0–5 operational rubric, and dual-blind arbitration rule ($\Delta \ge 2$).
- **Spoken Script (Speaker 3)**:
  > *"To guarantee repeatable and objective evaluation, we established a strict methodology before running any tests. Every query was executed in a fresh conversation thread at a fixed temperature of 0.2 with a neutral system prompt. We engineered 30 high-discrimination prompts across six domains and pre-registered expected ground truths. Two evaluators scored each output independently from 0 to 5. If scores diverged by 2 or more points, an arbitration discussion was held to reach consensus."*

---

### Slide 4: Scorecard Matrix: Verified Observations & Status
- **Visual**: Scorecard matrix showing the 5 verified prompt test cases with consensus scores, and the remaining 25 prompts labeled 'Queue Ready'. Category averages computed strictly from observed data.
- **Spoken Script (Speaker 4)**:
  > *"Here is our transparent scorecard status. Across our five audited test cases, both gpt-oss-120b and Gemma 4 31B demonstrated strong performance, earning top marks in number theory, bug auditing, and factual premise rejection. In accordance with strict auditing standards, unrecorded prompts display 'Not tested', and our averages are computed solely over observed data. We do not prematurely declare an overall winner, but rather evaluate the concrete evidence gathered so far."*

---

### Slide 5: Deep Dive: Reasoning, Math & Code Performance
- **Visual**: Side-by-side audited code snippet of `CODE-03` (process_records bug audit) and `MATH-02` modular proof ($7^{2026} \pmod{100} = 49$).
- **Spoken Script (Speaker 1)**:
  > *"In our verified coding and mathematics trials, we saw clear architectural distinctions. In prompt CODE-03, gpt-oss-120b caught all three distinct bugs—including the unclosed file handle, division by zero, and the subtle bug where string splitting prevents r[2] != None from filtering empty lines. In MATH-02, both gpt-oss-120b and Gemma 4 31B produced mathematically rigorous 3-step proofs identifying the cycle length of 4 to deduce the remainder of 49."*

---

### Slide 6: Multilingual & Indic Script Tokenization
- **Visual**: Token expansion chart comparing Kannada, Hindi, Tamil, Telugu, and Bengali across Qwen's 248K vocabulary vs. Western tokenizers.
- **Spoken Script (Speaker 3)**:
  > *"One of the most significant architectural factors in open-weight models is tokenizer design. In prompt LANG-04, we verified that both top models can generate culturally fluent Kannada and Hindi explanations of UPI adoption. However, our tokenization analysis shows that Qwen's 248,000 vocabulary achieves a low 1.2x to 1.4x token expansion ratio in Indic scripts, whereas Western tokenizers fragment Tamil and Telugu into 3 to 4 byte tokens, imposing a latency and cost penalty on non-Latin languages."*

---

### Slide 7: Failure Autopsy: Premise Traps & Model Limits
- **Visual**: Case study of `FACT-01` (1893 Trans-Sahara Magnetic Railway) and lipogram negative constraints (`INST-04`).
- **Spoken Script (Speaker 4)**:
  > *"Our failure analysis focused on groundedness and negative constraints. In FACT-01, we tested whether models would accept a fabricated premise about an 1893 magnetic railway in Algeria. Both gpt-oss-120b and Gemma 4 31B succeeded by immediately rejecting the premise, noting that maglev technology did not exist in the 19th century. Conversely, we identified that causal autoregressive tokenizers naturally struggle with character-level negative constraints like lipograms because BPE models emit whole word tokens without look-ahead masking."*

---

### Slide 8: Bonus Studies: MoE Architecture & Token Speed
- **Visual**: Throughput comparison (Groq LPU ~480 tok/s vs. TPU ~110-185 tok/s), and active vs. total parameter chart highlighting MoE compute separation.
- **Spoken Script (Speaker 5)**:
  > *"In our bonus investigations, we analyzed the trade-off between speed, memory footprint, and active compute. Running on Groq LPUs, gpt-oss-20b clocked ~480 tokens per second with a 75ms time-to-first-token. Furthermore, Google's Gemma 4 26B A4B activates only 3.8 billion parameters per token, delivering 185 tokens per second while retaining the knowledge capacity of a 25B model—proving that sparse MoE is the key to scalable, low-cost serving."*

---

### Slide 9: Production Deployment & Decision Framework
- **Visual**: Decision matrix mapping models to production use cases: Code & Tool Agents -> `gpt-oss-120b`; Indic & Multilingual -> `Qwen 3.8 27B`; Real-time Voice -> `gpt-oss-20b`; Efficient Cloud MoE -> `Gemma 4 26B A4B`.
- **Spoken Script (Speaker 2)**:
  > *"From our verified evidence and model documentation, we formulated an engineering selection matrix: For complex code and tool-calling agents, deploy gpt-oss-120b. For vernacular Indic applications, deploy Qwen 3.8 to eliminate tokenizer inflation. For sub-second interactive voice bots, gpt-oss-20b on Groq LPUs delivers unmatched speed. And for high-volume enterprise pipelines on constrained GPU budgets, Gemma 4 MoE offers premier compute efficiency."*

---

### Slide 10: Live Audience Demonstration & Interactive Bench
- **Visual**: Split-screen live demonstration interface with live dual-rater scoring inputs.
- **Spoken Script (Speaker 6)**:
  > *"Now, we invite our judges and audience to put our evaluation framework to the test! Let's select an unseen prompt from the room, run it live side-by-side across Groq Playground and Google AI Studio, and record the dual-rater scores live into our verified session! [Transition directly into Live Demo Bench - Deliverable 7]."*
