# 09 — Complete Evaluation Audit & Outstanding Test Checklist

## 1. Executive Summary of Evaluation Coverage

| Metric | Count | Percentage | Notes |
| :--- | :---: | :---: | :--- |
| **Total Planned Prompts** | `30` | `100%` | 6 categories × 5 prompts (`MATH`, `FACT`, `INST`, `CODE`, `LANG`, `SAFE`) |
| **Total Evaluated Models** | `5` | `100%` | `gpt-oss-120b`, `Gemma 4 31B`, `Qwen 3.8 27B`, `Gemma 4 26B A4B`, `gpt-oss-20b` |
| **Total Planned Model-Prompt Runs** | `150` | `100%` | 30 prompts × 5 models |
| **Completed & Verified Runs (Genuine Logs)** | `13` | `8.7%` | Stored verbatim with raw objective checks & dual-rater grades in `evaluation_results.json` |
| **Outstanding / Missing Runs (`Pending`)** | `137` | `91.3%` | Explicitly marked `Not tested` / `Pending` (zero fabricated scores) |

---

## 2. Per-Model Completion Audit (Verified Runs Only)

| Model | Platform | API Key Required | Completed Runs | Outstanding Runs | Verified Raw Sum | Verified Mean (1–5) | Normalized Verified Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **gpt-oss-120b** | Groq Playground | `GROQ_API_KEY` | `5 / 30` | `25 / 30` | `25 / 25` | **5.00 / 5.00** | **100.0%** |
| **Gemma 4 31B** | Google AI Studio | `GEMINI_API_KEY` | `5 / 30` | `25 / 30` | `24 / 25` | **4.80 / 5.00** | **96.0%** |
| **Qwen 3.8 27B** | Groq Playground | `GROQ_API_KEY` | `1 / 30` | `29 / 30` | `5 / 5` | **5.00 / 5.00** | **100.0%** |
| **Gemma 4 26B A4B** | Google AI Studio | `GEMINI_API_KEY` | `1 / 30` | `29 / 30` | `4 / 5` | **4.00 / 5.00** | **80.0%** |
| **gpt-oss-20b** | Groq Playground | `GROQ_API_KEY` | `1 / 30` | `29 / 30` | `4 / 5` | **4.00 / 5.00** | **80.0%** |

---

## 3. Per-Category Completion Audit

| Category | Prompts | `gpt-oss-120b` | `Gemma 4 31B` | `Qwen 3.8 27B` | `Gemma 4 26B A4B` | `gpt-oss-20b` | Completed Cells | Missing Cells |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Reasoning & Math** | 5 | `5.0/5` (2/5 run) | `5.0/5` (2/5 run) | `5.0/5` (1/5 run) | `4.0/5` (1/5 run) | `4.0/5` (1/5 run) | `7 / 25` | `18 / 25` |
| **Factual Accuracy** | 5 | `5.0/5` (1/5 run) | `5.0/5` (1/5 run) | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `2 / 25` | `23 / 25` |
| **Instruction Following** | 5 | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `0 / 25` | `25 / 25` |
| **Coding** | 5 | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `0 / 25` | `0 / 25` |
| **Indian Languages** | 5 | `5.0/5` (1/5 run) | `5.0/5` (1/5 run) | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `2 / 25` | `23 / 25` |
| **Safety** | 5 | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `Pending (0/5)` | `0 / 25` | `0 / 25` |

---

## 4. Prompt-by-Prompt Checklist (All 30 Planned Prompts × 5 Models = 150 Cells)

Legend: `[x] Verified (Score/5)` = Genuine response recorded & graded in `evaluation_results.json` · `[ ] Pending` = Outstanding test awaiting API or Playground execution.

| Prompt ID | Category | Title | `gpt-oss-120b` | `Gemma 4 31B` | `Qwen 3.8 27B` | `Gemma 4 26B A4B` | `gpt-oss-20b` | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `MATH-01` | Reasoning & Math | Warehouse Apple Arithmetic | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `MATH-02` | Reasoning & Math | Modular Arithmetic 7^2026 mod 100 | `[x] 5/5` | `[x] 5/5` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | **2/5 Partial** |
| `MATH-03` | Reasoning & Math | Farmer Sheep Lateral Logic | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `MATH-04` | Reasoning & Math | Bayesian Conditional Probability | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `MATH-05` | Reasoning & Math | Knights and Knaves Island / River Logic Trap | `[x] 5/5` | `[x] 5/5` | `[x] 5/5` | `[x] 4/5` | `[x] 4/5` | **5/5 Complete** |
| `FACT-01` | Factual Accuracy | 1893 Trans-Sahara Railway Trap | `[x] 5/5` | `[x] 5/5` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | **2/5 Partial** |
| `FACT-02` | Factual Accuracy | Rayleigh Scattering & Sky Color | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `FACT-03` | Factual Accuracy | TPU v5e vs Groq LPU Architecture | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `FACT-04` | Factual Accuracy | Indian Constitution Timeline & Leaders | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `FACT-05` | Factual Accuracy | Shakespeare Hamlet False Attribution | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `INST-01` | Instruction Following | Strict Raw JSON Extraction | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `INST-02` | Instruction Following | Length & Word Count Quantum Summary | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `INST-03` | Instruction Following | Perishable Goods Markdown Table | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `INST-04` | Instruction Following | Lipogram Paragraph without letter E | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `INST-05` | Instruction Following | Countries Ending in L & Verification | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `CODE-01` | Coding & Algorithms | Longest Palindromic Substring O(1) Space | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `CODE-02` | Coding & Algorithms | Thread-Safe In-Memory LRU Cache | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `CODE-03` | Coding & Algorithms | Bug Finding & Context Manager Leak | `[x] 5/5` | `[x] 4/5` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | **2/5 Partial** |
| `CODE-04` | Coding & Algorithms | SQL DENSE_RANK Department Salaries | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `CODE-05` | Coding & Algorithms | FastAPI Endpoint & Pydantic Validation | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `LANG-01` | Indian Languages | Hindi Cloud & Data Privacy Technical | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `LANG-02` | Indian Languages | Tamil Proverb & Literary Translation | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `LANG-03` | Indian Languages | Bengali Doctor Patient Clinical Dialogue | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `LANG-04` | Indian Languages | Kannada + Hindi UPI Empowerment (Verified) | `[x] 5/5` | `[x] 5/5` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | **2/5 Partial** |
| `LANG-05` | Indian Languages | Hinglish UPI Transaction Failed Support | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `SAFE-01` | Responsible AI | Open Source Licenses MIT GPL Apache | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `SAFE-02` | Responsible AI | Refusal of Auth Bypass Scraper | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `SAFE-03` | Responsible AI | Algorithmic Bias & Demographic Parity | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `SAFE-04` | Responsible AI | Medical Emergency Chest Pain Triage | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |
| `SAFE-05` | Responsible AI | Data Privacy & Aadhaar K-Anonymity | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | `[ ] Pending` | 0/5 Pending |

---

## 5. How to Execute Outstanding Tests (API Batch Runner or Interactive Playground Mode)

Because `GROQ_API_KEY` and `GEMINI_API_KEY` are not currently set in the local shell environment, we provide **two practical, zero-fabrication workflows** to execute the remaining 137 model-prompt cells:

### Option A: Automated API Execution (`run_evaluations.py --mode api`)
Export your free API keys from [GroqCloud Console](https://console.groq.com/keys) and [Google AI Studio](https://aistudio.google.com/app/apikey), then run:
```bash
export GROQ_API_KEY="gsk_your_groq_key_here"
export GEMINI_API_KEY="AIzaSy_your_google_ai_studio_key_here"

# Run all missing evaluations (or filter by --prompt MATH-01 or --model "Qwen 3.8 27B")
python3 run_evaluations.py --mode api

# Synchronize evaluation_results.json -> CSV scorecard, Markdown tables, index.html, and slides.html
python3 run_evaluations.py --sync
```

### Option B: Interactive Web Playground Assisted Runner (`run_evaluations.py --mode interactive` or Browser UI)
If you prefer running prompts directly inside the free web playgrounds ([Groq Playground](https://console.groq.com/playground) and [Google AI Studio](https://aistudio.google.com)):
1. **Via Browser Workbench (`index.html`):** Open `SEC 05 (Scorecard)`, click any `Pending` row, click **Record / Edit Live Response**, paste the verbatim model output, assign Rater 1 & Rater 2 scores, and click **Download `evaluation_results.json`** or **Download Active CSV**.
2. **Via Terminal Assisted CLI:** Run `python3 run_evaluations.py --mode interactive --prompt MATH-01` to print the standardized prompt package, paste the playground response, auto-compute objective constraint checks, record dual-rater scores, and sync all project files automatically.
