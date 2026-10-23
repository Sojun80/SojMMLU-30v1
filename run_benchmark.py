#!/usr/bin/env python3
"""SojMMLU-30 v1: dependency-free OpenAI-compatible benchmark runner."""
import argparse
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATTERN = re.compile(r"(?im)^\s*ANSWER\s*:\s*([A-E])\s*$")
SYSTEM = "Solve the multiple-choice question carefully. Your final line must be exactly ANSWER: X, where X is one of A, B, C, D, E. Do not append anything after the final line."

def request(url, payload, token, timeout):
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))

def grade(records, keys):
    groups = {g: {"correct": 0, "total": 0, "answered": 0, "errors": 0} for g in "CMLSE"}
    tiers = {t: {"correct": 0, "total": 0, "answered": 0, "errors": 0} for t in ("basic", "applied", "stretch")}
    for r in records:
        correct = r["answer"] == keys[r["id"]]["answer"]
        for d in (groups[r["domain"]], tiers[r["tier"]]):
            d["total"] += 1
            d["correct"] += int(correct)
            d["answered"] += int(r["answer"] is not None)
            d["errors"] += int(bool(r["error"]))
        r["correct"] = correct
    return {"overall": {"correct": sum(x["correct"] for x in groups.values()), "total": len(records), "answered": sum(x["answered"] for x in groups.values()), "errors": sum(x["errors"] for x in groups.values())}, "groups": groups, "tiers": tiers, "technical": {"correct": sum(groups[g]["correct"] for g in "CML"), "total": sum(groups[g]["total"] for g in "CML")}, "general": {"correct": sum(groups[g]["correct"] for g in "SE"), "total": sum(groups[g]["total"] for g in "SE")}}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--endpoint", default="http://127.0.0.1:8001/v1")
    ap.add_argument("--model", required=True)
    ap.add_argument("--subset", choices=("smoke", "full"), default="full")
    ap.add_argument("--output", default="sojmmlu-results.json")
    ap.add_argument("--max-tokens", type=int, default=4096)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--timeout", type=float, default=120.0)
    ap.add_argument("--api-key", default="")
    args = ap.parse_args()
    questions = json.loads((HERE / "questions.json").read_text())["questions"]
    keys = json.loads((HERE / "answer_key.json").read_text())["answers"]
    if args.subset == "smoke":
        questions = [q for q in questions if q["tier"] == "basic"]
    records = []
    t0 = time.monotonic()
    for q in questions:
        prompt = q["question"] + "\n\n" + "\n".join(k + ". " + v for k, v in q["choices"].items())
        payload = {"model": args.model, "temperature": args.temperature, "max_tokens": args.max_tokens, "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}]}
        started = time.monotonic()
        rec = {"id": q["id"], "domain": q["domain"], "tier": q["tier"], "answer": None, "finish_reason": None, "usage": None, "response": None, "error": None}
        try:
            obj = request(args.endpoint.rstrip("/") + "/chat/completions", payload, args.api_key, args.timeout)
            choice = obj["choices"][0]
            content = choice.get("message", {}).get("content") or ""
            rec["response"] = choice.get("message")
            rec["finish_reason"] = choice.get("finish_reason")
            rec["usage"] = obj.get("usage")
            matches = PATTERN.findall(content)
            if rec["finish_reason"] == "length":
                rec["error"] = "truncated"
            elif len(matches) != 1:
                rec["error"] = "missing_or_multiple_answer_markers"
            else:
                rec["answer"] = matches[0].upper()
        except (urllib.error.URLError, ValueError, KeyError, IndexError, TimeoutError) as e:
            rec["error"] = str(e)
        rec["elapsed_seconds"] = round(time.monotonic() - started, 3)
        records.append(rec)
        print(f'{q["id"]}: {rec["answer"] or "-"} ({rec["error"] or "ok"}; {rec["elapsed_seconds"]:.1f}s)', flush=True)
    summary = grade(records, keys)
    report = {"benchmark": "SojMMLU-30v1", "model": args.model, "endpoint": args.endpoint, "subset": args.subset, "temperature": args.temperature, "max_tokens": args.max_tokens, "total_elapsed_seconds": round(time.monotonic() - t0, 3), "summary": summary, "records": records}
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    print("Saved:", args.output)

if __name__ == "__main__":
    main()
