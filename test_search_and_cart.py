# test_search_and_cart.py
# Task 2 – Automated Scenario: Search for a product and add it to the cart.
#
# Run:
#   pytest test_search_and_cart.py -v --html=report.html --self-contained-html

from selenium.webdriver.by import By
from config import STORE_URL, STORE_PASSWORD, SEARCH_TERM
from pages import PasswordPage, HomePage, SearchResultsPage, ProductPage


# ──────────────────────────────────────────────
# Helper
# ──────────────────────────────────────────────

def _unlock_store_if_needed(driver, password: str):
    """
    Shopify password-protected stores redirect to /password.
    This helper detects that page and enters the store password.
    """
    if (
        "/password" in driver.current_url
        or driver.find_elements(By.ID, "password")
    ):
        PasswordPage(driver).enter_password(password)


# ──────────────────────────────────────────────
# Test
# ──────────────────────────────────────────────

class TestSearchAndAddToCart:
    """
    End-to-end scenario:
      1. Open AdNabuTestStore and unlock the password gate.
      2. Search for a product using the search bar.
      3. Click the first result from the search results page.
      4. Add the product to the cart on the product detail page.
      5. Assert that the cart confirmation is visible.
    """

    def test_search_product_and_add_to_cart(self, driver):
        # ── Step 1: Open the store ────────────────────────────────────────
        driver.get(STORE_URL)
        _unlock_store_if_needed(driver, STORE_PASSWORD)

        # ── Step 2: Search for a product ─────────────────────────────────
        home = HomePage(driver)
        home.search(SEARCH_TERM)

        # ── Step 3: Click the first search result ─────────────────────────
        results = SearchResultsPage(driver)
        results.click_first_product()

        # ── Step 4: Add to cart ───────────────────────────────────────────
        product = ProductPage(driver)
        assert product.is_add_to_cart_enabled(), (
            "Add to Cart button is disabled — product may be out of stock."
        )
        product.add_to_cart()

        # ── Step 5: Verify cart confirmation appeared ─────────────────────
        page_text = driver.page_source.lower()
        confirmation_keywords = ["added", "cart", "item", "bag", "basket"]
        assert any(kw in page_text for kw in confirmation_keywords), (
            "No cart confirmation signal found on the page after clicking Add to Cart."
        )
