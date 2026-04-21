# QA Automation Setup Notes

## Objective
Set up a Python test automation environment for the Sauce Demo QA portfolio project.

## Why automation was added
Manual testing shows understanding of QA process, but automation demonstrates the ability to:
- repeat important checks quickly
- reduce repetitive manual work
- validate core flows consistently
- support junior QA / test automation roles

## Tools chosen

### Python
Chosen because it is widely used in QA automation, and suitable for pytest-based frameworks.

### pytest
Chosen because it is simple, lightweight, and commonly used for organizing and running automated tests.

### Playwright
Chosen because it is modern, reliable for browser automation.

### Virtual Environment (.venv)
Chosen to isolate project dependencies and avoid package/version conflicts with other Python projects.

---

## Steps completed

### 1. Created project structure
Created the following folders:
- `docs/`
- `automation/`

Inside `automation/`, created:
- `tests/`
- `pages/`
- `requirements.txt`
- `pytest.ini`
- `conftest.py`

### Why
This separates:
- documentation/manual QA artifacts
- automation code
- reusable page objects
- test configuration

---

### 2. Created virtual environment and activate it 
Command used:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the required packages 
Command used : 
```bash
python -m pip install pytest
python -m pip install playwright
python -m pip install pytest-playwright
python-m playwright install 
```

- pytest - to run the test 
- playwright - to automate the browser actions
- pytest-playwright to integrate playwright with pytest 
- and finally install browser binaries (chrome.exe or msedge.exe) for automation