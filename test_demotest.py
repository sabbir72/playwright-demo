# # test_google.py
# from playwright.sync_api import sync_playwright

# def run(playwright):
#     # 1️⃣ Chromium browser খুলবে
#     browser = playwright.chromium.launch(headless=False)  # headless=False মানে browser দেখা যাবে
#     page = browser.new_page()

#     # 2️⃣ Google এ যাবে
#     page.goto("https://www.google.com")

#     # 3️⃣ Search box এ কিছু লিখবে
#     page.fill("textarea[name='q']", "Playwright Python tutorial")

#     # 4️⃣ Enter চাপবে
#     page.keyboard.press("Enter")

#     # 5️⃣ কিছুক্ষণ অপেক্ষা করবে
#     page.wait_for_timeout(3000)

#     # 6️⃣ Screenshot নেবে
#     page.screenshot(path="google_search.png")

#     # 7️⃣ Browser বন্ধ করবে
#     # browser.close()

# with sync_playwright() as playwright:
#     run(playwright)

import pytest
import allure

@allure.title("Google Homepage Test")
def test_google_title(page):
    page.goto("https://google.com")
    with allure.step("Check incorrect page title to fail test"):
        # Intentionally wrong title to fail
        assert "Googl" in page.title()  # Fail hobe
