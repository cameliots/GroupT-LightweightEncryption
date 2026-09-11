# Research Gap Analysis

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## 1. Introduction

The literature review shows that lightweight encryption is important for protecting data in resource-constrained IoT environments.

Previous studies have evaluated individual lightweight algorithms and, in some cases, compared multiple algorithms. However, differences in experimental conditions make it difficult to determine which algorithms provide the best balance between security, performance and resource efficiency.

This section identifies the research gaps that motivate the proposed research.

---

## 2. Findings from Previous Research

Previous research has demonstrated that different encryption algorithms have different performance and resource requirements.

Radhakrishnan et al. (2024) compared AES-128, SPECK and ASCON on resource-constrained IoT boards using metrics such as execution time, memory utilization, latency, throughput and security robustness.

Research on PRESENT focused on its ultra-lightweight design and suitability for constrained hardware.

Research on SPECK demonstrated its focus on efficient software implementation for constrained computing platforms.

NIST's standardisation of ASCON further demonstrates the importance of lightweight authenticated encryption for constrained devices.

These studies provide a strong foundation for selecting algorithms and evaluation metrics for the proposed research.

---

## 3. Identified Research Gaps

### 3.1 Lack of a Unified Comparison

Previous studies do not consistently evaluate AES, PRESENT, SPECK and ASCON together.

Some studies focus on individual algorithms, while others compare only a subset of the algorithms.

Therefore, a unified comparison of all four selected algorithms is required.

---

### 3.2 Different Hardware Platforms

Existing research uses different hardware platforms.

The processing capability, memory capacity and architecture of the hardware can affect encryption performance.

As a result, results obtained from different platforms may not be directly comparable.

The proposed research will use a consistent experimental platform for all selected algorithms.

---

### 3.3 Different Experimental Conditions

Previous studies may use different:

- Input data
- Input sizes
- Number of test repetitions
- Software environments
- Implementation techniques
- Testing procedures

These differences can influence measured performance.

The proposed research will apply consistent experimental conditions to improve the fairness of the comparison.

---

### 3.4 Inconsistent Evaluation Metrics

Different studies may focus on different evaluation metrics.

For example, one study may focus on execution time and memory, while another may focus on throughput or security.

This makes it difficult to evaluate the overall suitability of different algorithms.

The proposed research will use a common set of evaluation metrics:

- Execution time
- Memory utilization
- Throughput
- Latency
- Energy consumption where applicable
- Security characteristics

---

### 3.5 Limited Comparison of Resource Efficiency and Security

An algorithm may provide good computational performance while having different security characteristics or resource requirements.

Therefore, evaluating performance alone may not provide enough information for selecting an encryption algorithm for IoT devices.

The proposed research will consider both resource efficiency and security characteristics when analysing the selected algorithms.

---

## 4. Research Gap Summary

| Existing Research Situation | Identified Gap | Proposed Research Response |
|---|---|---|
| Studies may evaluate different subsets of algorithms | Limited unified comparison | Compare AES, PRESENT, SPECK and ASCON together |
| Different hardware platforms are used | Results may not be directly comparable | Use a consistent experimental platform |
| Different input sizes and workloads are used | Performance results may vary | Use common test inputs and controlled workloads |
| Different evaluation metrics are used | Difficult to compare overall performance | Apply common evaluation metrics |
| Performance and security may be considered separately | Difficult to determine overall suitability | Analyse resource efficiency together with security |
| Different implementation environments are used | Implementation differences may affect results | Use consistent software and testing conditions |

---

## 5. Proposed Research Response

The proposed research addresses these gaps through a controlled comparative evaluation.

The research will:

1. Select AES, PRESENT, SPECK and ASCON based on the literature review.
2. Implement the selected algorithms using a consistent experimental environment.
3. Use common input data and controlled input sizes.
4. Apply the same testing procedures to each algorithm.
5. Measure execution time and memory utilization.
6. Evaluate throughput and latency.
7. Measure energy consumption where appropriate and feasible.
8. Compare relevant security characteristics.
9. Analyse the results using tables and graphical representations.

---

## 6. Relationship Between Research Gap and Objectives

The identified research gaps directly support the research objectives.

### Research Objective 1

**To identify and select lightweight encryption algorithms suitable for resource-constrained IoT environments based on findings from existing literature.**

The literature review identifies AES, PRESENT, SPECK and ASCON as suitable algorithms for comparative evaluation.

### Research Objective 2

**To implement the selected lightweight encryption algorithms in a controlled experimental environment using consistent test conditions.**

The differences in hardware, implementation environments and experimental conditions identified in previous research demonstrate the need for a controlled testing environment.

### Research Objective 3

**To evaluate and compare the selected algorithms based on defined performance and resource-efficiency metrics.**

The lack of consistent evaluation metrics supports the use of common measurements such as execution time, memory utilization, throughput, latency and energy consumption.

---

## 7. Research Significance

Addressing these research gaps can provide a clearer understanding of the trade-offs between different encryption algorithms.

The results may help determine which algorithm provides a more suitable balance between:

- Security
- Processing performance
- Memory efficiency
- Data processing capability
- Latency
- Energy efficiency

This information can support the selection of suitable encryption algorithms for different resource-constrained IoT environments.

---

## 8. Expected Contribution

The proposed research is expected to contribute a consistent comparative evaluation of AES, PRESENT, SPECK and ASCON.

Rather than assuming that one algorithm is universally superior, the research will analyse the measured results and identify the strengths and limitations of each algorithm.

The findings can provide a useful reference for understanding the trade-offs involved when selecting encryption algorithms for resource-constrained IoT devices.

---

## 9. Conclusion

The literature review identifies several limitations in existing comparative research, particularly differences in algorithms evaluated, hardware platforms, input conditions, implementation environments and evaluation metrics.

These differences make direct comparison difficult.

The proposed research addresses these gaps by evaluating AES, PRESENT, SPECK and ASCON under consistent experimental conditions using common performance, resource-efficiency and security-related criteria.

The identified research gaps therefore provide the foundation for the proposed methodology and experimental evaluation.
