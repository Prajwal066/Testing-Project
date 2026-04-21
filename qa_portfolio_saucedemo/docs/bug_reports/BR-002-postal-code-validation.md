# BR-002 — Checkout accepts invalid postal code values

## Related Test Case
TC-015

## Summary
Postal code field accepts alphabetic characters and excessively long values without validation.

## Environment
- Browser: Chrome
- OS: Windows
- Application: Sauce Demo

## Preconditions
- User is logged in
- Product is added to cart

## Steps to Reproduce
1. Go to cart
2. Click Checkout
3. Enter valid first name and last name
4. Enter "ABCDE123456789" as postal code
5. Click Continue

## Actual Result
Form accepts invalid postal code and allows user to proceed.

## Expected Result
System should validate postal code format and reject invalid input.

## Related Test Case
TC-015

## Severity
Medium

## Priority
P2