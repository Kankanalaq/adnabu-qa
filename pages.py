# pages.py
# Page Object Model for AdNabuTestStore
# Each class represents one page and owns its locators + actions.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import WAIT_TIMEOUT


# ──────────────────────────────────────────────
# Base Page
# ──────────────────────────────────────────────

class BasePage:
    """Common wait helpers shared across all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def _wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))


# ──────────────────────────────────────────────
# Password Page  (Shopify storefront password gate)
# ──────────────────────────────────────────────

class PasswordPage(BasePage):

    _INPUT  = (By.ID, "password")
    _SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_password(self, password: str):
        """Type the store password and submit the form."""
        field = self._wait_visible(self._INPUT)
        field.clear()
        field.send_keys(password)
        self._wait_clickable(self._SUBMIT).click()


# ──────────────────────────────────────────────
# Home Page  (search bar interaction)
# ──────────────────────────────────────────────

class HomePage(BasePage):

    # Shopify themes differ; these selectors cover the most common patterns
    _SEARCH_TOGGLE = (By.CSS_SELECTOR,
        "button[aria-label*='Search'], "
        "a[href='/search'], "
        ".header__icon--search, "
        "[data-action='toggle-search']"
    )
    _SEARCH_INPUT = (By.CSS_SELECTOR,
        "input[type='search'], "
        "input[name='q']"
    )

    def search(self, term: str):
        """Open the search field (if needed) and submit the query."""
        # Try clicking a search toggle icon first; some themes need it
        try:
            self._wait_clickable(self._SEARCH_TOGGLE).click()
        except Exception:
            pass  # Input may already be in the DOM

        box = self._wait_visible(self._SEARCH_INPUT)
        box.clear()
        box.send_keys(term)
        box.send_keys(Keys.RETURN)


# ──────────────────────────────────────────────
# Search Results Page
# ──────────────────────────────────────────────

class SearchResultsPage(BasePage):

    _FIRST_PRODUCT = (By.CSS_SELECTOR,
        ".product-item a, "
        ".grid-product__link, "
        ".card__heading a, "
        "h3.h4 a, "
        ".product-card a"
    )

    def click_first_product(self):
        """Click the first product link in the search results."""
        self._wait_clickable(self._FIRST_PRODUCT).click()


# ──────────────────────────────────────────────
# Product Detail Page
# ──────────────────────────────────────────────

class ProductPage(BasePage):

    _ADD_TO_CART = (By.CSS_SELECTOR,
        "button[name='add'], "
        "button[type='submit'].product-form__submit, "
        "button.btn--add-to-cart, "
        "#AddToCart"
    )
    _CART_CONFIRMATION = (By.CSS_SELECTOR,
        ".cart-notification, "
        ".cart-drawer, "
        "[id*='cart-notification'], "
        ".cart-popup, "
        "[aria-label*='cart' i]"
    )

    def add_to_cart(self):
        """Click 'Add to Cart' and wait for the confirmation element."""
        btn = self._wait_clickable(self._ADD_TO_CART)
        btn.click()
        self._wait_visible(self._CART_CONFIRMATION)

    def is_add_to_cart_enabled(self) -> bool:
        """Return True when the Add to Cart button is active (not sold out)."""
        btn = self._wait_present(self._ADD_TO_CART)
        return btn.is_enabled() and btn.get_attribute("disabled") is None
