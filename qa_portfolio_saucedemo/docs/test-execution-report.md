# Test Execution Report — Sauce Demo

## 1. Execution Details
- Tester: Prajwal  
- Date: 2026-03-31  
- Application: Sauce Demo (Swag Labs)  
- Environment:
  - OS: Windows  
  - Browser: Chrome  

---

## 2. Scope of Testing
The following modules were tested:
- Login functionality  
- Product (Inventory) page  
- Cart functionality  
- Checkout process  

---

## 3. Test Summary

| Metric | Count |
|------|------|
| Total Test Cases | 15 |
| Executed | 15 |
| Passed | 12 |
| Failed | 3 |
| Blocked | 0 |

---

## 4. Passed Test Cases
The following functionalities worked as expected:
- Valid login  
- Invalid login (wrong credentials handling)  
- Product listing and visibility  
- Add to cart  
- Remove from cart  
- Cart item count update  
- Checkout with valid inputs  
- Order completion  

---

## 5. Failed Test Cases

| Test Case ID | Description | Bug ID |
|-------------|------------|--------|
| TC-003 | Login with trailing space in username | N/A (edge case behavior) | Priority: Low
| TC-014 | Invalid characters accepted in name fields | BR-001 |
| TC-015 | Invalid postal code accepted | BR-002 |

---

## 6. Defect Summary

### BR-001 — Invalid name input accepted
- First Name and Last Name fields accept numbers and special characters without validation.

### BR-002 — Invalid postal code accepted
- Postal code field accepts alphabetic and excessively long values without validation.

---

## 7. Observations

- Core functionalities such as login, cart operations, and checkout flow are working correctly.
- Validation mechanisms for input fields are weak or missing.
- System does not trim trailing spaces in username input, leading to login failure (edge case).

---

## 8. Conclusion

The application is functionally stable for core user flows.  
However, improvements are required in input validation and handling of edge cases to enhance data integrity and user experience.

---

## 9. Recommendations

- Implement validation for name fields (restrict numeric/special characters)
- Add format validation for postal code
- Trim leading/trailing spaces in login inputs