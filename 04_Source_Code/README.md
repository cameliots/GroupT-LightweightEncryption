# Source Code

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## Purpose of This Folder

This folder contains the implementation of the experimental system described in
`../03_Architecture_and_Flowchart/`. It supports Research Objective **RO2** (implement the
selected algorithms in a controlled experimental environment using consistent test conditions)
and produces the data required for **RO3**.

---

## Requirements

Python 3.9 or later. **No third-party packages are required** — the implementation uses only the
Python standard library, so it runs anywhere Python runs, including on a constrained board.

---

## Quick Start

```bash
cd 04_Source_Code

# 1. Verify the cipher implementations against published test vectors
python -m tests.test_vectors

# 2. Short verification run (3 trials, up to 10 KB) — takes about a minute
python run_experiment.py --quick

# 3. Full experimental run (30 trials, up to 1 MB)
python run_experiment.py
```

> **Note on runtime.** The full run performs 480 encrypt/decrypt pairs on payloads up to 1 MB
> using pure-Python ciphers. It takes a long time — PRESENT on 1 MB is the slow case. Use
> `--quick` or `--max-size 100KB` while setting up, and run the full experiment once when
> collecting final data.

---

## Folder Structure

```
04_Source_Code/
├── run_experiment.py          Main entry point (Figure 3.2 process)
├── ciphers/                   Encryption & Decryption Algorithm Module
│   ├── base.py                Common Cipher interface + CTR mode
│   ├── aes128.py              AES-128        (baseline, conventional)
│   ├── present.py             PRESENT-80     (lightweight)
│   ├── speck.py               SPECK 64/128   (lightweight)
│   └── ascon.py               ASCON-128 AEAD (lightweight)
├── harness/                   Experimental framework
│   ├── control_module.py      Experimental Control Module
│   ├── monitor.py             Performance Monitoring Unit
│   ├── data_logger.py         Data Logger
│   ├── analysis.py            Analysis & Comparison Module
│   └── environment.py         Experimental environment recorder
└── tests/
    └── test_vectors.py        Known-answer tests (validation gate)
```

Each module maps to a component of Figure 3.1. See
`../03_Architecture_and_Flowchart/Module_Specification.md` for the full mapping.

---

## Implemented Algorithms

| Algorithm | Block | Key | Mode | Category | Reference |
|---|---|---|---|---|---|
| **AES-128** | 128-bit | 128-bit | CTR | Conventional (baseline) | FIPS 197 |
| **PRESENT-80** | 64-bit | 80-bit | CTR | Lightweight | Bogdanov et al. (2007) |
| **SPECK 64/128** | 64-bit | 128-bit | CTR | Lightweight | Beaulieu et al. (2013) |
| **ASCON-128** | 64-bit rate | 128-bit | AEAD | Lightweight | NIST SP 800-232 (2025) |

---

## Why All Four Are Implemented From Scratch

This is a deliberate methodological decision, not a shortcut.

Section 2.4.2 identifies that prior studies are hard to compare because different algorithms were
measured under different conditions. Using a highly optimised C library for AES and an interpreted
implementation for PRESENT would reintroduce exactly that problem — the measurement would compare
*implementations*, not *algorithms*.

Implementing all four in the same language and runtime, behind the same interface, means the
measured differences come from the algorithms' own structure: number of rounds, operations per
round, and how well those operations map onto the execution platform.

> **Security warning.** These are reference implementations written for a performance study. They
> are **not constant-time** and must never be used to protect real data. For production use,
> established audited libraries should be used instead.

---

## Verification

`tests/test_vectors.py` is the validation gate described in the iteration plan. Every cipher must
reproduce its published test vectors before any timing data from it is collected — a measurement
taken from an incorrect implementation would be meaningless.

| Algorithm | Verified Against |
|---|---|
| AES-128 | FIPS-197 Appendix B and Appendix C.1 known-answer vectors |
| PRESENT-80 | All four CHES 2007 Appendix I known-answer vectors, encryption and decryption |
| SPECK 64/128 | ePrint 2013/404 known-answer vector, encryption and decryption |
| ASCON-128 | Round-trip across every padding case (0, 1, 7, 8, 9, 15, 16, 17, 64, 1000 bytes) plus tamper detection on both ciphertext and tag |

Current status: **50 assertions, all passing.**

In addition, the control module verifies every single trial at runtime by comparing the recovered
plaintext against the original input. A failed comparison marks the trial invalid and excludes it
from the analysis.

---

## Measured Metrics

| Metric | Method | Unit |
|---|---|---|
| Encryption time | `time.perf_counter_ns()` around the encrypt call only | ms |
| Decryption time | `time.perf_counter_ns()` around the decrypt call only | ms |
| Peak memory | `tracemalloc` peak allocation during the operation | KB |
| Throughput | `payload_bytes × 8 ÷ elapsed_seconds ÷ 1e6` | Mbps |

The timer brackets only the cipher call. Data generation, validation and logging happen outside
the timed region.

---

## Experimental Controls

| Condition | Control |
|---|---|
| Test data | Generated from a fixed seed; byte-identical across algorithms and machines |
| Keys | Derived deterministically, once per algorithm, outside the measured region |
| Trials | 30 per algorithm per data size |
| Warm-up | 3 unmeasured iterations before each measured set, applied identically to all algorithms |
| Validation | Every trial's round trip verified before its data is used |
| Environment | Platform, processor, Python version and timer resolution recorded in the results metadata |

---

## Output

| File | Content |
|---|---|
| `../06_Results_or_Expected_Output/results.csv` | One row per trial (480 rows for a full run) |
| `../06_Results_or_Expected_Output/results.metadata.json` | Environment and parameters for the run |
| `../06_Results_or_Expected_Output/Analysis_Report.md` | Mean, standard deviation and baseline ratios |

---

## Contributor

| Name | Student ID | Contribution |
|---|---|---|
| MUHAMAD AZIM SYAFAWI BIN ABDULLAH | 52215124282 | Implementation of the four ciphers, experimental framework and validation tests |
