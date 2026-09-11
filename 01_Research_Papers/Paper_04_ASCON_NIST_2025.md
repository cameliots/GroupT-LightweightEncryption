# Paper 04 – ASCON NIST (2025)

## Paper Information

### Title

**Ascon-Based Lightweight Cryptography Standards for Constrained Devices: Authenticated Encryption, Hash, and Extendable Output Functions**

### Authors

M. S. Turan, K. McKay, J. Kang, J. Kelsey, and D. Chang

### Year

2025

### Publisher

National Institute of Standards and Technology (NIST)

### Publication

NIST Special Publication 800-232

### DOI

https://doi.org/10.6028/NIST.SP.800-232

---

## 1. Research Problem

Resource-constrained devices require cryptographic protection while operating with limited processing power, memory and energy.

Traditional cryptographic solutions may introduce significant computational and resource requirements.

The publication addresses the need for lightweight cryptographic standards that provide appropriate security while remaining suitable for constrained devices.

---

## 2. ASCON-Based Lightweight Cryptography

The publication specifies Ascon-based lightweight cryptographic standards for constrained devices.

The standards cover:

- Authenticated encryption
- Hash functions
- Extendable-output functions

Authenticated encryption is particularly important because it can provide confidentiality and integrity protection within a single cryptographic construction.

---

## 3. ASCON and IoT Devices

ASCON is designed for environments where computing resources are limited.

Its lightweight characteristics make it relevant to applications involving:

- IoT devices
- Embedded systems
- Sensor networks
- Low-power devices
- Resource-constrained systems

These characteristics make ASCON an important candidate for evaluating modern lightweight cryptography.

---

## 4. Security Capabilities

ASCON-based authenticated encryption provides protection against unauthorised access to data while also supporting data integrity and authentication.

This is an important distinction when comparing ASCON with conventional encryption algorithms that do not directly provide authenticated encryption as part of their basic construction.

Security is therefore an important factor when evaluating ASCON for IoT applications.

---

## 5. Evaluation Focus

The NIST publication focuses primarily on the standardisation and technical specification of Ascon-based lightweight cryptography.

Important considerations include:

- Security
- Authenticated encryption
- Hashing
- Lightweight implementation
- Suitability for constrained devices

The publication provides a standardised foundation for implementing and evaluating ASCON-based cryptographic functions.

---

## 6. Main Findings

The publication establishes Ascon-based algorithms as standards for lightweight cryptography for constrained devices.

ASCON provides authenticated encryption capabilities while maintaining a lightweight design suitable for constrained environments.

This makes ASCON particularly relevant to modern IoT applications where both resource efficiency and data integrity are important.

---

## 7. Strengths

The main strengths of ASCON include:

- Designed for constrained devices
- Lightweight cryptographic design
- Provides authenticated encryption
- Supports confidentiality and integrity
- Standardised by NIST
- Relevant to modern IoT security requirements

---

## 8. Limitations

The publication is primarily a cryptographic standard and does not provide a direct experimental comparison of ASCON with all algorithms selected for this research.

It therefore does not determine whether ASCON is faster or more resource-efficient than AES, PRESENT or SPECK under identical experimental conditions.

Experimental evaluation is still required to make such comparisons.

---

## 9. Relevance to Proposed Research

ASCON is one of the four algorithms selected for the proposed research:

**AES, PRESENT, SPECK and ASCON**

The NIST publication provides strong support for selecting ASCON because it is specifically designed and standardised for lightweight cryptography on constrained devices.

The proposed research will evaluate ASCON alongside AES, PRESENT and SPECK using common experimental conditions and evaluation metrics.

---

## 10. Contribution to Research Gap

The NIST standard demonstrates the importance of modern lightweight authenticated encryption for constrained devices.

However, standardisation alone does not establish how ASCON compares with other selected algorithms in terms of execution time, memory utilization, throughput, latency and energy consumption under the same testing conditions.

The proposed research addresses this gap by including ASCON in a unified experimental comparison.

---

## 11. Key Takeaway

The main takeaway from this publication is that ASCON provides a modern standardised approach to lightweight authenticated encryption for constrained devices.

Its combination of lightweight operation, confidentiality and integrity protection makes it highly relevant to resource-constrained IoT environments.

---

## Reference

Turan, M. S., McKay, K., Kang, J., Kelsey, J., & Chang, D. (2025). *Ascon-based lightweight cryptography standards for constrained devices: Authenticated encryption, hash, and extendable output functions*. NIST Special Publication 800-232.

DOI: https://doi.org/10.6028/NIST.SP.800-232
