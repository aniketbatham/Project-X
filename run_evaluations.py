#!/usr/bin/env python3
"""
Hacktoberfest 2026 — Theme 1: Open Model Evaluation (Team X)
Evidence-Based Evaluation Runner, Objective Constraint Verifier & Artifact Synchronizer.

Supports:
  1. Audit status of all 30 prompts x 5 models = 150 test cells:
       python3 run_evaluations.py --audit
  2. Live API execution against Groq Cloud & Google AI Studio (zero fabrication):
       export GROQ_API_KEY="gsk_..."
       export GEMINI_API_KEY="AIzaSy..."
       python3 run_evaluations.py --mode api [--prompt MATH-01] [--model "Qwen 3.8 27B"]
  3. Interactive Web Playground paste-and-grade workflow (no API keys required):
       python3 run_evaluations.py --mode interactive [--prompt MATH-01] [--model "Qwen 3.8 27B"]
  4. Full artifact synchronization (updates CSV scorecard, Markdown scorecard, and HTML workbench):
       python3 run_evaluations.py --sync
"""

import argparse
import csv
import datetime
import json
import os
import re
import shutil
import sys
import time
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_JSON = os.path.join(ROOT_DIR, "evaluation_results.json")
CSV_SCORECARD = os.path.join(ROOT_DIR, "03_completed_scorecard.csv")
INDEX_HTML = os.path.join(ROOT_DIR, "index.html")
DASHBOARD_HTML = os.path.join(ROOT_DIR, "interactive_dashboard.html")

MODEL_API_CONFIG = {
    "gpt-oss-120b": {
        "provider": "groq",
        "env_key": "GROQ_API_KEY",
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "api_model": "openai/gpt-oss-120b",
        "playground_url": "https://console.groq.com/playground"
    },
    "gpt-oss-20b": {
        "provider": "groq",
        "env_key": "GROQ_API_KEY",
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "api_model": "openai/gpt-oss-20b",
        "playground_url": "https://console.groq.com/playground"
    },
    "Qwen 3.8 27B": {
        "provider": "groq",
        "env_key": "GROQ_API_KEY",
        "endpoint": "https://api.groq.com/openai/v1/chat/completions",
        "api_model": "qwen/qwen3.8-27b",
        "playground_url": "https://console.groq.com/playground"
    },
    "Gemma 4 31B": {
        "provider": "google",
        "env_key": "GEMINI_API_KEY",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent",
        "api_model": "gemma-4-31b-it",
        "playground_url": "https://aistudio.google.com"
    },
    "Gemma 4 26B A4B": {
        "provider": "google",
        "env_key": "GEMINI_API_KEY",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemma-4-26b-a4b-it:generateContent",
        "api_model": "gemma-4-26b-a4b-it",
        "playground_url": "https://aistudio.google.com"
    }
}


def compute_objective_observations(prompt_id, text):
    """Distinguishes raw programmatic observations from subjective rubric judgments."""
    lines = [l for l in text.splitlines() if l.strip()]
    words = len(text.split())
    chars = len(text)
    bullets = sum(1 for l in lines if l.strip().startswith(("•", "-", "*")))
    numbered = sum(1 for l in lines if re.match(r"^\d+[\.\)]", l.strip()))
    has_code = ("def " in text or "SELECT " in text or "```" in text)
    has_kn = any(0x0C80 <= ord(c) <= 0x0CFF for c in text)
    has_hi = any(0x0900 <= ord(c) <= 0x097F for c in text)
    has_ta = any(0x0B80 <= ord(c) <= 0x0BFF for c in text)
    has_bn = any(0x0980 <= ord(c) <= 0x09FF for c in text)
    has_te = any(0x0C00 <= ord(c) <= 0x0C7F for c in text)

    checks = {}
    if prompt_id == "INST-01":
        try:
            parsed_json = json.loads(text.strip())
            checks["valid_raw_json"] = isinstance(parsed_json, dict)
            checks["no_markdown_fences"] = ("```" not in text)
        except Exception:
            checks["valid_raw_json"] = False
            checks["no_markdown_fences"] = ("```" not in text)
    elif prompt_id == "INST-02":
        checks["word_count_in_80_100_range"] = (80 <= words <= 100)
    elif prompt_id == "INST-04":
        checks["zero_forbidden_letter_e"] = ("e" not in text.lower())
    elif prompt_id == "MATH-02":
        checks["mentions_remainder_49"] = ("49" in text)
        checks["shows_3_steps"] = (numbered >= 3)
    elif prompt_id == "MATH-05":
        checks["exact_4_bullets"] = (bullets == 4)
        checks["mentions_monkey_return_swap"] = ("monkey back" in text.lower() or "return" in text.lower())
    elif prompt_id == "FACT-01":
        checks["rejects_1893_maglev_premise"] = ("no " in text.lower() or "inaccurate" in text.lower() or "not exist" in text.lower())
        checks["cites_duponchel_1879"] = ("duponchel" in text.lower() or "1879" in text.lower())
    elif prompt_id == "CODE-03":
        checks["identifies_file_leak"] = ("with open" in text or "closed" in text.lower())
        checks["uses_valid_row_denominator"] = ("valid_count" in text)
    elif prompt_id == "LANG-04":
        checks["renders_kannada_script"] = has_kn
        checks["renders_hindi_devanagari"] = has_hi

    return {
        "char_count": chars,
        "word_count": words,
        "non_empty_lines": len(lines),
        "bullet_line_count": bullets,
        "numbered_item_count": numbered,
        "contains_code_syntax": has_code,
        "contains_kannada_unicode": has_kn,
        "contains_devanagari_unicode": has_hi,
        "contains_tamil_unicode": has_ta,
        "contains_bengali_unicode": has_bn,
        "contains_telugu_unicode": has_te,
        "automated_constraint_checks": checks
    }


def recalculate_aggregates(data):
    model_ids = [m["id"] for m in data["models"]]
    prompts = data["prompts"]
    completed_cells = 0
    missing_cells = 0

    by_model = {}
    for m_id in model_ids:
        scores = []
        for sp in prompts:
            sc = sp["evaluations"][m_id]["rubric_scoring"]["consensus_score"]
            if sc is not None and sp["evaluations"][m_id].get("raw_response") is not None:
                scores.append(sc)
                completed_cells += 1
            else:
                missing_cells += 1
        by_model[m_id] = {
            "completed_tests": len(scores),
            "pending_tests": len(prompts) - len(scores),
            "completion_rate_pct": round((len(scores) / float(len(prompts))) * 100, 1),
            "raw_points_sum": sum(scores) if scores else None,
            "max_possible_on_completed": len(scores) * 5,
            "mean_score_out_of_5": round(sum(scores) / len(scores), 2) if scores else None,
            "normalized_pct_on_completed": round((sum(scores) / (len(scores) * 5)) * 100, 1) if scores else None
        }

    categories = ["Reasoning & Math", "Factual Accuracy", "Instruction Following", "Coding", "Indian Languages", "Safety"]
    by_category = {}
    for cat in categories:
        cat_prompts = [sp for sp in prompts if sp["category"] == cat]
        cat_stats = {}
        for m_id in model_ids:
            scores = [
                sp["evaluations"][m_id]["rubric_scoring"]["consensus_score"]
                for sp in cat_prompts
                if sp["evaluations"][m_id]["rubric_scoring"]["consensus_score"] is not None
                and sp["evaluations"][m_id].get("raw_response") is not None
            ]
            cat_stats[m_id] = {
                "completed_in_category": len(scores),
                "pending_in_category": len(cat_prompts) - len(scores),
                "mean_score_out_of_5": round(sum(scores) / len(scores), 2) if scores else None,
                "normalized_pct": round((sum(scores) / (len(scores) * 5)) * 100, 1) if scores else None
            }
        by_category[cat] = cat_stats

    data["summary_counts"] = {
        "total_planned_prompts": len(prompts),
        "total_models": len(model_ids),
        "total_planned_cells": len(prompts) * len(model_ids),
        "completed_verified_cells": completed_cells,
        "outstanding_pending_cells": missing_cells,
        "completion_percentage": round((completed_cells / float(len(prompts) * len(model_ids))) * 100, 1)
    }
    data["aggregates_verified_only"] = {
        "by_model": by_model,
        "by_category": by_category
    }
    return data


def print_audit_report(data):
    recalculate_aggregates(data)
    sc = data["summary_counts"]
    print("=" * 84)
    print("HACKTOBERFEST 2026 — OPEN MODEL EVALUATION AUDIT REPORT")
    print("=" * 84)
    print(f"Total Planned Prompts          : {sc['total_planned_prompts']} across 6 categories")
    print(f"Total Models                   : {sc['total_models']} (3 on Groq Playground, 2 on Google AI Studio)")
    print(f"Total Planned Evaluation Cells : {sc['total_planned_cells']}")
    print(f"Verified Transcript Cells      : {sc['completed_verified_cells']} / 150 ({sc['completion_percentage']}%)")
    print(f"Incomplete (No Raw Transcript) : {sc['outstanding_pending_cells']} / 150 ({round(100 - sc['completion_percentage'], 1)}%)")
    print("-" * 84)
    print(f"{'Model':<18} | {'Verified':<8} | {'Missing':<8} | {'Verified Mean':<13} | {'30-Row Table Sum':<16} | {'API Key Env'}")
    print("-" * 84)
    tsv_totals = data.get("user_submitted_30_prompt_scorecard", {}).get("by_model", {})
    for m in data["models"]:
        mid = m["id"]
        st = data["aggregates_verified_only"]["by_model"][mid]
        cfg = MODEL_API_CONFIG[mid]
        env_present = "SET" if os.environ.get(cfg["env_key"]) else f"MISSING ({cfg['env_key']})"
        mean_str = f"{st['mean_score_out_of_5']:.2f}/5 ({st['normalized_pct_on_completed']}%)" if st["mean_score_out_of_5"] is not None else "N/A"
        t_info = tsv_totals.get(mid, {})
        t_str = f"{t_info.get('raw_sum', '-')}/150 ({t_info.get('pct', '-')}%)"
        print(f"{mid:<18} | {st['completed_tests']:>2}/30    | {st['pending_tests']:>2}/30    | {mean_str:<13} | {t_str:<16} | {env_present}")
    print("=" * 84)


def call_model_api(model_id, system_prompt, user_prompt, temperature=0.2, top_p=0.95, max_tokens=2048):
    cfg = MODEL_API_CONFIG[model_id]
    api_key = os.environ.get(cfg["env_key"])
    if not api_key:
        raise RuntimeError(f"Environment variable {cfg['env_key']} is not set for {model_id}.")

    t0 = time.time()
    if cfg["provider"] == "groq":
        payload = {
            "model": cfg["api_model"],
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens
        }
        req = urllib.request.Request(
            cfg["endpoint"],
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        elapsed = round(time.time() - t0, 3)
        msg = body["choices"][0]["message"]
        text = msg.get("content", "")
        think = msg.get("reasoning", "") or ""
        return {"text": text, "think": think, "latency_sec": elapsed}
    else:
        url = f"{cfg['endpoint']}?key={api_key}"
        payload = {
            "systemInstruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generationConfig": {
                "temperature": temperature,
                "topP": top_p,
                "maxOutputTokens": max_tokens
            }
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        elapsed = round(time.time() - t0, 3)
        parts = body["candidates"][0]["content"]["parts"]
        text = "\n".join(p.get("text", "") for p in parts)
        return {"text": text, "think": "", "latency_sec": elapsed}


def sync_all_artifacts(data):
    recalculate_aggregates(data)
    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    model_ids = ["gpt-oss-120b", "Gemma 4 31B", "Qwen 3.8 27B", "Gemma 4 26B A4B", "gpt-oss-20b"]
    with open(CSV_SCORECARD, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Prompt_ID", "Category", "Prompt_Title", "Verification_Status",
            "gpt-oss-120b_Groq", "Gemma-4-31B_AIStudio", "Qwen-3.8-27B_Groq",
            "Gemma-4-26B-A4B_AIStudio", "gpt-oss-20b_Groq", "Evaluator_Notes"
        ])
        for sp in data["prompts"]:
            scores = [
                sp["evaluations"][m]["rubric_scoring"]["consensus_score"]
                if sp["evaluations"][m].get("raw_response") is not None else None
                for m in model_ids
            ]
            done_cnt = sum(1 for s in scores if s is not None)
            status = "Verified (5/5 Models)" if done_cnt == 5 else (f"Partial Pilot ({done_cnt}/5 Models)" if done_cnt > 0 else "Not tested")
            row_vals = [str(s) if s is not None else "Not tested" for s in scores]
            notes = []
            for m in model_ids:
                n = sp["evaluations"][m]["rubric_scoring"].get("subjective_evaluator_notes")
                if scores[model_ids.index(m)] is not None and n:
                    notes.append(f"{m}: {n}")
            note_str = " | ".join(notes) if notes else "Pending live playground transcript capture."
            writer.writerow([sp["prompt_id"], sp["category"], sp["title"], status] + row_vals + [note_str])

    new_v_map = {}
    for sp in data["prompts"]:
        pid = sp["prompt_id"]
        for m in model_ids:
            ev = sp["evaluations"][m]
            sc = ev["rubric_scoring"]["consensus_score"]
            if sc is not None and ev.get("raw_response"):
                new_v_map.setdefault(pid, {})[m] = {
                    "think": ev["raw_response"].get("reasoning_trace", ""),
                    "text": ev["raw_response"].get("output_text", ""),
                    "r1": ev["rubric_scoring"].get("rater_1", sc),
                    "r2": ev["rubric_scoring"].get("rater_2", sc),
                    "consensus": sc,
                    "notes": ev["rubric_scoring"].get("subjective_evaluator_notes", "")
                }

    if os.path.exists(INDEX_HTML):
        with open(INDEX_HTML, "r", encoding="utf-8") as f:
            html = f.read()
        v_json_str = json.dumps(new_v_map, indent=6, ensure_ascii=False)
        replacement = "const verifiedResponsesData = " + v_json_str + ";\n\n    let currentDataMode"
        html_updated = re.sub(
            r"const verifiedResponsesData = \{.*?\};\s*let currentDataMode",
            lambda _: replacement,
            html,
            flags=re.S
        )
        with open(INDEX_HTML, "w", encoding="utf-8") as f:
            f.write(html_updated)
        shutil.copyfile(INDEX_HTML, DASHBOARD_HTML)

    print(f"[SYNC COMPLETE] Updated {RESULTS_JSON}, {CSV_SCORECARD}, {INDEX_HTML}, and {DASHBOARD_HTML}")


def run_interactive_mode(data, filter_prompt=None, filter_model=None):
    sys_prompt = data["standardized_protocol"]["system_prompt"]
    model_ids = [m["id"] for m in data["models"]]
    for sp in data["prompts"]:
        pid = sp["prompt_id"]
        if filter_prompt and pid != filter_prompt:
            continue
        for mid in model_ids:
            if filter_model and mid != filter_model:
                continue
            ev = sp["evaluations"][mid]
            if ev.get("raw_response") is not None and ev["rubric_scoring"]["consensus_score"] is not None:
                continue
            print("=" * 72)
            print(f"OUTSTANDING TEST: {pid} ({sp['title']}) on {mid}")
            print(f"Platform: {MODEL_API_CONFIG[mid]['playground_url']} | Temp: 0.2")
            print("-" * 72)
            print(f"SYSTEM PROMPT:\n{sys_prompt}\n")
            print(f"USER PROMPT:\n{sp['prompt_text']}\n")
            print(f"RUBRIC CRITERIA:\n{sp['rubric_criteria']}")
            print("=" * 72)
            ans = input("Paste response now? [y = paste / s = skip / q = quit]: ").strip().lower()
            if ans == "q":
                sync_all_artifacts(data)
                return
            if ans != "y":
                continue
            print("Paste the verbatim model response below. Type EOF on a new line when finished:")
            lines = []
            while True:
                line = sys.stdin.readline()
                if not line or line.strip() == "EOF":
                    break
                lines.append(line.rstrip("\n"))
            resp_text = "\n".join(lines).strip()
            if not resp_text:
                print("Empty response skipped.")
                continue
            obs = compute_objective_observations(pid, resp_text)
            print(f"Objective Observations: {json.dumps(obs, ensure_ascii=False)}")
            r1 = int(input("Enter Rater 1 Score (1-5): ").strip())
            r2 = int(input("Enter Rater 2 Score (1-5): ").strip())
            consensus = round((r1 + r2) / 2.0, 1)
            if consensus.is_integer():
                consensus = int(consensus)
            notes = input("Enter Evaluator Justification Note: ").strip()
            ev["status"] = "completed_verified"
            ev["execution_source"] = "interactive_playground_session"
            ev["timestamp_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            ev["raw_response"] = {"reasoning_trace": "", "output_text": resp_text}
            ev["objective_observations"] = obs
            ev["rubric_scoring"] = {
                "scale": "1-5",
                "rater_1": r1,
                "rater_2": r2,
                "consensus_score": consensus,
                "subjective_evaluator_notes": notes
            }
            sync_all_artifacts(data)


def run_api_mode(data, filter_prompt=None, filter_model=None):
    sys_prompt = data["standardized_protocol"]["system_prompt"]
    model_ids = [m["id"] for m in data["models"]]
    missing_keys = set()
    for mid in model_ids:
        if filter_model and mid != filter_model:
            continue
        env_k = MODEL_API_CONFIG[mid]["env_key"]
        if not os.environ.get(env_k):
            missing_keys.add(f"{env_k} (for {mid})")
    if missing_keys:
        print("[API CREDENTIALS REQUIRED]")
        print("Cannot run live API queries without the following environment variables:")
        for mk in sorted(missing_keys):
            print(f"  - {mk}")
        print("\nTo run via API, export your keys first:")
        print("  export GROQ_API_KEY='gsk_...'")
        print("  export GEMINI_API_KEY='AIzaSy...'")
        print("Or use '--mode interactive' to paste genuine responses from the free web playgrounds.")
        sys.exit(1)

    for sp in data["prompts"]:
        pid = sp["prompt_id"]
        if filter_prompt and pid != filter_prompt:
            continue
        for mid in model_ids:
            if filter_model and mid != filter_model:
                continue
            ev = sp["evaluations"][mid]
            if ev.get("raw_response") is not None and ev["rubric_scoring"]["consensus_score"] is not None:
                continue
            print(f"Executing {pid} on {mid} via {MODEL_API_CONFIG[mid]['provider']} API (Temp=0.2)...")
            res = call_model_api(mid, sys_prompt, sp["prompt_text"])
            obs = compute_objective_observations(pid, res["text"])
            ev["status"] = "response_captured_awaiting_dual_rater_score"
            ev["execution_source"] = f"{MODEL_API_CONFIG[mid]['provider']}_api"
            ev["timestamp_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            ev["raw_response"] = {"reasoning_trace": res["think"], "output_text": res["text"]}
            ev["objective_observations"] = obs
            print(f"  -> Captured {obs['word_count']} words in {res['latency_sec']}s. Objective checks: {obs['automated_constraint_checks']}")
            sync_all_artifacts(data)


def main():
    parser = argparse.ArgumentParser(description="Team X Open Model Evaluation Runner & Synchronizer")
    parser.add_argument("--audit", action="store_true", help="Print full completion audit of the 30x5 matrix")
    parser.add_argument("--mode", choices=["api", "interactive"], help="Execute missing tests via API or interactive CLI")
    parser.add_argument("--prompt", help="Filter to a specific Prompt ID (e.g., MATH-01)")
    parser.add_argument("--model", help="Filter to a specific Model ID (e.g., 'Qwen 3.8 27B')")
    parser.add_argument("--sync", action="store_true", help="Synchronize evaluation_results.json to CSV and HTML files")
    args = parser.parse_args()

    with open(RESULTS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.sync:
        sync_all_artifacts(data)
    if args.mode == "api":
        run_api_mode(data, args.prompt, args.model)
    elif args.mode == "interactive":
        run_interactive_mode(data, args.prompt, args.model)
    else:
        print_audit_report(data)


if __name__ == "__main__":
    main()
