# BR-001 — Checkout accepts invalid characters in name fields

## Summary
Checkout form allows numeric and special characters in First Name and Last Name fields.

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
3. Enter "123@#" in First Name
4. Enter "456@#" in Last Name
5. Enter any postal code
6. Click Continue

## Actual Result
Form accepts invalid name input and allows user to proceed.

## Expected Result
System should reject invalid characters or show validation error.

## Related Test Case
TC-014

## Severity
Medium

## Priority
P2
