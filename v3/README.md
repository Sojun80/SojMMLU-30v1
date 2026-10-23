# SojMMLU-30 v3 — Linked Reasoning

30 original multi-step problems: six each in Code, Math, Logic, Science and Evidence. Each category has two Linked, two Deep, and two Synthesis questions. Technical total is 18; General total is 12.

Unlike v1 and v2, each problem requires several dependent calculations, state transitions, or decisions. Correct answer letters are evenly distributed: six A, six B, six C, six D, six E.

The complete verified questions and answer key are also available in the accompanying downloadable v3 bundle. `questions.json` is safe for model prompts; `answer_key.json` is evaluator-only. `verify.py` independently recomputes all 30 answer values using only Python's standard library (SQLite, exhaustive enumeration, dynamic programming, rational arithmetic, etc.).

Use `FRONTIER_PROMPT.md` for a fresh, blind frontier-model conversation. Do not provide the answer key to the model.

The runner supports `--version v3`; v1 remains the default. Each question is sent as an independent API request in local tests. Manual all-in-one chat scores should be labeled separately.

This is an author-verified benchmark, not an independently peer-reviewed psychometric evaluation. Preserve original answers, report per-category and per-tier scores, and investigate any item whose answer is disputed.
