# Data / Sample Input

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## Purpose of This Folder

This folder documents the data collection procedure (Section 3.5) and contains the generator for
the synthetic test data used as encryption input.

---

## Data Collection Approach

The data collection procedure adopted in this study is **experimental rather than survey-based**,
since the research does not involve human participants or organizational data. Instead, data is
collected through the controlled execution of the selected lightweight encryption algorithms
(AES, PRESENT, SPECK and ASCON) within the experimental environment described in Chapter 3.

To reflect realistic IoT workloads, sample test data of varying sizes is used as encryption input
rather than a single fixed input. This allows the study to observe how each algorithm behaves as
the volume of processed data increases, which is relevant because IoT devices commonly handle
small to moderate data payloads such as sensor readings, status updates and short control
messages.

---

## Table 3.1: Data Collection Parameters

| Parameter | Description | Values / Settings | Purpose |
|---|---|---|---|
| **Test data sizes** | Sample plaintext files representing typical IoT payloads | 1 KB, 10 KB, 100 KB, 1 MB | Simulate varying payload workloads |
| **Data type** | Synthetic sensor-style data | Deterministically generated sample data | Avoid use of confidential data |
| **Number of trials** | Repeated runs per algorithm per data size | 30 repetitions | Improve reliability |
| **Execution environment** | Hardware/software used to run all algorithms | Same machine, idle background state | Ensure fair and consistent comparison |
| **Recorded metrics** | Values captured automatically during each run | Encryption and decryption time, memory usage, throughput | Provide quantitative basis |

---

## Contents

| File | Description |
|---|---|
| `generate_test_data.py` | Generates the four test payloads and a readable sample |
| `sample_sensor_records.json` | 20 human-readable synthetic sensor records, showing what the payloads represent |
| `generated/` | Generated binary payloads (git-ignored — reproducible from the script) |

---

## Usage

```bash
cd 05_Data_or_Sample_Input

python generate_test_data.py            # write all four payload sizes
python generate_test_data.py --preview  # show sample sensor records
```

---

## Why the Data Is Deterministic

The payloads are derived from a fixed seed using a SHA-256 hash chain rather than from a random
source. This has two consequences that matter for the study:

1. **All four algorithms receive byte-identical input.** If each algorithm were given different
   random data, any difference in the measurements could be caused by the input rather than by
   the algorithm. The seed removes that possibility.

2. **The experiment is reproducible.** Anyone re-running the study on another machine encrypts
   exactly the same bytes, which is required by the transparency commitment in Section 3.6.3.

The generated payloads are not committed to the repository because they are fully reproducible
from the script, and committing a 1 MB binary would add nothing that the generator does not
already provide.

---

## Ethical Position

The study relies entirely on synthetic and sample test data generated for the purpose of the
experiment. **No confidential, personal or organisational data is collected, stored or processed
at any stage of the research** (Section 3.6.1). The study therefore does not require informed
consent procedures.

---

## Note on Repetition

Each algorithm is executed for 30 repeated trials on every test data size under identical system
conditions. Repeating each trial is intended to reduce the influence of random system
fluctuations and to allow calculation of average values and standard deviation for each recorded
metric.

Before the measured trials, a small number of unmeasured warm-up iterations are performed, because
the first execution of a code path in an interpreted runtime includes one-time costs that are not
representative of steady-state performance. The same warm-up procedure is applied identically to
all four algorithms.
