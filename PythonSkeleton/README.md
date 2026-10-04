# Python Learning Projects

This repository contains two beginner-friendly Python projects for practising core language concepts and data structures.

## Projects

### 1. Python Data Structures Lab

An interactive Streamlit app for exploring lists, dictionaries, sets, and tuples. Choose a data structure, perform an operation, and see the live value update in the sidebar.

Run it with:

```powershell
streamlit run datastructure.py
```

The app opens in your browser. Use **Reset all variables** in the sidebar to restore the starting examples.

### 2. College Student Registration System

A menu-driven terminal program that demonstrates:

- Lists, dictionaries, tuples, and sets
- Functions, conditions, and loops
- JSON persistence and CSV export

Run it with:

```powershell
python pythonskeleton.py
```

Choose an option from the numbered menu to register, view, search for, or check a student's eligibility. The program can save records to `students.json` and export them to `students.csv`.

## Setup

### Prerequisites

- Python 3.9 or later
- `pip` (included with standard Python installations)

### Install dependencies

From the repository folder, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Then install the required packages:

```powershell
python -m pip install -r requirements.txt
```

If PowerShell prevents virtual-environment activation, use the full Python path instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\streamlit.exe run datastructure.py
```

## Repository layout

```text
datastructure.py     # Streamlit data-structures lab
pythonskeleton.py    # Terminal student registration system
requirements.txt     # Python dependencies
students.json        # Saved student records (created/updated by the terminal app)
students.csv         # Student-record export (created/updated by the terminal app)
```

## Notes

- The data-structures lab keeps changes only for the current browser session; reset it whenever you want to start again.
- The registration system loads `students.json` when it starts, so saved records remain available between runs.
- CSV and JSON files are sample/output data. You can delete their contents or replace them if you want to begin with your own records.
