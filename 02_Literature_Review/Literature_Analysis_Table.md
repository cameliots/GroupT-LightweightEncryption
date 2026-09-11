# Literature Analysis Table

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## Literature Analysis

| Study | Algorithm | Platform / Environment | Evaluation Metrics | Main Findings | Limitation | Relevance to Proposed Research |
|---|---|---|---|---|---|---|
| Radhakrishnan et al. (2024) | AES-128, SPECK, ASCON | Resource-constrained IoT boards, including Arduino Micro/Nano | Execution time, memory utilization, latency, throughput, security robustness | SPECK demonstrated strong performance in the evaluated environment | Results may depend on the hardware platform and implementation | Provides the main basis for the proposed evaluation metrics and comparison |
| Bogdanov et al. (2007) | PRESENT | Constrained hardware environments | Hardware efficiency and security characteristics | PRESENT was designed as an ultra-lightweight block cipher with a compact design | Focuses mainly on lightweight hardware design rather than direct comparison with all selected algorithms | Supports the selection of PRESENT for the proposed comparison |
| Beaulieu et al. (2013) | SPECK | Constrained computing platforms | Lightweight implementation and efficiency | SPECK was designed for efficient operation on constrained platforms | Performance depends on configuration, implementation and hardware platform | Supports SPECK as a lightweight algorithm for comparison |
| Turan et al. (2025) | ASCON | Constrained devices | Lightweight authenticated cryptography and security | ASCON provides standardised lightweight cryptographic functions for constrained devices | Does not directly compare ASCON with all algorithms selected in this research | Supports ASCON as a modern lightweight cryptographic algorithm |

---

## Analysis of Reviewed Studies

The reviewed studies demonstrate that lightweight cryptographic algorithms can reduce computational and resource requirements for resource-constrained devices.

Radhakrishnan et al. (2024) provides a particularly relevant comparison because it evaluates AES-128, SPECK and ASCON using several performance and resource-related metrics.

The PRESENT study focuses on developing an ultra-lightweight block cipher suitable for constrained hardware, while the SPECK study focuses on lightweight cryptographic operations for constrained computing platforms.

The NIST ASCON standard demonstrates the development and standardisation of lightweight cryptography for constrained devices.

However, the reviewed studies use different hardware platforms, implementation environments, input conditions and evaluation approaches. Therefore, their results cannot always be directly compared.

---

## Identified Research Gap

The main research gap identified from the literature is the lack of a unified experimental comparison of AES, PRESENT, SPECK and ASCON under the same experimental conditions.

Existing studies may differ in:

- Hardware platforms
- Software environments
- Input sizes
- Test workloads
- Implementation techniques
- Evaluation metrics
- Experimental conditions

These differences can affect measured performance and make direct comparison between algorithms difficult.

---

## Proposed Research Response

The proposed research addresses the identified gap by:

1. Comparing AES, PRESENT, SPECK and ASCON.
2. Using consistent experimental conditions.
3. Using common test inputs.
4. Applying common evaluation metrics.
5. Measuring performance and resource-efficiency characteristics.
6. Analysing the strengths and limitations of each algorithm.

This approach is intended to provide a clearer and more consistent comparison of the selected lightweight encryption algorithms for resource-constrained IoT devices.

---

## Contribution to Research Objectives

### Research Objective 1

**To identify and select lightweight encryption algorithms suitable for resource-constrained IoT environments based on findings from existing literature.**

The reviewed literature supports the selection of AES, PRESENT, SPECK and ASCON for the proposed comparative evaluation.

### Research Objective 2

**To implement the selected lightweight encryption algorithms in a controlled experimental environment using consistent test conditions.**

The identified research gap supports the need for consistent experimental conditions when comparing the selected algorithms.

### Research Objective 3

**To evaluate and compare the selected algorithms based on defined performance and resource-efficiency metrics.**

The reviewed studies provide a basis for evaluating execution time, memory utilization, throughput, latency, energy consumption and security.

---

## Summary

The literature analysis shows that each selected algorithm has different design characteristics and resource considerations.

AES provides an established encryption benchmark, PRESENT focuses on compact hardware implementation, SPECK focuses on efficient lightweight operations, and ASCON provides modern lightweight authenticated encryption.

The differences in previous experimental conditions highlight the need for a consistent comparative evaluation. The proposed research will therefore compare the four selected algorithms using common conditions and evaluation metrics.
