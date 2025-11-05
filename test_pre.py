import re
from playwright.sync_api import Page, expect

def test_pre_costing_creation(page: Page):
    page.goto("https://stagev15.inctl.net/#login")

    # Login
    page.get_by_role("textbox", name="Email").fill("Administrator")
    page.get_by_role("textbox", name="Password").fill("admin")
    page.get_by_role("button", name="Login").click()

    # Verify login success
    expect(page).to_have_url(re.compile(".*home"))

    # Navigate to Pre Costing
    page.get_by_role("combobox", name=re.compile("Search")).click()
    page.get_by_role("link", name="Pre Costing List").click()
    page.get_by_role("button", name="Add Pre Costing").click()

    # Select buyer and style
    page.get_by_role("combobox").nth(1).click()
    page.get_by_title("RMG", exact=True).click()
    page.get_by_role("combobox").nth(2).click()
    page.get_by_title("HUPM0060").click()

    # Add fabric item
    # page.get_by_text("% BCI Cotton S/J").click()
    # page.get_by_role("option", name="Local").click()
    # page.get_by_role("option", name="Black", exact=True).click()
    # page.get_by_text("GSM-161-0474160.0").click()
    # page.get_by_text("DIA-00001").click()
    # page.get_by_text("Back", exact=True).click()
    # page.get_by_text("Front", exact=True).click()
    # page.fill("input", "0.25")
    # page.fill("input", "5")

    # Add accessories (example)
    # page.get_by_role("button", name="Insert Below").click()
    # page.fill("input", "Sewing Thread 50/2 Accessories-0018")
    # page.get_by_role("option", name="Local").click()
    # page.fill("input", "0.21")
    # page.get_by_role("option", name="Cone").click()
    # page.fill("input", "0.2")

    # # Fill costing data
    # page.get_by_role("tab", name="Operations").click()
    # page.get_by_title("KOHLS-OPB", exact=True).click()
    # page.get_by_role("tab", name="Pre Costing Data").click()
    # page.fill("input", "600")
    # page.get_by_title("120 Days").click()
    # page.get_by_title("Sea", exact=True).click()
    # page.get_by_title("FOB").click()

    # # Save and submit
    # page.get_by_role("button", name="Save").click()
    # page.get_by_role("button", name="Submit").click()
    # page.get_by_role("button", name="Yes").click()

    # Final assertion
    expect(page).to_have_url(re.compile(".*Pre Costing List"))
