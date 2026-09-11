# Paper 02 – PRESENT (2007)

## Paper Information

### Title

**PRESENT: An Ultra-Lightweight Block Cipher**

### Authors

Andrey Bogdanov, Lars R. Knudsen, Gregor Leander, Christof Paar, Axel Poschmann, Matthew J. B. Robshaw, Yannick Seurin, and C. Vikkelsoe

### Year

2007

### Conference

*Cryptographic Hardware and Embedded Systems – CHES 2007*

### Pages

450–466

### DOI

https://doi.org/10.1007/978-3-540-74735-2_31

---

## 1. Research Problem

The paper addresses the need for cryptographic algorithms that can operate efficiently on devices with very limited hardware resources.

Many embedded systems have restrictions in areas such as:

- Hardware area
- Memory
- Power consumption
- Processing capability

Conventional cryptographic algorithms may require more resources than are available on highly constrained devices.

Therefore, the researchers proposed PRESENT as an ultra-lightweight block cipher designed specifically for constrained environments.

---

## 2. Proposed Algorithm

The paper introduces **PRESENT**, a lightweight symmetric block cipher.

PRESENT uses:

- 64-bit block size
- 80-bit key or 128-bit key
- 31 encryption rounds

The design focuses on achieving a small hardware footprint while maintaining an appropriate level of security.

---

## 3. Design Approach

PRESENT uses a substitution-permutation network structure.

The cipher combines:

- AddRoundKey operations
- Substitution operations
- Bit permutation

The design was developed to minimise implementation requirements while maintaining cryptographic strength.

This makes the algorithm particularly relevant to embedded systems and highly constrained hardware.

---

## 4. Evaluation Focus

The paper primarily evaluates the lightweight characteristics of PRESENT from a hardware implementation perspective.

Important considerations include:

- Hardware area
- Power requirements
- Implementation efficiency
- Security characteristics

The study demonstrates that cryptographic functionality can be implemented using a relatively small hardware footprint.

---

## 5. Main Findings

The research demonstrates that PRESENT can achieve a compact hardware implementation while providing suitable cryptographic protection.

Its lightweight design makes it suitable for applications where hardware resources are severely constrained.

The study established PRESENT as an important example of lightweight block cipher design.

---

## 6. Strengths

The main strengths of PRESENT include:

- Very compact hardware design
- Low implementation requirements
- Suitable for constrained embedded devices
- 80-bit and 128-bit key options
- Designed specifically for lightweight cryptography

---

## 7. Limitations

The paper primarily focuses on lightweight hardware implementation rather than providing a direct performance comparison with AES, SPECK and ASCON.

The evaluation is also strongly oriented toward hardware characteristics.

Therefore, additional software-based experiments are useful when evaluating PRESENT alongside algorithms designed for efficient software implementations.

---

## 8. Relevance to Proposed Research

PRESENT is included in the proposed research because of its lightweight design and suitability for constrained environments.

The paper provides support for selecting PRESENT as one of the four algorithms to be evaluated:

**AES, PRESENT, SPECK and ASCON**

The proposed research will extend the analysis by evaluating PRESENT alongside the other selected algorithms using common experimental conditions and performance metrics.

---

## 9. Contribution to Research Gap

The PRESENT study demonstrates the importance of designing cryptographic algorithms specifically for constrained environments.

However, the study does not provide a unified experimental comparison involving all four algorithms selected for the proposed research.

This supports the identified research gap regarding the lack of a consistent comparison of different lightweight encryption algorithms.

The proposed research will address this gap by applying the same testing conditions and evaluation criteria to all selected algorithms.

---

## 10. Key Takeaway

The main takeaway from the paper is that lightweight cryptographic algorithms can be designed to significantly reduce hardware requirements while maintaining useful security characteristics.

PRESENT therefore provides an important lightweight reference for evaluating encryption algorithms intended for resource-constrained IoT devices.

---

## Reference

Bogdanov, A., Knudsen, L. R., Leander, G., Paar, C., Poschmann, A., Robshaw, M. J. B., Seurin, Y., & Vikkelsoe, C. (2007). PRESENT: An ultra-lightweight block cipher. In *Cryptographic Hardware and Embedded Systems – CHES 2007* (pp. 450–466). Springer.

DOI: https://doi.org/10.1007/978-3-540-74735-2_31
