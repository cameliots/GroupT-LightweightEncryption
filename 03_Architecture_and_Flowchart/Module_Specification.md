# Module Specification

This document specifies the interface of each architectural module shown in Figure 3.1 and maps
it to the corresponding file in `../04_Source_Code/`.

---

## 1. Common Cipher Interface

Every cipher in the Encryption / Decryption Algorithm Module implements the same interface. This
is what makes the comparison valid: the Experimental Control Module calls all four algorithms
through identical calls, so no algorithm receives a different calling convention or a different
amount of surrounding framework work.

```python
class Cipher:
    name: str          # "AES-128", "PRESENT-80", "SPECK-64/128", "ASCON-128"
    key_size: int      # key length in bytes
    nonce_size: int    # nonce / IV length in bytes
    category: str      # "Conventional" or "Lightweight"

    def encrypt(self, key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
        ...

    def decrypt(self, key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
        ...
```

| Cipher | File | Block | Key | Mode | Category |
|---|---|---|---|---|---|
| AES-128 | `ciphers/aes128.py` | 128-bit | 128-bit | CTR | Conventional |
| PRESENT-80 | `ciphers/present.py` | 64-bit | 80-bit | CTR | Lightweight |
| SPECK 64/128 | `ciphers/speck.py` | 64-bit | 128-bit | CTR | Lightweight |
| ASCON-128 | `ciphers/ascon.py` | 64-bit rate | 128-bit | AEAD | Lightweight |

**Note on modes.** AES, PRESENT and SPECK are block ciphers and are run in **CTR (counter)
mode** so that all three process arbitrary-length payloads under the same construction. ASCON is
an authenticated encryption scheme and is run in its native AEAD mode, which additionally
produces a 16-byte authentication tag. This difference is a genuine property of the algorithms
rather than an inconsistency in the experiment, and is reported as such in the results:
ASCON's output is 16 bytes longer because it provides integrity as well as confidentiality.

---

## 2. Experimental Control Module

**File:** `harness/control_module.py`

| Responsibility | Detail |
|---|---|
| Configuration | Holds `ALGORITHMS`, `DATA_SIZES`, `TRIALS_PER_CONFIGURATION`, `WARMUP_ITERATIONS` |
| Key material | Generates one fixed key and nonce per algorithm, reused across all trials so key generation cost does not enter the measurement |
| Sequencing | Iterates algorithm → data size → trial, matching Figure 3.2 |
| Input supply | Passes the identical plaintext buffer to every algorithm at a given size |
| Validation | Compares recovered plaintext against the original and flags invalid trials |

---

## 3. Performance Monitoring Unit

**File:** `harness/monitor.py`

| Metric | Method | Unit |
|---|---|---|
| Encryption time | `time.perf_counter_ns()` around the encrypt call only | milliseconds (ms) |
| Decryption time | `time.perf_counter_ns()` around the decrypt call only | milliseconds (ms) |
| Peak memory | `tracemalloc` peak allocation during the operation | kilobytes (KB) |
| Throughput | `payload_bytes × 8 ÷ elapsed_seconds ÷ 1_000_000` | megabits per second (Mbps) |

The timer brackets only the cipher call. Data generation, logging and validation happen outside
the timed region so they do not contaminate the measurement.

---

## 4. Data Logger

**File:** `harness/data_logger.py`

Writes one row per trial. Columns:

| Column | Description |
|---|---|
| `algorithm` | Cipher name |
| `category` | Conventional or Lightweight |
| `data_size_label` | 1KB / 10KB / 100KB / 1MB |
| `data_size_bytes` | Payload size in bytes |
| `trial` | Trial number, 1–30 |
| `encryption_time_ms` | Encryption time |
| `decryption_time_ms` | Decryption time |
| `encrypt_peak_memory_kb` | Peak memory during encryption |
| `decrypt_peak_memory_kb` | Peak memory during decryption |
| `encrypt_throughput_mbps` | Encryption throughput |
| `decrypt_throughput_mbps` | Decryption throughput |
| `ciphertext_bytes` | Length of ciphertext produced |
| `roundtrip_valid` | Whether decryption recovered the original plaintext |

---

## 5. Analysis and Comparison Module

**File:** `harness/analysis.py`

| Output | Description |
|---|---|
| Summary table | Mean and standard deviation of every metric, per algorithm per data size |
| Baseline comparison | Each lightweight algorithm expressed as a ratio relative to AES-128 |
| Markdown report | Written to `06_Results_or_Expected_Output/` |

---

## 6. Environment Record

**File:** `harness/environment.py`

Records the platform, processor, Python version and timer resolution into the results metadata.
This exists because Section 2.4.2 identifies undocumented experimental environments as a cause
of non-comparable results in prior work. Recording the environment alongside the measurements
allows anyone re-running the experiment to state whether their conditions matched.
