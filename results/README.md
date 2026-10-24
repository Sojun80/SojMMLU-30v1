# SojMMLU benchmark results

Results snapshot: **2026-10-24**.

## Qualification protocol

- **V1 — "Are you broken?"** Thirty basic-to-stretch questions: a smoke test for model, quantization, and inference setup.
- **V3 — "Are you good enough to proceed?"** Thirty linked/deep/synthesis questions. The *strict* bar is **30/30 first-pass, zero mistakes, zero skips**.
- A model can eventually reach 30/30 yet fail the first-pass gate. We always retain **first-pass correctness and omissions**, separately from eventual results.
- A wrong selected letter counts wrong even if its explanation contains the correct numerical solution. Incorrect answers are distinct from omissions; unknown first-pass status is marked unknown, not assumed zero.
- V1/V3 are narrow, original diagnostic screens—not claims about general intelligence or real-world agent competence. Some manual all-in-one prompts and independent-request runner tests are not directly equivalent.

## V3 model results

| Model / variant | Final | First-pass correct | First-pass skips | Known wrong / unanswered IDs |
|---|---:|---:|---:|---|
| Composer 2.5 | 30/30 | 30/30 | 0 | — |
| GPT-5 Mini | 30/30 | 30/30 | 0 | — |
| DeepSeek V4.1 Flash (local) | 30/30 | 30/30 | 0 | — |
| Swift 1.5 27B dense — XTX Vulkan | 30/30 | 30/30 | 0 | — |
| Swift 1.5 IQ3_S — XTX Strata HIP | 30/30 | 30/30 | 0 | — |
| Qwen IQ3_S — XTX Strata HIP | 30/30 | 30/30 | 0 | — |
| Gemini 2.5 Flash | 30/30 | 18/30 | 12 | — |
| Minio 2.6 Flash (as named in submission) | 30/30 | not recorded | not recorded | — |
| Qwen IQ2_XS — XTX Strata HIP | 29/30 | 29/30 | 0 | M06 |
| Nemotron (exact variant unverified) | 29/30 | 29/30 | 0 | E05 |
| Claude Sonnet 4.6 Thinking | 29/30 | 29/30 | 0 | S01 |
| GLM 5.2 High | 29/30 | 29/30 | 0 | L06 |
| Terra Light | 29/30 | 29/30 | 1 | unanswered: S04 |
| GLM 5.3 Flash — OpenCode Free | 29/30 | not recorded | not recorded | C05 |
| Flint Free | 28/30 | not recorded | not recorded | C06, E03 |
| Claude Haiku 4.5 | 27/30 | 27/30 | 0 | M05, L01, L05 |
| GPT-OSS 120B | 25/30 | 24/30 | 1 | C03, C06, M05, M06, L05 |
| Big Pickle | 19/30 | 1/30 | 29 | M03, M04, L01, L03, L05, L06, S02, S04, S06, E01, E06 |
| Beam Medium | 14/30 | 14/30 | 0 | C04, C06, M03, M04, M05, M06, L02, L03, L05, L06, S01, S04, S05, E03, E04, E06 |

### Notable failure profiles

- **Gemini 2.5 Flash:** 18 correct and 12 skipped on its first response; supplied the remaining 12 correctly in a follow-up. Eventual 30/30, but **not** a first-pass qualification.
- **Big Pickle:** one question answered initially (C01), **29 initial skips**. The final 30-answer submission scored 19/30.
- **GPT-OSS 120B:** initial One omitted logic item was subsequently answered correctly. Eventual 25/30.
- **Claude Sonnet 4.6 Thinking (S01) and GLM 5.2 High (L06):** explanations computed the correct values but selected the inconsistent answer labels. Strictly 29/30.
- **GLM 5.3 Flash via OpenCode Free:** C05 found a minimum cost but undercounted optimal paths.
- **Terra Light:** S04 reported a value inconsistent with the options and abstained from choosing a letter.
- **OpenCode Free:** the user observed recurrent difficulty obtaining final answers from multiple models. Complete submitted sheets are archived, but the initial delivery/skip status for some is unknown.
- **Beam Medium:** roughly four seconds reported for the 30-answer submission, 14/30 correct. Treat this speed as anecdotal, not controlled throughput.

## XTX measurements

RX 7900 XTX 24 GiB; native Strata CLI 0.2.2/engine 0.1.47 HIP. All three native Strata variants passed **V1 30/30**.

### Native Strata HIP (RX 7900 XTX)

| Variant | V1 | V1 runtime | V1 decode | V3 | V3 runtime | V3 decode |
|---|---:|---:|---:|---:|---:|---:|
| Qwen IQ2_XS | 30/30 | 158.2 s | 99.4 tok/s | 29/30 (M06) | 19m 15s | 109.2 tok/s |
| Swift 1.5 IQ3_S | 30/30 | 222.5 s | 49.1 tok/s | **30/30** | **18m 16s** | 55.0 tok/s |
| Qwen IQ3_S | 30/30 | 235.8 s | 49.2 tok/s | **30/30** | 20m 16s | 53.1 tok/s |

### Dense Swift 1.5 Qwen3.8-27B / RX 7900 XTX

| Path | V1 | V1 runtime | Decode |
|---|---:|---:|---:|
| Direct llama.cpp Vulkan | 29/30 (L04) | 127.318 s | 80.03 tok/s |
| Strata CLI → llama.cpp Vulkan | 29/30 (L04) | 128.368 s | 80.96 tok/s |
| llama.cpp HIP/ROCm | 29/30 (L04) | ~170 s | ~62.2 tok/s |
| vLLM ROCm, conservative mode | 29/30 (L04) | ~547 s | ~25 tok/s |

The **dense Vulkan V3 run** scored **30/30** in **17m 07s**, at **61.6 decode tok/s**, with **61,637 output tokens**, **19.55 GiB peak VRAM**, and **69.1% MTP acceptance**. Its separate V1 result remains 29/30. The dense model's exact weight filename/quantization was not archived in the discussion; do not infer it.

The direct Vulkan and Strata CLI→Vulkan scores and speeds are nearly identical; one 1.05 s runtime difference does not establish a meaningful CLI overhead. Strata had **no native Vulkan LLM engine** in this setup; the CLI used an external llama.cpp Vulkan server.

## Data and reproducibility

- [V3 machine-readable scores](v3-results.json): model labels, known wrong letters, score breakdowns, first-pass metadata, and run notes.
- [XTX machine-readable run archive](xtx-2026-10-24.json): V1/V3 configurations, benchmark timing, throughput, tokens and errors.
- [Frozen V3 questions](../v3/questions.json). The V3 answer key is privately held and **not included in this public repository**; [frozen V1 questions](../questions.json) and [V1 key](../answer_key.json).
- Runner: [run_benchmark.py](../run_benchmark.py) (`--version v1` or `--version v3`; the answer key stays evaluator-only).

**Provenance:** The results were reported by the user and coding agents in conversation, with some answer sheets graded against a separately held private benchmark key. This archive does not claim to contain all raw inference transcripts, host logs, exact checkpoint revisions, or original engine settings. Where these are missing, the record says so. Scores are not independently rerun on hardware.

**Next experiments mentioned, not yet reported:** Flint performance on XTX, local GLM through OhMyPi/Claude Code, and Claude Code harness comparison for XTX.

**Answer-key policy:** V3 correct answer letters and full answer sheets are intentionally not published. Public data includes scores, missed item IDs, timings, configurations and first-pass completion. Historical GitHub commits may retain previously exposed content; removing a file from the current branch does not erase commit history.
