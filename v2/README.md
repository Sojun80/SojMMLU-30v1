# SojMMLU-30 v2 · Challenge screen

**30 new, original, harder multiple-choice questions.** V1 remains unchanged as our fast smoke test. V2 is intended to reveal *capability* differences that V1's repeated perfect scores could not.

## The scoring matrix

| Domain | Moderate | Hard | Challenge | Total |
|---|---:|---:|---:|---:|
| C · Code & algorithms | 2 | 2 | 2 | 6 |
| M · Mathematics & quantitative reasoning | 2 | 2 | 2 | 6 |
| L · Logic & constraint solving | 2 | 2 | 2 | 6 |
| S · Science & engineering | 2 | 2 | 2 | 6 |
| E · Reading, evidence & interpretation | 2 | 2 | 2 | 6 |
| **Total** | **10** | **10** | **10** | **30** |

Also report **technical reasoning /18** (C+M+L), **general capability /12** (S+E), and scores by difficulty /10. Every correct answer is worth exactly one point.

## Files

- [FRONTIER_PROMPT.md](FRONTIER_PROMPT.md) — all 30 questions **without answers**, ready to paste into a fresh ChatGPT/Claude/Gemini conversation.
- [questions.json](questions.json) — machine-readable question IDs, text, 5 choices, and domain/tier labels, **without answers**.
- [answer_key.json](answer_key.json) — answer letters and explanations; **never paste into model prompts**.

V2 uses the same root runner as V1 with `--version v2`. If the GitHub copy of the runner does not yet support that flag, use the runner in the latest main branch.

```bash
python3 run_benchmark.py --version v2 --endpoint http://127.0.0.1:8001/v1 --model YOUR_MODEL --subset full --output sojmmlu-v2-result.json
```

The full run sends **30 isolated requests**, stores responses, failures, timings and usage, and grades by key. `--subset smoke` selects the 10 moderate questions; V1 is preferable for routine smoke tests.

### Manual zero-cost frontier runs

1. Start a **fresh** chat with the target model.
2. Paste **only** `FRONTIER_PROMPT.md`; never paste the answer key or the repo's root README.
3. Ask for ID-to-letter JSON only. Grade against `answer_key.json` afterward.
4. Label manual all-at-once chat results separately from 30 isolated API calls; their contexts and reasoning budgets differ.

## Validation and interpretation

These 30 questions have deterministic scoring, with **exactly six correct answers for each letter A–E**. The construction was checked for five independent answer choices per item and an even matrix. Specific quantitative and logic questions were independently enumerated or calculated, including the 4,096 cyclic bit strings, the 11-step paths, all 720 constrained permutations, the truth-teller assignments, conditional probability, expected costs, and shortest directed paths with one discount coupon.

**Important:** The initial validation is by the benchmark author plus computational spot-checks, not by an independent panel. If blind model answers expose a genuine question defect, isolate and document it publicly rather than silently altering the key. Do not tune the exam after observing GPT-5 Mini's score. A six-question category changes 16.7 percentage points per miss; report per-item errors as well as percentages.

V2 is **not** official MMLU/MMLU-Pro, is not contamination-resistant once published, and cannot prove universal model rankings. It is a fixed, interpretable local-LLM diagnostic screen.
