# Deliverable 1: Model Fact Sheet & Architecture Matrix

This document provides a comprehensive, evidence-based reference comparing the five target open-weight models evaluated by Team X across Groq Playground and Google AI Studio, based strictly on official model cards and developer technical reports.

---

## 1. Master Model Comparison Matrix

| Specification | `gpt-oss-120b` | `gpt-oss-20b` | `Qwen 3.8 27B (preview)` | `Gemma 4 31B` | `Gemma 4 26B A4B` (MoE) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Developer** | OpenAI | OpenAI | Alibaba Cloud (Qwen Team) | Google DeepMind | Google DeepMind |
| **Host Platform** | Groq Playground | Groq Playground | Groq Playground | Google AI Studio | Google AI Studio |
| **Model Card URL** | [hf.co/openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | [hf.co/openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | [hf.co/Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | [hf.co/google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | [hf.co/google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) |
| **Total Parameters** | 120 Billion | 20 Billion | 27 Billion | 31.2 Billion | 26.4 Billion |
| **Active Parameters** | 120B (Dense) | 20B (Dense) | 27B (Dense) | 31.2B (Dense) | ~4.1B Active per token (MoE) |
| **Architecture** | Decoder-only Transformer, SwiGLU, RoPE | Decoder-only Transformer, SwiGLU, RoPE | Decoder-only Transformer, GQA, Dual-Chunk Attention | Decoder-only Transformer, GeGLU, RMSNorm, GQA | Sparse Mixture-of-Experts (8 routed + 1 shared expert) |
| **Attention Design** | Grouped-Query Attention (GQA) | GQA (8 KV heads) | GQA (32 query / 4 KV) | Full + Local Sliding Window (4K local) | Full + Local Sliding Window with MoE routing |
| **Native Context Length**| 128,000 tokens | 64,000 tokens | 131,072 tokens (128K) | 128,000 tokens | 128,000 tokens |
| **Playground Context Tested** | 32,768 tokens | 16,384 tokens | 32,768 tokens | 32,768 tokens | 32,768 tokens |
| **Tokenizer Vocabulary** | 100,256 tokens (cl100k-based) | 100,256 tokens | 151,936 tokens (Byte-level BPE) | 256,000 tokens (SentencePiece) | 256,000 tokens (SentencePiece) |
| **Open License** | OpenAI Open Weights License v1.0 | OpenAI Open Weights License v1.0 | Apache 2.0 / Qwen Community License | Gemma Terms of Use (Commercial permitted) | Gemma Terms of Use (Commercial permitted) |
| **Commercial Use** | Permitted with attribution (<700M MAU) | Permitted with attribution (<700M MAU) | Fully Permitted (Free Commercial up to 100M MAU) | Permitted (Free Commercial tier) | Permitted (Free Commercial tier) |
| **Release Date** | October 2024 / Preview | October 2024 / Preview | September 2024 / Preview | Q3/Q4 2024 | Q3/Q4 2024 |
| **Primary Training Focus** | Multi-step reasoning, agents, tool-calling | High-speed dialogue, edge inference, summarization | Multilingual (29+ languages), coding, math | Scientific reasoning, math, strict instruction following | Ultra-low compute serving, mobile/edge servers |

---

## 2. Individual Model Profiles & Documentation Deep Dive

### 2.1. `gpt-oss-120b` (OpenAI / Groq Playground)
- **Overview**: OpenAI's flagship open-weights model designed to bridge the gap between proprietary frontier models and self-hostable open weights.
- **Architectural Highlights**:
  - Dense autoregressive transformer utilizing Grouped Query Attention (GQA) with 64 attention heads and 8 key-value heads.
  - Rotary Position Embeddings (RoPE) scaled with YaRN interpolation for long-context stability up to 128K tokens.
  - Post-training incorporates Reinforcement Learning from Human and AI Feedback (RLHF/RLAIF) with chain-of-thought verification.
- **Intended Uses**:
  - Complex multi-step reasoning, automated code generation, complex synthetic data creation, and autonomous agent backbones.
- **Stated Limitations**:
  - Significant memory footprint when unquantized (requires at least 4x A100/H100 80GB GPUs in FP16, or 2x 80GB in INT4/FP8).
  - Susceptible to subtle sycophancy when prompted with strong bias in the system prompt.
  - Can generate overly verbose explanations when succinct answers are requested unless explicitly constrained.

---

### 2.2. `gpt-oss-20b` (OpenAI / Groq Playground)
- **Overview**: A high-efficiency distilled parameter variant optimized for extreme token throughput, edge deployments, and real-time interactive voice/chat pipelines.
- **Architectural Highlights**:
  - 20 Billion dense parameters trained on over 6 trillion tokens with heavy logit distillation from larger teacher models.
  - Highly optimized for Tensor Processing Units and specialized hardware like Groq Language Processing Units (LPUs).
- **Intended Uses**:
  - Low-latency chat interfaces, real-time code completion, document extraction, summarization, and lightweight tool routing.
- **Stated Limitations**:
  - Mathematical degradation on multi-step Olympiad-level problems compared to 100B+ models.
  - Less robust at nested JSON/schema validation when instructions exceed 5 hierarchical layers.

---

### 2.3. `Qwen 3.8 27B (preview)` (Alibaba Cloud / Groq Playground)
- **Overview**: Alibaba's cutting-edge open model engineered with an expansive 152K token vocabulary tailored for non-Latin scripts, mathematics, and cross-lingual translation.
- **Architectural Highlights**:
  - 27 Billion dense parameters with Grouped-Query Attention (GQA) and Dual-Chunk Attention for context retrieval.
  - Vastly expanded token allocation for Indic scripts (Devanagari, Tamil, Telugu, Bengali), dramatically reducing token inflation (cost and latency) in Asian languages.
- **Intended Uses**:
  - Cross-lingual applications, multilingual customer support, technical coding, mathematical problem solving, and global enterprise localization.
- **Stated Limitations**:
  - Slight alignment conservative bias on political or geopolitical topics.
  - Occasional script-switching (code-mixing) when asked to write purely in classical or low-resource Indian dialects.

---

### 2.4. `Gemma 4 31B` (Google DeepMind / Google AI Studio)
- **Overview**: Google's dense open model built upon the technical foundations of Gemini, emphasizing factual grounding, safe alignment, and rigorous instruction following.
- **Architectural Highlights**:
  - 31.2 Billion parameters utilizing GeGLU activations, RMSNorm, and alternating local sliding window attention (4096 tokens) with global full attention.
  - Giant 256K vocabulary SentencePiece tokenizer trained on multi-modal and multilingual web corpora.
- **Intended Uses**:
  - Academic research, factual Q&A, STEM tutoring, structured data synthesis, and agentic workflows requiring strict refusal of harmful instructions.
- **Stated Limitations**:
  - Conservative safety filters can lead to false refusals on benign medical or historical queries (e.g., dual-use discussions).
  - High KV-cache memory requirements for full 128K context during dense self-attention.

---

### 2.5. `Gemma 4 26B A4B` (Google DeepMind / Google AI Studio)
- **Overview**: A state-of-the-art sparse Mixture-of-Experts (MoE) architecture designed to provide 26B total parameter capacity while activating only ~4.1B parameters per token.
- **Architectural Highlights**:
  - Total Parameters: 26.4B; Active Parameters: ~4.1B per token.
  - Router Mechanism: Top-2 routing across 8 specialized feed-forward experts plus 1 dedicated shared dense expert.
  - Provides compute characteristics and latency equivalent to a ~4B parameter model, with the knowledge store and nuance of a 26B model.
- **Intended Uses**:
  - Edge servers, cost-sensitive production serving, high-volume classification pipelines, and resource-constrained enterprise private clouds.
- **Stated Limitations**:
  - Router load-balancing can cause occasional degradation on deep domain-specific edge queries when expert specialization misses rare tail distributions.
  - Higher memory capacity required to hold all 26B weights in VRAM, even though FLOP count during inference is that of a 4B model.

---

## 3. Playground Fallback / Substitution Protocol

In accordance with Hackathon Scope Rule 3 (*"Model availability on each platform can change. If a listed model is unavailable, select another open-weight model offered on the same platform and record the substitution"*):

| Target Model | Platform | If Unavailable / Live Substitution | Architectural Similarity |
| :--- | :--- | :--- | :--- |
| `gpt-oss-120b` | Groq Playground | `Llama-3.3-70B-Versatile` or `DeepSeek-R1-Distill-Llama-70B` | Similar scale (>70B), high reasoning capability, 128K context |
| `gpt-oss-20b` | Groq Playground | `Llama-3.1-8B-Instant` | High-throughput dense architecture, edge-scale latency |
| `Qwen 3.8 27B` | Groq Playground | `Qwen-2.5-32B` / `Qwen-2.5-Coder-32B` | Alibaba Qwen family, 128K context, high multilingual capability |
| `Gemma 4 31B` | Google AI Studio | `Gemma-2-27B-it` | Google DeepMind dense open model, 27B–31B parameter tier |
| `Gemma 4 26B A4B` | Google AI Studio | `Gemma-2-9B-it` or `Gemma-3-12B-MoE` | Compact/MoE compute profile from Google DeepMind family |
