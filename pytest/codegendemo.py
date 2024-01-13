from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cakebitesbycarolyn.com/")
    page.get_by_role("link", name="Naughty Cakes").click()
    page.get_by_role("link", name="Naughty Cake", exact=True).first.click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="PLACE RESERVATION").click()
    page1 = page1_info.value
    page1.close()
    page.get_by_role("link", name="CAKEBITESbyCarolyn Logo").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
