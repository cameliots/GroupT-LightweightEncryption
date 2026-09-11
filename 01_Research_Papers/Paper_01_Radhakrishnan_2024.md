# Paper 01 – Radhakrishnan et al. (2024)

## Paper Information

### Title

**Efficiency and Security Evaluation of Lightweight Cryptographic Algorithms for Resource-Constrained IoT Devices**

### Authors

I. Radhakrishnan, S. Jadon, and P. B. Honnavalli

### Year

2024

### Journal

*Sensors, 24*(12), 4008

### DOI

https://doi.org/10.3390/s24124008

---

## 1. Research Problem

The study investigates the performance and security of lightweight cryptographic algorithms when implemented on resource-constrained IoT devices.

IoT devices commonly have limitations in processing capability, memory, energy availability and computational resources. These limitations can affect the suitability of cryptographic algorithms for IoT applications.

Therefore, the study evaluates different algorithms to determine their efficiency and security characteristics in constrained environments.

---

## 2. Algorithms Evaluated

The study evaluates:

- AES-128
- SPECK
- ASCON

These algorithms represent different approaches to cryptographic protection for resource-constrained IoT environments.

---

## 3. Experimental Platform

The algorithms were evaluated using resource-constrained IoT development boards, including Arduino-based platforms such as:

- Arduino Micro
- Arduino Nano

The use of constrained hardware allows the researchers to examine the practical performance of the algorithms in environments similar to low-resource IoT devices.

---

## 4. Evaluation Metrics

The study evaluates the algorithms using several performance and security-related metrics.

The main metrics include:

- Execution time
- Memory utilization
- Latency
- Throughput
- Security robustness

These metrics provide information about both computational performance and resource requirements.

---

## 5. Method

The selected cryptographic algorithms were implemented and tested on resource-constrained IoT hardware.

The researchers measured the performance of each algorithm and compared the results across the selected platforms.

The evaluation considered both computational efficiency and security characteristics rather than focusing only on encryption speed.

---

## 6. Main Findings

The study demonstrates that cryptographic algorithm performance can vary depending on the hardware platform and implementation environment.

SPECK demonstrated strong performance in the evaluated environment, particularly in terms of efficiency for resource-constrained platforms.

The study also demonstrates the importance of considering multiple performance metrics when selecting cryptographic algorithms for IoT devices.

---

## 7. Limitations

The results of the study are influenced by the selected hardware platforms and implementation environment.

Performance obtained on one IoT development board may not be identical on another hardware architecture.

In addition, the study does not provide a unified comparison of all four algorithms selected for the proposed research because PRESENT is not included in the comparison.

---

## 8. Relevance to Proposed Research

This study is highly relevant to the proposed research because it evaluates lightweight cryptographic algorithms specifically for resource-constrained IoT devices.

The study provides a basis for selecting several evaluation metrics, including:

- Execution time
- Memory utilization
- Latency
- Throughput
- Security

The proposed research extends this comparison by including PRESENT and evaluating:

**AES, PRESENT, SPECK and ASCON**

under consistent experimental conditions.

---

## 9. Contribution to Research Gap

The study demonstrates that algorithm performance can depend on the hardware and implementation environment.

This supports the research gap identified in the literature review, where different experimental conditions can make direct comparison difficult.

The proposed research addresses this issue by using common experimental conditions, common input data and common evaluation metrics when comparing the selected algorithms.

---

## 10. Key Takeaway

The main takeaway from this study is that lightweight encryption algorithms should be evaluated based on both security and resource efficiency.

An algorithm that performs well in one environment may produce different results on another platform.

Therefore, controlled and consistent experimental conditions are important when comparing lightweight encryption algorithms for resource-constrained IoT devices.

---

## Reference

Radhakrishnan, I., Jadon, S., & Honnavalli, P. B. (2024). Efficiency and security evaluation of lightweight cryptographic algorithms for resource-constrained IoT devices. *Sensors, 24*(12), 4008.

DOI: https://doi.org/10.3390/s24124008
