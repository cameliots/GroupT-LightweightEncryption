# Evaluation Metrics

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## 1. Introduction

The performance of lightweight encryption algorithms can be evaluated using several technical and resource-related metrics.

Based on the reviewed literature, this research will focus on execution time, memory utilization, throughput, latency, energy consumption and security characteristics.

These metrics will be used to compare AES, PRESENT, SPECK and ASCON under consistent experimental conditions.

---

## 2. Execution Time

Execution time refers to the amount of time required to perform an encryption or decryption operation.

It is an important metric for resource-constrained IoT devices because longer processing times can increase computational workload and delay data transmission.

### Measurement

The execution time will be measured for:

- Encryption
- Decryption

### Interpretation

A lower execution time indicates faster cryptographic processing.

---

## 3. Memory Utilization

Memory utilization refers to the amount of memory required by an encryption algorithm during execution.

IoT devices may have limited RAM and storage capacity, making memory efficiency an important consideration.

### Measurement

Memory usage will be recorded during the execution of each selected algorithm.

### Interpretation

Lower memory utilization indicates better suitability for devices with limited memory resources.

---

## 4. Throughput

Throughput measures the amount of data that can be processed within a specific period.

It can be used to determine the efficiency of an encryption algorithm when processing different input sizes.

### Measurement

Throughput can be calculated using:

**Throughput = Data Size / Execution Time**

The result can be represented using units such as bytes per second (B/s) or kilobytes per second (KB/s).

### Interpretation

Higher throughput indicates that an algorithm can process data more efficiently.

---

## 5. Latency

Latency refers to the delay introduced during cryptographic processing.

Low latency is important for IoT applications that require rapid communication or near real-time responses.

### Measurement

Latency will be determined by measuring the time taken for the cryptographic operation to complete.

### Interpretation

Lower latency indicates faster response and reduced processing delay.

---

## 6. Energy Consumption

Energy consumption refers to the amount of energy required to perform encryption and decryption.

This metric is particularly important for battery-powered IoT devices.

### Measurement

Where suitable hardware measurement facilities are available, energy consumption will be measured during cryptographic operations.

If direct hardware energy measurement is not available, the limitation will be documented and energy-related conclusions will be made cautiously.

### Interpretation

Lower energy consumption indicates better suitability for battery-powered devices.

---

## 7. Security

Security evaluates the protection provided by each encryption algorithm.

The comparison will consider characteristics such as:

- Key size
- Block or state size
- Confidentiality protection
- Integrity or authentication capability
- Known security considerations

Security will not be evaluated only through performance measurements.

An algorithm with high performance but insufficient security would not necessarily be the most suitable choice for an IoT application.

---

## 8. Summary of Evaluation Metrics

| Metric | Measurement | Desired Result | Importance to IoT |
|---|---|---|---|
| Execution Time | Time required for encryption/decryption | Lower | Reduces processing delay |
| Memory Utilization | Memory required during execution | Lower | Important for limited RAM |
| Throughput | Data processed per unit of time | Higher | Improves data processing efficiency |
| Latency | Delay introduced by cryptographic processing | Lower | Important for responsive applications |
| Energy Consumption | Energy required for cryptographic operations | Lower | Extends battery operation |
| Security | Security characteristics and protection | Stronger | Protects IoT data and communication |

---

## 9. Consistent Evaluation Conditions

To ensure a fair comparison, the selected algorithms should be tested using consistent conditions.

The proposed evaluation will aim to maintain the same:

- Hardware platform
- Software environment
- Input data
- Input sizes
- Number of test repetitions
- Encryption/decryption procedures
- Measurement methods

Using consistent conditions can reduce the influence of external factors and make the comparison more meaningful.

---

## 10. Input Size Consideration

Different input sizes may affect the performance of encryption algorithms.

Therefore, multiple input sizes may be tested to observe how algorithm performance changes as the amount of data increases.

For example:

| Test | Input Size |
|---|---:|
| Test 1 | 1 KB |
| Test 2 | 10 KB |
| Test 3 | 100 KB |
| Test 4 | 1 MB |

The final input sizes may be adjusted according to the selected experimental platform and available resources.

---

## 11. Comparison Approach

The collected measurements will be organised into tables and graphs.

The algorithms will then be compared based on each evaluation metric.

For example:

**Execution Time**

Lower values indicate faster processing.

**Memory Utilization**

Lower values indicate better memory efficiency.

**Throughput**

Higher values indicate better data processing performance.

**Latency**

Lower values indicate faster response.

**Energy Consumption**

Lower values indicate better energy efficiency.

**Security**

Stronger security characteristics indicate better protection, provided that the resource requirements remain suitable for the target IoT environment.

---

## 12. Expected Evaluation Output

The evaluation is expected to produce:

1. Encryption execution time results.
2. Decryption execution time results.
3. Memory utilization results.
4. Throughput measurements.
5. Latency measurements.
6. Energy consumption measurements where applicable.
7. Security comparison.
8. Comparative tables and graphs.

These results will be used to identify the strengths and limitations of AES, PRESENT, SPECK and ASCON.

---

## 13. Conclusion

The selected evaluation metrics provide a balanced approach to comparing lightweight encryption algorithms.

Performance metrics such as execution time, throughput and latency measure computational efficiency, while memory utilization and energy consumption evaluate resource requirements.

Security characteristics provide an additional perspective to ensure that performance improvements are considered together with cryptographic protection.

Using these metrics under consistent experimental conditions will support a more reliable comparison of AES, PRESENT, SPECK and ASCON for resource-constrained IoT devices.
