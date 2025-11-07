import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://stagev15.inctl.net/#login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("Administrator")

    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin")

    page.get_by_role("button", name="Login").click()


#----------------- Finishing Target Creation -----------------#
    page.get_by_role("combobox", name="Search or type a command (").click()
    page.get_by_role("combobox", name="Search or type a command (").fill("finishing Target")
    page.get_by_role("link", name="Finishing Target List").click()

    # Create Finishing Target
    page.get_by_role("button", name="Add Finishing Target").click()

    page.locator("form").filter(has_text="Operation Type Begin typing").get_by_role("combobox").click()
    page.get_by_title("Finishing", exact=True).click()
    page.locator("form").filter(has_text="Sewing Target Begin typing").get_by_role("combobox").first.click()
    page.locator("form").filter(has_text="Sewing Target Begin typing").get_by_role("combobox").first.fill("MFG-PP-2025-00025-1")

    page.get_by_title("MFG-PP-2025-00025-").click()
    page.locator("form").filter(has_text="Operation Bulletin Begin").get_by_role("combobox").click()
    page.get_by_title("OB-FIN-NTG").click()

    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(1).click()
    page.get_by_title("IRON(OP)").click()

  
    page.locator("form").filter(has_text="Product Begin typing for").get_by_role("textbox").fill("4")
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(2).click()
    page.get_by_title("Line 1", exact=True).click()
    # page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    # page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    page.locator("div:nth-child(4) > .section-body > div:nth-child(2)").click()

    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").fill("2")

    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("60")

    page.get_by_role("button", name="Insert").click()

    # Create Sewing Target
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").first.click()
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").first.fill("MFG-PP-2025-00025-1")
    page.get_by_title("MFG-PP-2025-00025-").click()

    page.locator("form").filter(has_text="Operation Bulletin OB-FIN-").get_by_role("combobox").click()
    page.get_by_role("strong").click()
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(1).click()
    page.get_by_text("Poly Pack & close", exact=True).click()

    page.locator("form").filter(has_text="Product Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Product Begin typing for").get_by_role("textbox").fill("4")

    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(2).click()
    page.get_by_title("Line 2").click()

    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").fill("3")
    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("65")
    page.get_by_role("button", name="Insert").click()
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").first.click()
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").first.fill("MFG-PP-2025-00025-1")
    page.get_by_title("MFG-PP-2025-00025-").click()
    page.locator("form").filter(has_text="Operation Bulletin OB-FIN-").get_by_role("combobox").click()
    page.get_by_role("option", name="OB-FIN-NTG").click()
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(1).click()
    page.get_by_role("option", name="Packing").get_by_role("paragraph").click()
    page.locator("form").filter(has_text="Product Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Product Begin typing for").get_by_role("textbox").fill("4")
    page.locator("form").filter(has_text="Sewing Target MFG-PP-2025-").get_by_role("combobox").nth(2).click()
    page.get_by_text("Line 3").click()
    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Style Begin typing for").get_by_role("textbox").fill("3")
    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("65")
    page.get_by_role("button", name="Insert").click()

    # Adding BOM in Finishing Target
    page.locator(".rows > div > .data-row > .row-index").first.click()
    page.locator("div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.locator("div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").fill("BOM-RMG-0029-028")
    # page.wait_for_selector("text=BOM-RMG-0029-028", timeout=5000)
    # page.get_by_text("BOM-RMG-0029-028").click()
    # page.locator("#freeze div").first.click()
    page.locator(".btn.btn-secondary.btn-sm.pull-right").first.click()

    page.get_by_text("2", exact=True).nth(1).click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > .row > .section-body > div:nth-child(2) > form > div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > .row > .section-body > div:nth-child(2) > form > div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").fill("BOM-RMG-0029-028")
    # page.wait_for_selector("text=BOM-RMG-0029-028 RMG-0029, T", timeout=5000)
    # page.get_by_text("BOM-RMG-0029-028 RMG-0029, T").click()
    # page.locator("#freeze div").first.click()
    # page.locator(".btn.btn-secondary.btn-sm.pull-right").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-heading > .toolbar > .row-actions > .btn.btn-secondary.btn-sm.pull-right.grid-collapse-row").click()

    page.get_by_text("3", exact=True).nth(1).click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > .row > .section-body > div:nth-child(2) > form > div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-body > .form-area > .form-layout > .form-page > .row > .section-body > div:nth-child(2) > form > div:nth-child(6) > .form-group > .control-input-wrapper > .control-input > .link-field > .awesomplete > .input-with-feedback").fill("BOM-RMG-0029-028")
    # page.wait_for_selector("text=BOM-RMG-0029-028 RMG-0029, T", timeout=5000)
    # page.get_by_text("BOM-RMG-0029-028 RMG-0029, T").click()
    # page.locator("#freeze div").first.click()
    page.locator(".grid-row.grid-row-open > .form-in-grid > .grid-form-heading > .toolbar > .row-actions > .btn.btn-secondary.btn-sm.pull-right.grid-collapse-row").click()
    page.get_by_role("button", name="Save").click()
    page.screenshot(path="finishing_target.png")
    # page.get_by_role("button", name="Submit").click()
    # page.get_by_role("button", name="Yes").click()
