# Algorithm Comparison

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## 1. Overview

This section compares the four encryption algorithms selected for the proposed research: AES, PRESENT, SPECK and ASCON.

The comparison focuses on their design characteristics, security capabilities, resource requirements and suitability for resource-constrained IoT devices.

---

## 2. Comparison of Encryption Algorithms

| Feature | AES | PRESENT | SPECK | ASCON |
|---|---|---|---|---|
| Type | Symmetric block cipher | Lightweight block cipher | Lightweight block cipher | Authenticated encryption |
| Main Focus | General-purpose security | Hardware efficiency | Software efficiency | Lightweight authenticated encryption |
| Block Size | 128-bit | 64-bit | Configuration dependent | 128-bit state |
| Key Size | 128, 192, 256-bit | 80, 128-bit | Configuration dependent | 128-bit key |
| Resource Requirement | Moderate | Very low | Low | Low |
| Hardware Suitability | Suitable with sufficient resources | Highly suitable | Suitable | Suitable |
| Software Efficiency | Good | Moderate | High | High |
| Authentication | Not provided directly | Not provided directly | Not provided directly | Built-in |
| IoT Suitability | Suitable as a benchmark | Suitable for highly constrained devices | Suitable for constrained processors | Highly relevant to modern IoT |

---

## 3. AES

AES is an established symmetric encryption algorithm widely used for securing digital information.

Its strong security and widespread adoption make it useful as a benchmark when comparing lightweight cryptographic algorithms.

However, AES may require more computational and memory resources than algorithms specifically designed for highly constrained environments.

Therefore, AES is included in the proposed research to provide a comparison between an established encryption standard and lightweight alternatives.

---

## 4. PRESENT

PRESENT was designed as an ultra-lightweight block cipher for constrained hardware environments.

Its compact structure allows it to operate with relatively low hardware requirements.

This makes PRESENT relevant to IoT devices with limited processing power, memory and energy availability.

However, PRESENT does not provide authenticated encryption as part of its basic design, which is an important consideration when comparing it with ASCON.

---

## 5. SPECK

SPECK is a family of lightweight block ciphers designed to provide efficient encryption on constrained computing platforms.

Its simple operations support efficient software implementations and can reduce computational overhead.

SPECK is therefore suitable for evaluating lightweight encryption performance on resource-constrained processors.

Previous research has also demonstrated strong performance for SPECK in certain resource-constrained IoT environments.

---

## 6. ASCON

ASCON is a lightweight cryptographic family designed for constrained devices.

Unlike traditional block ciphers such as AES, PRESENT and SPECK, ASCON provides authenticated encryption, allowing confidentiality and integrity protection to be handled within the same cryptographic construction.

ASCON was standardised by NIST for lightweight cryptography and is therefore highly relevant to modern IoT security requirements.

Its lightweight design makes it suitable for evaluating performance and resource efficiency in constrained environments.

---

## 7. Strengths and Limitations

| Algorithm | Strengths | Limitations |
|---|---|---|
| AES | Strong security, widely adopted, well-established | May require more resources on highly constrained devices |
| PRESENT | Very compact and lightweight hardware design | Limited compared with modern authenticated encryption approaches |
| SPECK | Efficient software implementation and low computational overhead | Performance can vary depending on configuration and platform |
| ASCON | Lightweight, authenticated encryption, modern standard | Performance may vary depending on implementation and hardware |

---

## 8. Suitability for Resource-Constrained IoT

The four algorithms provide different approaches to lightweight encryption.

**AES** is useful as a benchmark because of its established security and widespread use.

**PRESENT** is particularly relevant where hardware resource consumption is a major concern.

**SPECK** is useful for evaluating lightweight software performance on constrained processors.

**ASCON** is highly relevant for modern IoT applications because it combines lightweight operation with authenticated encryption.

Therefore, comparing these algorithms under consistent experimental conditions can provide useful information about their relative performance and resource requirements.

---

## 9. Comparison Based on Research Metrics

The proposed research will compare the algorithms using the following metrics:

| Metric | Purpose |
|---|---|
| Execution Time | Determines how quickly encryption and decryption are performed |
| Memory Utilization | Measures memory required during cryptographic operations |
| Throughput | Measures the amount of data processed over time |
| Latency | Measures the delay introduced by encryption and decryption |
| Energy Consumption | Evaluates the energy required for cryptographic processing |
| Security | Considers the security characteristics and protection provided by each algorithm |

These metrics will be applied using consistent experimental conditions to improve the fairness of the comparison.

---

## 10. Expected Comparison

The proposed research does not assume that one algorithm will be the best in every category.

Instead, the experiment will determine the relative strengths and limitations of AES, PRESENT, SPECK and ASCON based on the collected measurements.

The results are expected to demonstrate differences in:

- Processing performance
- Memory requirements
- Data processing efficiency
- Latency
- Energy consumption
- Security characteristics

The final conclusions will be based on experimental results rather than assumptions from previous studies.

---

## 11. Conclusion

AES, PRESENT, SPECK and ASCON represent different approaches to cryptographic protection for constrained environments.

AES provides an established benchmark, PRESENT focuses on compact hardware implementation, SPECK provides efficient lightweight operations, and ASCON provides modern authenticated encryption.

Their different characteristics make them suitable for comparative evaluation.

The proposed research will therefore implement and evaluate the four algorithms under consistent conditions using common performance and resource-efficiency metrics.
