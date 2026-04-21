# Automation Implementation Notes

## Objective
Automate critical user flows of Sauce Demo to validate functionality and reduce manual effort.

## Tools Used
- Python
- pytest
- Playwright

## Why these tools
- Python: simple and widely used in QA
- pytest: lightweight test framework
- Playwright: reliable browser automation

---

## First Automated Test

### Test Name
test_valid_login

### Purpose
Verify that a user can successfully log in with valid credentials.

### Steps Automated
1. Open Sauce Demo website
2. Enter username: standard_user
3. Enter password: secret_sauce
4. Click Login

### Validation
- Check if user is redirected to inventory page

### Assertion Used
```python
assert "inventory.html" in page.url