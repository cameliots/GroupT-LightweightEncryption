# Research Methodology

## Section 3.1 — Research Methodology

This study adopts an **experimental research methodology** because the research aim is to
compare the performance and resource efficiency of selected lightweight encryption algorithms
under controlled and consistent conditions, rather than to explore opinions or behaviours.

The methodology is built around the implementation, execution and measurement of four
lightweight encryption algorithms:

- **AES-128** — conventional symmetric standard, used as the reference baseline
- **PRESENT** — ultra-lightweight block cipher (64-bit block, 80-bit key)
- **SPECK** — lightweight ARX block cipher (64-bit block, 128-bit key)
- **ASCON-128** — NIST-standardised lightweight authenticated encryption

These four algorithms were selected based on the literature review presented in Chapter 2 and
documented in `../02_Literature_Review/`.

---

## Quantitative Approach

A **quantitative approach** is used in this study. Numerical data such as encryption time,
decryption time, memory usage and throughput are gathered through repeated experiments. These
results are then analysed using descriptive statistical methods (mean and standard deviation)
to make objective comparisons between algorithms.

This approach matches the methods used by the cryptography studies reviewed in Chapter 2, which
rely on controlled experiments rather than surveys or descriptive explanations alone.

---

## Justification for the Baseline

**AES-128 is taken as the reference point** for comparison. AES is the most widely used
symmetric encryption standard and is commonly adopted as a comparison point in lightweight
cryptography research, including Radhakrishnan et al. (2024). AES also represents
"conventional cryptography" as distinguished from the "lightweight cryptography" category
comprising PRESENT, SPECK and ASCON.

Using AES-128 as the baseline allows the study to quantify how much improvement in time,
memory and throughput the lightweight algorithms offer relative to an established conventional
standard.

---

## Control of Experimental Conditions

The research gap identified in Section 2.4.2 is that direct comparison between studies is
difficult because researchers use different hardware platforms, datasets, workloads and
evaluation metrics. To address this gap, the following conditions are held constant across all
four algorithms:

| Condition | Control Applied |
|---|---|
| Implementation language | All four ciphers implemented in the same language and runtime |
| Hardware platform | Single machine, identical for all runs |
| Background load | Idle background state during measurement |
| Test input | Identical plaintext bytes supplied to every algorithm |
| Data sizes | 1 KB, 10 KB, 100 KB and 1 MB for every algorithm |
| Number of trials | 30 repetitions per algorithm per data size |
| Timing method | Same monotonic high-resolution timer for all algorithms |
| Memory method | Same allocation tracker for all algorithms |

Implementing all four ciphers in the same language and runtime is a deliberate methodological
decision. Using an optimised native library for one algorithm and an interpreted implementation
for another would reintroduce exactly the comparability problem that this research aims to
solve.

---

## Research Process

The overall research process is:

1. Select the algorithms (based on Chapter 2)
2. Design the experimental architecture
3. Build the implementation and measurement framework
4. Test and validate against published test vectors
5. Collect performance data across repeated trials
6. Analyse and compare the results

Each of these steps is expanded in `Methodology_Phases.md`.

---

## Reference

Radhakrishnan, I., Jadon, S., & Honnavalli, P. B. (2024). Efficiency and security evaluation of
lightweight cryptographic algorithms for resource-constrained IoT devices. *Sensors, 24*(12),
4008. https://doi.org/10.3390/s24124008
