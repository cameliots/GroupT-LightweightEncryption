# Architecture and Flowchart

## Research Title

**A Comparative Evaluation of Lightweight Encryption Algorithms for Resource-Constrained IoT Devices**

---

## Purpose of This Folder

This folder documents the methodology, the selected development model, the experimental
architecture and the experimental process flowchart for the proposed research. It supports
**Chapter 3 (Part A)** of the research proposal and relates to Research Objective **RO2**
(implementation of the selected algorithms in a controlled experimental environment).

---

## Contents

| File | Description |
|---|---|
| `Research_Methodology.md` | Research methodology and quantitative approach (Section 3.1) |
| `Development_Model.md` | Comparison of development models and justification of the selected model (Section 3.2) |
| `Methodology_Phases.md` | The six methodology phases and their mapping to the research objectives (Section 3.3) |
| `Experimental_Architecture.md` | Proposed experimental architecture, Figure 3.1 (Section 3.4.1) |
| `Experimental_Process_Flowchart.md` | Experimental process flowchart, Figure 3.2 (Section 3.4.2) |
| `Module_Specification.md` | Specification of each architectural module and its mapping to the source code |

---

## Relationship to the Source Code

The architecture described in this folder is implemented in `../04_Source_Code/`.
Each architectural component in Figure 3.1 corresponds to a module in the implementation:

| Architectural Component | Implementation Module |
|---|---|
| Experimental Control Module | `04_Source_Code/harness/control_module.py` |
| Encryption / Decryption Algorithm Module | `04_Source_Code/ciphers/` |
| Performance Monitoring Unit | `04_Source_Code/harness/monitor.py` |
| Data Logger | `04_Source_Code/harness/data_logger.py` |
| Analysis and Comparison Module | `04_Source_Code/harness/analysis.py` |

---

## Diagram Format

The diagrams in this folder are written in **Mermaid**, which GitHub renders directly in the
browser. No image files or external tools are required to view them.

---

## Contributor

| Name | Student ID | Contribution |
|---|---|---|
| MUHAMAD AZIM SYAFAWI BIN ABDULLAH | 52215124282 | Chapter 3 (Part A): Research Methodology, Development Model, Methodology Phases, Architecture Diagram and Flowchart |
