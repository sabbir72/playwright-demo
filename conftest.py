import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # শুধুমাত্র failed test এর জন্য screenshot
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)  # Playwright page fixture
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            
            # Allure রিপোর্টে attach
            allure.attach.file(
                screenshot_path,
                name=f"{item.name} Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
