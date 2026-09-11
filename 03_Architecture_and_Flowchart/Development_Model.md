# Development Model and Justification

## Section 3.2 — Development Model

Because this study is about creating an experimental model rather than a full production
system, a suitable software development approach is required to organise the implementation of
the four encryption algorithms and the testing framework. Three common software development
models were considered.

---

## Table 3.A: Comparison of Development Models

| Model | Strengths for this study | Limitations for this study | Suitability |
|---|---|---|---|
| **Waterfall Model** | Simple, easy to plan and document | Rigid; does not allow revisiting implementation after testing begins | Low |
| **Agile Model** | Flexible, supports change requests | Designed around end-user features and sprints, less suited to fixed algorithm-comparison research | Moderate |
| **Iterative & Incremental Model** | Allows each algorithm to be implemented, tested and refined in successive cycles; supports repeated data collection and progressive comparison | Requires careful planning between cycles to keep test conditions consistent | **High (Selected)** |

---

## Justification of the Selected Model

The **Iterative and Incremental Model** was selected as the development approach for this study.

This model was chosen because the four algorithms can be implemented one after another, with
each one tested and validated before the next algorithm is added to the experiment. This
prevents implementation errors from accumulating across all four components at once, and allows
the testing process to be verified early using the first algorithm before the same procedure is
applied to the remaining algorithms.

The iterative approach also allows the monitoring and logging modules to be verified step by
step, because each new algorithm cycle reuses the timing and logging components built in the
earlier cycle. This ensures that all four algorithms are ultimately tested with the same
validated measurement framework, which directly supports the consistency required to address
the research problem stated in Section 1.3.

---

## Iteration Plan

| Iteration | Deliverable | Validation Gate |
|---|---|---|
| **Iteration 0** | Experimental control module, performance monitor, data logger, analysis module | Framework produces a valid CSV from a no-op cipher |
| **Iteration 1** | AES-128 (baseline) | Known-answer test against FIPS-197 test vector; round-trip decryption succeeds |
| **Iteration 2** | PRESENT-80 | Known-answer test against Bogdanov et al. (2007) test vectors |
| **Iteration 3** | SPECK 64/128 | Known-answer test against Beaulieu et al. (2013) test vectors |
| **Iteration 4** | ASCON-128 AEAD | Round-trip authenticated encryption; tag verification succeeds |
| **Iteration 5** | Full comparative run and analysis | 30 trials × 4 data sizes × 4 algorithms recorded and analysed |

Each iteration reuses the framework from Iteration 0 without modification. If a defect is found
in the framework during a later iteration, the earlier iterations are re-run so that all
recorded results come from the same framework version.

---

## Mapping to the Repository

The iteration plan is reflected in the commit history of this repository. Each numbered folder
and each algorithm implementation was committed separately, so that the progression of the
research activity is visible and verifiable.
