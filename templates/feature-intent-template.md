# Feature Intent

## Objective



## Business Outcome



## Source Story



## Acceptance Criteria



## Constraints



## Existing Patterns to Inspect



## APIs Involved



## Data Involved



## Tests Required



## Evidence Required



---

## Worked Example: Customer Address Form

The blank template above is what you copy for a new feature. Below is a filled-out example for reference — based on a fictional story `CUST-4821`.

### Objective

Create a customer address form that allows users to add or update their mailing address.

### Business Outcome

Customers should be able to maintain accurate mailing information without contacting support.

### Source Story

Jira: CUST-4821

### Acceptance Criteria

1. User can enter street address, city, state, ZIP code, and country.
2. Required fields are validated before submission.
3. ZIP code must be valid for United States addresses.
4. User sees a success message after saving.
5. User sees a clear error message if the save fails.
6. Existing address data is loaded when available.
7. The form follows existing design system patterns.

### Constraints

- Use existing React component library.
- Use existing API client pattern.
- Do not introduce a new form library.
- Must include tests.
- Must meet accessibility expectations.

### Existing Patterns to Inspect

- Existing profile-edit forms in `src/components/forms/`
- Existing address validation utilities, if any
- Existing success/error toast or banner pattern

### APIs Involved

- `PATCH /api/customers/:id/address` (assumed — confirm against actual contract via Confluence or existing code before implementation)

### Data Involved

- Customer mailing address: street, city, state, ZIP, country
- No payment or highly sensitive data involved

### Tests Required

- Happy path: valid address saves successfully
- Validation: required field missing blocks submission
- Validation: invalid US ZIP code blocks submission
- Failure path: API failure shows clear error message
- Existing data loads correctly into the form on mount

### Evidence Required

The final response must include:

- Files changed
- Tests added
- Test results
- Screens or component references used
- API endpoint used
- Risks or unresolved questions
