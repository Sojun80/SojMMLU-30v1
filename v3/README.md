# SojMMLU-30 v3 — Linked Reasoning

Thirty original multi-step questions: six each in Code, Math, Logic, Science and Evidence, with two Linked, two Deep, and two Synthesis items in each category. Technical total is 18; General total is 12.

## Public benchmark policy

- `questions.json` contains **questions and choices only**, so it is safe to supply to tested models.
- The **V3 answer key is private** and intentionally not included in this repository. Do not publish full answer sheets or the correct letter mapping.
- The `run_benchmark.py --version v3` runner expects `v3/answer_key.json` **locally** for grading. An evaluator must supply that private file independently; a fresh clone intentionally cannot grade V3 by itself.
- Models can be tested with the questions-only file while preserving blind grading.
- Public [results](../results/README.md) include scores, missed question IDs, skips, runtime and hardware configurations but not correct answers.

V3 remains a fixed qualification screen: the strict first-pass bar is 30/30, no unanswered items and no wrong selected letters. Manual one-shot exam prompts should be distinguished from independent-question API testing.

**Note:** An answer key was briefly committed to the public repository on October 24, 2026, then removed. Its old GitHub commit remains reachable in history unless the repository history is explicitly rewritten; removing the current file is not sufficient to guarantee secrecy from anyone who accessed that commit.

This is an author-verified diagnostic benchmark, not a contamination-resistant or independently peer-reviewed assessment.
