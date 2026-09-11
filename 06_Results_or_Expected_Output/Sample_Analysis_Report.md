# Experimental Results

Total trials recorded: **80**  
Invalid trials excluded: **0**  
Algorithms evaluated: **4**  
Data sizes: **1KB, 10KB**

---

## 1. Measured Metrics

### Encryption Time (ms)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 8.9633 ± 0.2594 | 85.5866 ± 1.1815 |
| ASCON-128 | 41.2535 ± 7.5709 | 381.0814 ± 8.5441 |
| PRESENT-80 | 329.6388 ± 6.0400 | 3280.3383 ± 52.2149 |
| SPECK-64/128 | 19.6380 ± 2.5617 | 184.3964 ± 10.7040 |

_Values are mean ± standard deviation across all valid trials._

### Decryption Time (ms)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 9.0463 ± 0.3084 | 86.5651 ± 1.5601 |
| ASCON-128 | 39.2704 ± 1.8196 | 382.4908 ± 17.6745 |
| PRESENT-80 | 326.7254 ± 4.6639 | 3255.6223 ± 76.3340 |
| SPECK-64/128 | 18.5081 ± 0.7225 | 185.1952 ± 14.5136 |

_Values are mean ± standard deviation across all valid trials._

### Encrypt Peak Memory (KB)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 5.7490 ± 0.0000 | 21.3940 ± 0.0000 |
| ASCON-128 | 4.6000 ± 0.0000 | 40.8690 ± 0.0000 |
| PRESENT-80 | 3.8520 ± 0.0000 | 21.8830 ± 0.0000 |
| SPECK-64/128 | 3.5700 ± 0.0000 | 21.6020 ± 0.0000 |

_Values are mean ± standard deviation across all valid trials._

### Decrypt Peak Memory (KB)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 5.7490 ± 0.0000 | 21.3940 ± 0.0000 |
| ASCON-128 | 3.6720 ± 0.0000 | 30.9410 ± 0.0000 |
| PRESENT-80 | 3.8520 ± 0.0000 | 21.8830 ± 0.0000 |
| SPECK-64/128 | 3.5700 ± 0.0000 | 21.6020 ± 0.0000 |

_Values are mean ± standard deviation across all valid trials._

### Encrypt Throughput (Mbps)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 0.9146 ± 0.0255 | 0.9573 ± 0.0132 |
| ASCON-128 | 0.2028 ± 0.0256 | 0.2151 ± 0.0048 |
| PRESENT-80 | 0.0249 ± 0.0005 | 0.0250 ± 0.0004 |
| SPECK-64/128 | 0.4225 ± 0.0453 | 0.4455 ± 0.0229 |

_Values are mean ± standard deviation across all valid trials._

### Decrypt Throughput (Mbps)

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 0.9065 ± 0.0310 | 0.9466 ± 0.0169 |
| ASCON-128 | 0.2090 ± 0.0089 | 0.2146 ± 0.0091 |
| PRESENT-80 | 0.0251 ± 0.0004 | 0.0252 ± 0.0006 |
| SPECK-64/128 | 0.4432 ± 0.0171 | 0.4444 ± 0.0294 |

_Values are mean ± standard deviation across all valid trials._

---

## 2. Comparison Against the Baseline

### Encryption Time (ms) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 4.60× | 4.45× |
| PRESENT-80 | 36.78× | 38.33× |
| SPECK-64/128 | 2.19× | 2.15× |

_Ratio of each algorithm to the AES-128 baseline; below 1.00× is better._

### Decryption Time (ms) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 4.34× | 4.42× |
| PRESENT-80 | 36.12× | 37.61× |
| SPECK-64/128 | 2.05× | 2.14× |

_Ratio of each algorithm to the AES-128 baseline; below 1.00× is better._

### Encrypt Peak Memory (KB) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 0.80× ✅ | 1.91× |
| PRESENT-80 | 0.67× ✅ | 1.02× |
| SPECK-64/128 | 0.62× ✅ | 1.01× |

_Ratio of each algorithm to the AES-128 baseline; below 1.00× is better._

### Decrypt Peak Memory (KB) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 0.64× ✅ | 1.45× |
| PRESENT-80 | 0.67× ✅ | 1.02× |
| SPECK-64/128 | 0.62× ✅ | 1.01× |

_Ratio of each algorithm to the AES-128 baseline; below 1.00× is better._

### Encrypt Throughput (Mbps) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 0.22× | 0.22× |
| PRESENT-80 | 0.03× | 0.03× |
| SPECK-64/128 | 0.46× | 0.47× |

_Ratio of each algorithm to the AES-128 baseline; above 1.00× is better._

### Decrypt Throughput (Mbps) — relative to AES-128

| Algorithm | 1KB | 10KB |
|---|---|---|
| AES-128 | 1.00× (baseline) | 1.00× (baseline) |
| ASCON-128 | 0.23× | 0.23× |
| PRESENT-80 | 0.03× | 0.03× |
| SPECK-64/128 | 0.49× | 0.47× |

_Ratio of each algorithm to the AES-128 baseline; above 1.00× is better._

---

## 3. Ciphertext Expansion

| Algorithm | Data Size | Plaintext (B) | Ciphertext (B) | Overhead (B) |
|---|---|---|---|---|
| AES-128 | 10KB | 10240 | 10240 | 0 |
| AES-128 | 1KB | 1024 | 1024 | 0 |
| ASCON-128 | 10KB | 10240 | 10256 | 16 |
| ASCON-128 | 1KB | 1024 | 1040 | 16 |
| PRESENT-80 | 10KB | 10240 | 10240 | 0 |
| PRESENT-80 | 1KB | 1024 | 1024 | 0 |
| SPECK-64/128 | 10KB | 10240 | 10240 | 0 |
| SPECK-64/128 | 1KB | 1024 | 1024 | 0 |

_ASCON-128 adds a 16-byte authentication tag because it provides integrity as well as confidentiality. The CTR-mode block ciphers add no overhead._