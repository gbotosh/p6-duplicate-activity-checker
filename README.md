# P6 Duplicate Activity Description Checker

A simple Python automation tool for checking exact and near-duplicate activity descriptions in Primavera P6 Excel exports.

---

## Purpose

In large Primavera P6 schedules, activity descriptions may be repeated or written in slightly different ways. Manually checking these duplicates can be time-consuming and inconsistent.

This tool automates the process by:

- Detecting exact duplicate activity descriptions
- Detecting near-duplicate activity descriptions using similarity scoring
- Exporting clean Excel reports for schedule QA review

---

## Example

The tool can identify activities such as:

- Install chilled water pipe
- Installation of chilled water piping
- Install CHW pipes

as possible near duplicates.

---

## Input File

Place the Primavera P6 Excel export inside the `data_raw` folder and rename it:

```text
activity_list.xlsx
```

The Excel file must contain at least these two columns:

- Activity ID
- Activity Name

---

## Folder Structure

```text
p6-duplicate-activity-checker/
│
├── data_raw/
│   └── activity_list.xlsx
│
├── outputs/
│
├── check_duplicates.py
├── requirements.txt
├── run_project.bat
├── README.md
└── .gitignore
```

---

## How to Run (Windows)

Double-click:

```text
run_project.bat
```

Or run from Command Prompt:

```bash
run_project.bat
```

---

## What the Tool Checks

### 1. Exact Duplicates

Example:

| Activity ID | Activity Name |
|---|---|
| A1000 | Excavate foundation |
| A1010 | Excavate foundation |

---

### 2. Near Duplicates

Example:

| Activity 1 | Activity 2 | Similarity |
|---|---|---|
| Install chilled water pipe | Installation of chilled water piping | 88% |

The tool uses text similarity logic to identify activities that may represent the same scope of work.

---

## Similarity Threshold

The default near-duplicate threshold is:

```python
SIMILARITY_THRESHOLD = 85
```

Meaning activity descriptions with similarity scores of 85% or higher will be flagged.

---

## Output Files

The tool generates two Excel reports inside the `outputs` folder:

```text
exact_duplicate_activity_names.xlsx
near_duplicate_activity_names.xlsx
```

---

## Technologies Used

- Python
- Pandas
- OpenPyXL
- RapidFuzz

---

## Potential Future Improvements

- WBS-based duplicate analysis
- Activity Code filtering
- NLP-based activity clustering
- Power BI integration
- Full schedule health dashboard integration
- Integration into a broader Project Controls Intelligence Tool (PCIT)

---

## Disclaimer

This repository uses only sample/dummy schedule data.

Do not upload confidential client or project schedules.
