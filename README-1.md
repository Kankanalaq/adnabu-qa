# AdNabuTestStore – QA Engineer Assignment

Submission for the **AdNabu QA Engineer** assignment.

---

## Repository Structure

```
adnabu-qa/
├── conftest.py               # Pytest browser fixture (setup & teardown)
├── config.py                 # Central config: URL, password, search term, timeouts
├── pages.py                  # Page Object Model (Password / Home / Results / Product pages)
├── test_search_and_cart.py   # Task 2 – Automated test scenario
├── test_cases.md             # Task 1 – 6 manual test cases
├── requirements.txt          # Python dependencies
├── report.html               # Sample test report
└── README.md
```

---

## Task 1 – Test Cases

See [`test_cases.md`](test_cases.md).

Covers **Product Search** and **Add to Cart** with positive, negative, and edge cases.

---

## Task 2 – Automated Test

**Scenario automated:** Search for a product → click the first result → add it to the cart → assert confirmation.

**Tech stack:** Python 3.9+ · Selenium 4 · pytest · webdriver-manager

**Design choices:**
- No `time.sleep()` — every wait uses `WebDriverWait` + `expected_conditions`
- Page Object Model keeps locators separate from test logic (readable + modular)
- `conftest.py` handles browser setup/teardown cleanly
- `webdriver-manager` auto-installs the correct ChromeDriver

---

## Setup

### 1 – Prerequisites

| Tool | Version |
|---|---|
| Python | 3.9+ |
| Google Chrome | Latest stable |

### 2 – Clone the repo

```bash
git clone https://github.com/<your-username>/adnabu-qa.git
cd adnabu-qa
```

### 3 – Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 4 – Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Tests

### Run with verbose output + HTML report

```bash
pytest test_search_and_cart.py -v --html=report.html --self-contained-html
```

### Run in a visible browser (for debugging)

Comment out the headless line in `conftest.py`:

```python
# options.add_argument("--headless=new")
```

Then run:

```bash
pytest test_search_and_cart.py -v
```

---

## Viewing the Report

After the run, open `report.html` in your browser:

```bash
open report.html          # macOS
start report.html         # Windows
xdg-open report.html      # Linux
```

A pre-generated sample report is already included in the repository.

---

## Configuration

All settings are in `config.py`:

```python
STORE_URL      = "https://adnabu-store-assignment1.myshopify.com"
STORE_PASSWORD = "AdNabuQA"
SEARCH_TERM    = "wax"     # Change to any product keyword
WAIT_TIMEOUT   = 15        # Seconds before WebDriverWait times out
```
