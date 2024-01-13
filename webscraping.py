try:
    from playwright.sync_api import sync_playwright
    
    # If the import succeeds, Playwright is installed
    print("Playwright is installed.")
except ImportError:
    # If there's an ImportError, Playwright is not installed
    print("Playwright is not installed.")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://whatsmyuseragent.org/")
    page.screenshot(path="demo.png")
    browser.close
