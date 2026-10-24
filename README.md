# SojMMLU-30 v1 (SojBench-30)

A **30-question original MMLU-style model capability screen**, authored for repeatable local-LLM deployment and quantization comparisons. Not an official MMLU-Pro subset, not a public leaderboard score, and not a statistical estimate of general intelligence.

## What it measures

Five capability groups of **six items each**:

| Group | Questions | Basic | Applied | Stretch |
|---|---|---:|---:|---:|
| C — Code & algorithms | C01–C06 | 2 | 2 | 2 |
| M — Mathematics & quantitative reasoning | M01–M06 | 2 | 2 | 2 |
| L — Logic & constraint solving | L01–L06 | 2 | 2 | 2 |
| S — Science & engineering | S01–S06 | 2 | 2 | 2 |
| E — Reading, evidence & data interpretation | E01–E06 | 2 | 2 | 2 |
| **Total** | **30** | **10** | **10** | **10** |

Also report **technical reasoning** (C+M+L, /18), **general capability** (S+E, /12), and performance by difficulty (/10 each).

- **Smoke mode:** 10 basic questions, two from every group. Intended as a quick deployment sanity check, *not* proof of model intelligence.
- **Full mode:** all 30 items. Diagnostic profile for comparisons among the same models, endpoints, prompts and decoding settings.

## Files

- `questions.json`: 30 prompts, option letters, fixed IDs, and capability/difficulty labels; **no answers**.
- `answer_key.json`: answer letters and concise independently reviewable rationales; never include this in prompts.
- `run_benchmark.py`: OpenAI-compatible inference runner, strict answer parsing, raw-response capture, and capability matrix report.

## Reproducible protocol

1. Send each item as an **independent** conversation. No few-shot examples and no running shared context.
2. Preserve choices A–E, IDs, and question text. Use the same prompt template, temperature, and maximum generation budget across models.
3. Instruct model to finish with `ANSWER: A` through `ANSWER: E`. Grade the final selected letter only. Do not use arbitrary inherited stop sequences.
4. Save full model responses, request errors, `finish_reason`, token usage, elapsed time, and parsing errors.
5. Report exact-match accuracy and the failure status separately; **do not silently discard unanswered/truncated questions**.
6. Freeze v1 questions and key. If a defect is discovered, document it explicitly and release a new version or pre-declared excluded-item report; do not retroactively tune the key to favor a particular model.

## Running

Requires Python 3.10+ with the standard library (no pip packages).

```bash
python3 run_benchmark.py --endpoint http://127.0.0.1:8001/v1 --model YOUR_MODEL --subset smoke
python3 run_benchmark.py --endpoint http://127.0.0.1:8001/v1 --model YOUR_MODEL --subset full --output deepseek-full.json
```

The runner accepts `--max-tokens`, `--timeout`, and `--temperature` arguments. Use `--help` for options. Actual runtime varies greatly with model, hardware, and reasoning output.

## Score interpretation

A result like 27/30 with C=6/6 and E=3/6 differs from 27/30 with C=3/6 and E=6/6. Likewise, a quantized model maintaining Basic 10/10 while dropping Stretch 9/10 to 5/10 merits targeted analysis, but **one point is 3.33% overall and 16.67% within a domain**. Differences that small are not definitive.

## Limitations

- These 30 questions were authored and internally checked by one assistant, not externally psychometrically validated or blind-reviewed by multiple independent specialists. All answer choices were rebalanced so each of A–E occurs exactly **six** times as the correct answer.
- Published test questions and answers can eventually be memorized by trained or prompted systems. Treat results as local regression diagnostics, **not contamination-resistant benchmarks**.
- Multiple choice does not directly measure tool use, actual code execution, long-context reasoning, or instruction-following robustness. Pair with executable coding tests and IFEval when needed.
- Run the same stable prompt/parser setup for comparison. For quantizations, compare to a known high-precision baseline under identical conditions.

## Provenance

Original SojBench-30 v1 questions curated in this conversation; answer-key review included direct arithmetic/constraint verification for combinatorics items M05 and L06. They are not official MMLU or MMLU-Pro questions.

## Benchmark results

See the [published leaderboard and XTX performance comparisons](results/README.md). The V3 grading key is held privately and is not included in this repository.
