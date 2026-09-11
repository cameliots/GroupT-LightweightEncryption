# Literature Review

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## 1. Introduction

The Internet of Things (IoT) consists of interconnected devices that collect, process and exchange data through communication networks. IoT devices are widely used in applications such as smart homes, healthcare, smart agriculture, environmental monitoring and industrial systems.

However, many IoT devices operate with limited processing capability, memory, storage capacity and energy resources. These limitations can affect the implementation and performance of conventional cryptographic algorithms.

Lightweight cryptography provides an approach for protecting information while reducing computational and resource requirements. Therefore, selecting suitable lightweight encryption algorithms is important for resource-constrained IoT environments.

This literature review examines four selected cryptographic algorithms:

- AES
- PRESENT
- SPECK
- ASCON

The review focuses on their characteristics, performance considerations, resource requirements and suitability for resource-constrained IoT environments.

---

## 2. Resource Constraints in IoT

Resource-constrained IoT devices commonly operate with limited hardware and computational resources.

### 2.1 Processing Capability

Many IoT devices use low-power processors with limited computational capability. Cryptographic operations that require significant processing can increase execution time and computational overhead.

### 2.2 Memory

IoT devices may have limited RAM and storage capacity. Cryptographic algorithms with higher memory requirements may therefore be less suitable for highly constrained devices.

### 2.3 Energy

Many IoT devices operate using batteries or other limited energy sources. Computationally intensive cryptographic operations can increase energy consumption and reduce operating time.

### 2.4 Latency

IoT applications may require fast communication and processing. Additional cryptographic processing can increase system latency and affect application performance.

These constraints demonstrate the importance of evaluating encryption algorithms based on both performance and resource-efficiency characteristics.

---

## 3. Selected Lightweight Encryption Algorithms

### 3.1 Advanced Encryption Standard (AES)

Advanced Encryption Standard (AES) is a widely adopted symmetric block cipher. AES supports key sizes of 128, 192 and 256 bits.

AES provides strong security and is commonly used as a benchmark when evaluating cryptographic implementations. However, its resource requirements may become an important consideration when implemented on highly constrained IoT devices.

Therefore, AES is included in this research as an established encryption algorithm for comparison with lightweight alternatives.

---

### 3.2 PRESENT

PRESENT is an ultra-lightweight block cipher designed for highly constrained environments.

PRESENT uses a 64-bit block size and supports 80-bit and 128-bit keys. Its compact design focuses on reducing hardware requirements while maintaining suitable security characteristics.

PRESENT is therefore relevant to IoT environments where hardware resources are highly limited.

---

### 3.3 SPECK

SPECK is a family of lightweight block ciphers designed for efficient operation on constrained computing platforms.

The algorithm uses simple operations that support efficient software implementation and low computational overhead.

SPECK is therefore relevant for evaluating lightweight encryption performance on resource-constrained IoT devices.

---

### 3.4 ASCON

ASCON is a lightweight cryptographic family designed for constrained devices. It provides authenticated encryption, which can provide confidentiality and integrity within a single cryptographic construction.

ASCON has been standardised by the National Institute of Standards and Technology (NIST) for lightweight cryptography.

Its lightweight design and authenticated encryption capability make ASCON particularly relevant to modern resource-constrained IoT applications.

---

## 4. Comparative Literature Analysis

Previous research demonstrates that different cryptographic algorithms have different performance and resource-efficiency characteristics.

Radhakrishnan et al. (2024) evaluated AES-128, SPECK and ASCON on resource-constrained IoT boards. The study considered execution time, memory utilization, latency, throughput and security robustness.

The study demonstrated that algorithm performance can vary depending on the hardware platform and implementation environment. SPECK showed strong performance in the evaluated environment.

Other research introduced PRESENT as an ultra-lightweight block cipher designed for constrained hardware, while research on the SPECK family demonstrated its suitability for efficient cryptographic operations on constrained platforms.

More recently, NIST standardised the ASCON family for lightweight cryptography for constrained devices.

These studies provide useful evidence for selecting algorithms and evaluation criteria for the proposed research.

---

## 5. Comparison of Selected Algorithms

| Algorithm | Main Characteristics | Lightweight Focus | IoT Relevance |
|---|---|---|---|
| AES | Established symmetric block cipher; 128, 192 and 256-bit keys | General-purpose encryption | Useful as a security and performance benchmark |
| PRESENT | 64-bit block; 80/128-bit keys; compact design | Hardware efficiency | Suitable for highly constrained hardware |
| SPECK | Lightweight block cipher family with efficient operations | Software efficiency | Suitable for constrained processors |
| ASCON | Lightweight authenticated encryption | Resource-efficient authenticated encryption | Suitable for modern constrained IoT devices |

The algorithms represent different design approaches and therefore provide a useful basis for comparative evaluation.

---

## 6. Evaluation Metrics

Based on the reviewed literature, several metrics are important for evaluating lightweight encryption algorithms.

### 6.1 Execution Time

Execution time measures the time required to perform encryption and decryption.

A lower execution time indicates faster cryptographic processing and may reduce the processing burden on constrained IoT devices.

### 6.2 Memory Utilization

Memory utilization measures the amount of memory required during cryptographic processing.

Lower memory requirements are important because many IoT devices have limited RAM and storage.

### 6.3 Throughput

Throughput measures the amount of data processed within a specific period.

Higher throughput indicates that an algorithm can process data more efficiently.

### 6.4 Latency

Latency measures the delay introduced by cryptographic processing.

Lower latency is important for IoT applications that require fast communication or near real-time responses.

### 6.5 Energy Consumption

Energy consumption measures the energy required during cryptographic operations.

Lower energy consumption is desirable for battery-powered IoT devices because it can help extend device operating time.

### 6.6 Security

Security considers the ability of an algorithm to protect information against unauthorised access and cryptographic attacks.

Performance and resource efficiency should be considered together with security when selecting an encryption algorithm.

---

## 7. Research Gap

The literature review identifies a major research gap in the consistent comparison of lightweight encryption algorithms.

Existing studies may use different:

- Hardware platforms
- Software environments
- Input sizes
- Test workloads
- Implementation techniques
- Evaluation metrics
- Experimental conditions

These differences can make direct comparison between algorithms difficult.

For example, an algorithm may perform efficiently on one hardware platform but produce different results on another platform. Similarly, different input sizes and implementation techniques can affect execution time, memory usage and throughput.

Furthermore, previous studies may focus on only a subset of the algorithms considered in this research.

Therefore, there is a need for a comparative evaluation of AES, PRESENT, SPECK and ASCON using consistent experimental conditions and common evaluation metrics.

---

## 8. Proposed Research Response to the Gap

The proposed research addresses the identified gap by:

1. Selecting AES, PRESENT, SPECK and ASCON based on findings from existing literature.
2. Implementing the selected algorithms in a controlled experimental environment.
3. Using consistent test conditions for the selected algorithms.
4. Applying common input data for comparative testing.
5. Measuring common performance and resource-efficiency metrics.
6. Comparing the results using a unified evaluation approach.

This approach is intended to provide a clearer and more consistent comparison of the selected algorithms.

---

## 9. Connection to Research Objectives

### Objective 1

**To identify and select lightweight encryption algorithms suitable for resource-constrained IoT environments based on findings from existing literature.**

The literature review provides the basis for selecting AES, PRESENT, SPECK and ASCON for comparative evaluation.

### Objective 2

**To implement the selected lightweight encryption algorithms in a controlled experimental environment using consistent test conditions.**

The research gap demonstrates the importance of using consistent experimental conditions when comparing different cryptographic algorithms.

### Objective 3

**To evaluate and compare the selected algorithms based on defined performance and resource-efficiency metrics.**

Previous studies provide the basis for evaluating execution time, memory utilization, throughput, latency, energy consumption and security.

---

## 10. Contribution to Methodology

The findings from the literature review will be used to guide the methodology and experimental design.

The general research process derived from the literature is:

1. Select the four algorithms.
2. Prepare common test inputs.
3. Implement the algorithms.
4. Apply consistent experimental conditions.
5. Perform encryption and decryption.
6. Measure execution time.
7. Measure memory utilization.
8. Measure throughput and latency.
9. Evaluate energy consumption where applicable.
10. Compare security characteristics.
11. Analyse the collected results.
12. Determine the relative strengths and limitations of each algorithm.

The final hardware platform, software environment and detailed testing procedures will be defined in the methodology section of the research.

---

## 11. Conclusion

The literature review demonstrates that lightweight cryptography is important for protecting data in resource-constrained IoT environments.

AES provides an established encryption benchmark, while PRESENT focuses on compact lightweight hardware design. SPECK provides efficient lightweight operations for constrained computing platforms, while ASCON provides modern lightweight authenticated encryption.

The reviewed studies also demonstrate that algorithm performance can depend on hardware, implementation and experimental conditions.

The main research gap is therefore the difficulty of making a consistent comparison between different algorithms when studies use different conditions and evaluation methods.

To address this gap, the proposed research will comparatively evaluate AES, PRESENT, SPECK and ASCON using consistent experimental conditions and common evaluation metrics.

The findings from this literature review will provide the foundation for the methodology, experimental design and evaluation process in the subsequent stages of the research.
