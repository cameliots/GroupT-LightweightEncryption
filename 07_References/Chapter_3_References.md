# Chapter 3 References

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

This document lists the sources used for the methodology, architecture and implementation in
Chapter 3, and records the attribution required by Section 3.6.2 (Software Licensing and
Attribution).

---

## 1. Algorithm Specifications

### National Institute of Standards and Technology (2001)

National Institute of Standards and Technology. (2001). *Advanced Encryption Standard (AES)*.
Federal Information Processing Standards Publication 197.

**DOI:**
https://doi.org/10.6028/NIST.FIPS.197

**Use in Chapter 3:**
Specification for the AES-128 implementation in `04_Source_Code/ciphers/aes128.py`, including the
S-box, key schedule and round structure. The Appendix B and Appendix C.1 known-answer vectors are
used to verify the implementation in `04_Source_Code/tests/test_vectors.py`.

---

### Bogdanov et al. (2007)

Bogdanov, A., Knudsen, L. R., Leander, G., Paar, C., Poschmann, A., Robshaw, M. J. B., Seurin, Y.,
& Vikkelsoe, C. (2007). PRESENT: An ultra-lightweight block cipher. In *Cryptographic Hardware and
Embedded Systems – CHES 2007* (pp. 450–466). Springer.

**DOI:**
https://doi.org/10.1007/978-3-540-74735-2_31

**Use in Chapter 3:**
Specification for the PRESENT-80 implementation in `04_Source_Code/ciphers/present.py`, including
the 4-bit S-box, bit permutation layer and 80-bit key schedule. All four Appendix I known-answer
vectors are used for verification.

---

### Beaulieu et al. (2013)

Beaulieu, R., Shors, D., Smith, J., Treatman-Clark, S., Weeks, B., & Wingers, L. (2013). *The
SIMON and SPECK families of lightweight block ciphers*. IACR Cryptology ePrint Archive,
Report 2013/404.

**Source:**
https://eprint.iacr.org/2013/404

**Use in Chapter 3:**
Specification for the SPECK 64/128 implementation in `04_Source_Code/ciphers/speck.py`, including
the ARX round function, rotation amounts and key schedule. The published test vector is used for
verification.

---

### Turan et al. (2025)

Turan, M. S., McKay, K., Kang, J., Kelsey, J., & Chang, D. (2025). *Ascon-based lightweight
cryptography standards for constrained devices: Authenticated encryption, hash, and extendable
output functions*. National Institute of Standards and Technology, SP 800-232.

**DOI:**
https://doi.org/10.6028/NIST.SP.800-232

**Use in Chapter 3:**
Specification for the ASCON-128 AEAD implementation in `04_Source_Code/ciphers/ascon.py`,
including the 320-bit permutation, round constants, substitution and diffusion layers, and the
initialisation and finalisation procedures.

---

## 2. Methodological Basis

### Radhakrishnan et al. (2024)

Radhakrishnan, I., Jadon, S., & Honnavalli, P. B. (2024). Efficiency and security evaluation of
lightweight cryptographic algorithms for resource-constrained IoT devices. *Sensors, 24*(12),
4008.

**DOI:**
https://doi.org/10.3390/s24124008

**Use in Chapter 3:**
Basis for selecting AES-128 as the comparison baseline, for the choice of evaluation metrics
(execution time, memory utilisation, latency, throughput) and for the expected outcomes stated in
Section 3.9.

---

## 3. Software Licensing and Attribution

In accordance with Section 3.6.2, the following is declared:

**All four cipher implementations in `04_Source_Code/ciphers/` were written specifically for this
study**, working from the published algorithm specifications listed in Section 1 above. No
third-party cryptographic source code was copied into this repository.

The algorithm designs themselves are attributed to their original authors as cited above. AES,
PRESENT, SPECK and ASCON are all published, openly specified algorithms with no licensing
restriction on independent implementation.

**Third-party dependencies:** none. The implementation uses only the Python standard library
(`hashlib`, `csv`, `json`, `statistics`, `time`, `tracemalloc`, `platform`), which is distributed
under the Python Software Foundation License.

**Security declaration:** the implementations are reference implementations written for
performance measurement. They are not constant-time and are not intended for use in protecting
real data. This is stated in the source files and in `04_Source_Code/README.md`.

---

## 4. Standards and Tools Referenced

| Item | Version / Reference | Purpose |
|---|---|---|
| Python | 3.9 or later | Implementation and measurement environment |
| `tracemalloc` | Python standard library | Peak memory measurement |
| `time.perf_counter_ns` | Python standard library | High-resolution monotonic timing |
| Mermaid | GitHub-native rendering | Architecture diagram and flowchart (Figures 3.1 and 3.2) |

---

## 5. Citation Format

All references in this repository follow **APA 7th edition** format, consistent with the
referencing style used in the research proposal and in `Chapter_2_References.md`.
