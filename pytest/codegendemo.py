from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://cakebitesbycarolyn.com/")
    page.locator("#menu-item-1523").get_by_role("link", name="Cupcakes").click()
    page.get_by_role("link", name="Student").click()
    page.get_by_role("link", name="Crypto Cupcake").first.click()
    page.get_by_role("link", name="CAKEBITESbyCarolyn Logo").click()
