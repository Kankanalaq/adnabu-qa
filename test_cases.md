# Task 1 – Test Cases: AdNabuTestStore

---

## A) Product Search

### TC-PS-01 | Search with a Valid Product Name *(Positive)*
- **Steps:** Enter a valid keyword (e.g., "shirt") in the search bar → press Enter
- **Expected Result:**
  - Search results page loads successfully
  - One or more matching products are displayed with name, image, and price

---

### TC-PS-02 | Search with a Non-Existent Product *(Negative)*
- **Steps:** Enter a keyword that has no matching product (e.g., "xyzabc999") → press Enter
- **Expected Result:**
  - Search results page loads
  - A "no results found" (or similar) message is displayed
  - No product cards appear; page does not crash

---

### TC-PS-03 | Search with Special Characters *(Edge Case)*
- **Steps:** Enter special characters (e.g., `@#$%^&*`) in the search bar → press Enter
- **Expected Result:**
  - Application handles the input gracefully without throwing an error or 500 page
  - Either a "no results" message is shown or the input is sanitised
  - Page remains functional after the search

---

## B) Add to Cart

### TC-AC-01 | Add an In-Stock Product to Cart *(Positive)*
- **Steps:** Open any in-stock product page → click "Add to Cart"
- **Expected Result:**
  - Product is added to the cart successfully
  - Cart count in the header increments by 1
  - A success notification / cart drawer appears showing the correct product and quantity

---

### TC-AC-02 | Attempt to Add an Out-of-Stock Product *(Negative)*
- **Steps:** Open a product page where the item is marked "Sold Out" → attempt to click "Add to Cart"
- **Expected Result:**
  - The "Add to Cart" button is disabled or replaced with a "Sold Out" label
  - Clicking produces no cart update
  - No item is added and no checkout redirect occurs

---

### TC-AC-03 | Add Product with Quantity Set to Maximum Boundary Value *(Edge Case)*
- **Steps:** On a product page, manually set the quantity input to an extremely high value (e.g., 9999) → click "Add to Cart"
- **Expected Result:**
  - System either caps the quantity at the allowed maximum and displays a warning
  - OR rejects the value with a validation message
  - Cart total reflects only the valid quantity; no broken state occurs
