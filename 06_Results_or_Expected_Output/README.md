# Results / Expected Output

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## Purpose of This Folder

This folder documents the proposed evaluation plan (Section 3.7), the expected measurable
outcomes, and the output format the experiment produces. It supports Research Objective **RO3**
(evaluate and compare the selected algorithms based on defined performance and resource-efficiency
metrics).

---

## Contents

| File | Description |
|---|---|
| `README.md` | Evaluation plan, metrics and expected outcomes |
| `sample_results.csv` | Output from a verification run (10 trials, 1 KB and 10 KB) |
| `sample_results.metadata.json` | Environment and parameters of that run |
| `Sample_Analysis_Report.md` | Analysis report generated from the sample run |
| `results.csv` | *(produced by the full 30-trial run)* |
| `Analysis_Report.md` | *(produced by the full 30-trial run)* |

---

## Baseline for Comparison

**AES-128 is taken as the reference point.** AES is the most widely used symmetric encryption
standard and is commonly adopted as a comparison point in lightweight cryptography research,
including Radhakrishnan et al. (2024). AES also represents "conventional cryptography", as
distinguished from the "lightweight cryptography" category comprising PRESENT, SPECK and ASCON.

Using AES-128 as the baseline allows the study to quantify how much improvement in time, memory
and throughput the lightweight algorithms offer relative to an established conventional standard.

---

## Table 3.2: Proposed Evaluation Metrics

| Metrics Category | Specific Metric | Definition | Unit of Measurement |
|---|---|---|---|
| **Performance** | Encryption Time | Time taken to convert plaintext into ciphertext | Milliseconds (ms) |
| | Decryption Time | Time taken to convert ciphertext into plaintext | Milliseconds (ms) |
| | Throughput | Amount of data processed per unit time | Megabits per second (Mbps) |
| **Resource Efficiency** | Memory / RAM Usage | Amount of memory consumed during algorithm execution | Kilobytes (KB) |
| | Energy indication (where feasible) | Estimated computational effort / power draw during execution | Relative measure / mW (if measurable) |

---

## Expected Measurable Outcomes

The experiment performs quantitative analysis over 30 repeated trials for every algorithm across
four levels of test dataset size: 1 KB, 10 KB, 100 KB and 1 MB.

The outcomes are the mean and standard deviation of encryption time, decryption time, memory used
and throughput for AES, PRESENT, SPECK and ASCON. Comparison tables at each dataset size show
which algorithm performed best on each metric. All results are stored in a reproducible CSV
dataset in this repository.

**Full run:** 4 algorithms × 4 data sizes × 30 trials = **480 recorded encrypt/decrypt pairs.**

---

## Output Format

`results.csv` contains one row per trial:

| Column | Description |
|---|---|
| `algorithm` | Cipher name |
| `category` | Conventional or Lightweight |
| `mode` | CTR or AEAD |
| `data_size_label` | 1KB / 10KB / 100KB / 1MB |
| `data_size_bytes` | Payload size in bytes |
| `trial` | Trial number |
| `encrypt_time_ms` | Encryption time |
| `decrypt_time_ms` | Decryption time |
| `encrypt_peak_memory_kb` | Peak memory during encryption |
| `decrypt_peak_memory_kb` | Peak memory during decryption |
| `encrypt_throughput_mbps` | Encryption throughput |
| `decrypt_throughput_mbps` | Decryption throughput |
| `ciphertext_bytes` | Length of ciphertext produced |
| `roundtrip_valid` | Whether decryption recovered the original plaintext |

Raw per-trial rows are stored rather than pre-aggregated averages, so that the summary statistics
can be recomputed or a different analysis applied without re-running the experiment
(Section 3.6.3).

---

## Expected Outcomes (Section 3.9)

Based on the literature reviewed in Chapter 2, the following outcomes are anticipated:

- **SPECK** is expected to show short processing time and low CPU use, due to the simplicity of
  its ARX design, making it well suited to microcontrollers with limited processing power
  (Radhakrishnan et al., 2024).
- **ASCON** is expected to show balanced performance, offering authenticated encryption (AEAD)
  at moderate memory cost, consistent with Radhakrishnan et al. (2024) and its adoption for
  constrained IoT environments.
- **PRESENT** is expected to consume the least memory because of its small 64-bit block size,
  though it may not match SPECK in processing speed.

In summary, **no algorithm is expected to outperform the others across every metric**, because
trade-offs are expected among speed, memory efficiency, throughput and security level. The
evaluation provides a consistent basis for comparing AES, PRESENT, SPECK and ASCON, addressing
the research gap in Section 2.4.2.

---

## Important Limitation: Software Platform Effects

The sample results show a pattern that must be interpreted carefully, and which is itself a
finding relevant to the research gap.

**PRESENT is the slowest algorithm in this software environment**, despite being designed as an
ultra-lightweight cipher. This is not a contradiction of the literature. PRESENT is optimised for
**hardware** efficiency: its bit-level permutation layer costs very few logic gates in an ASIC or
FPGA, but is expensive in software because each of the 64 bits must be moved individually.

Conversely, **AES benefits from a table-based software implementation**, which maps efficiently
onto a general-purpose CPU.

This directly illustrates the problem identified in Section 1.3: **an algorithm's measured
performance depends heavily on the evaluation platform.** A result showing PRESENT as slow in
software does not mean PRESENT is unsuitable for constrained hardware — it means software timing
alone cannot answer the question for hardware-oriented ciphers.

Accordingly, conclusions drawn from this study apply to **software execution on a
general-purpose processor**, and should be stated with that scope. Extending the evaluation to
FPGA or microcontroller platforms is identified as future work.

---

## Analysis Produced

The Analysis and Comparison Module generates:

1. **Measured metrics** — mean ± standard deviation for each metric, per algorithm per data size.
2. **Baseline comparison** — each algorithm expressed as a ratio relative to AES-128.
3. **Ciphertext expansion** — ciphertext length against plaintext length. ASCON adds 16 bytes
   because it includes an authentication tag; the CTR-mode block ciphers add none. This is
   reported explicitly so the difference is not mistaken for a measurement anomaly.

---

## Reproducing the Results

```bash
cd 04_Source_Code
python -m tests.test_vectors      # verify implementations first
python run_experiment.py          # full 30-trial run
```

Results are written back into this folder.
