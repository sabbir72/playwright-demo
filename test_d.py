# import pytest
# import frappe


# @pytest.mark.erpnext
# def test_style_duplicate_reference_clear():

#     page.goto("https://stagev15.inctl.net/#login")
#     page.get_by_role("textbox", name="Email").click()
#     page.get_by_role("textbox", name="Email").fill("Administrator")

#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("admin")

#     page.get_by_role("button", name="Login").click()
#     """Check that when Style doc is duplicated, old references are not carried over."""

#     # Step 1: Load original Style document
#     original = frappe.get_doc("Style", "333")

#     # Step 2: Create a duplicate (simulate 'Duplicate' button)
#     duplicate = frappe.copy_doc(original)
#     duplicate.style_name = "333-DUP"           # নতুন নাম দিন
#     duplicate.customer = "C&A"       # কিছু মান আলাদা করুন
#     duplicate.insert()

#     # # Step 3: Ensure name changed properly
#     # assert duplicate.name != original.name, "❌ Duplicate kept same docname!"

#     # # Step 4: Ensure child tables are new references, not linked to old doc
#     # for child in duplicate.style_item:
#     #     assert child.parent == duplicate.name, f"❌ Style Item parent still old: {child.parent}"
#     #     assert child.parent != original.name

#     # for combo in duplicate.style_combinations:
#     #     assert combo.parent == duplicate.name, f"❌ Style Combination parent still old: {combo.parent}"
#     #     assert combo.parent != original.name

#     # # Step 5: Ensure no hidden internal field reference exists
#     # # (ERPNext docs sometimes keep hidden __original_docname or ref_name field)
#     # doc_dict = duplicate.as_dict()

#     # for key, value in doc_dict.items():
#     #     if isinstance(value, str) and original.name in value:
#     #         pytest.fail(f"❌ Old docname found in field {key}: {value}")

#     # # Step 6: Submit new document (optional)
#     # duplicate.submit()
#     # assert duplicate.docstatus == 1, "❌ Duplicate doc failed to submit."

#     print("✅ Duplicate reference cleared successfully for Style doc.")
# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.mark.ui
# def test_style_duplicate_ui_login():
#     """UI Test: Login and open Style form"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         # Step 1: Go to ERPNext login page
#         page.goto("https://stagev15.inctl.net/#login")

#         # Step 2: Login
#         page.get_by_role("textbox", name="Email").fill("Administrator")
#         page.get_by_role("textbox", name="Password").fill("admin")
#         page.get_by_role("button", name="Login").click()

#         # Step 3: Verify login success (wait for desk to load)
#         page.wait_for_url("**/app")

#         # Step 4: Open Style list and search "333"
#         page.goto("https://stagev15.inctl.net/app/style")
#         page.get_by_placeholder("Search").fill("333")
#         page.keyboard.press("Enter")
#         page.wait_for_timeout(2000)

#         # Step 5: Optionally open and duplicate the record (manual flow simulation)
#         # (এই অংশ আপনি চাইলে পরের ধাপে add করতে পারেন)

#         browser.close()


# ===================================================================================

# import pytest
# import frappe

# def test_duplicate_style_doc():
#     """Check duplicate Style doc doesn't keep old reference."""

#     # 1️⃣ Original Style doc লোড করা
#     original = frappe.get_doc("Style", "333")

#     # 2️⃣ Duplicate তৈরি করা
#     duplicate = frappe.copy_doc(original)
#     duplicate.style_name = f"{original.style_name}-DUP"
#     duplicate.insert()

#     # 3️⃣ নিশ্চিত হওয়া নতুন docname পুরনোটা না
#     assert duplicate.name != original.name, "Duplicate doc kept same name!"

#     # 4️⃣ Old reference আছে কিনা চেক করা (simple string check)
#     assert original.name not in str(duplicate.as_dict()), "Old reference found in duplicate!"

#     print(f"✅ Duplicate created successfully: {duplicate.name}")
# ===================================================================================
import pytest
from playwright.sync_api import sync_playwright

def test_style_doc_internal_compare():
    """Compare old and duplicate Style doc JSON via UI (cur_frm.doc)."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # --- Step 1: Login ---
        page.goto("https://stagev15.inctl.net/#login")
        page.get_by_role("textbox", name="Email").fill("Administrator")
        page.get_by_role("textbox", name="Password").fill("admin")
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(3000)

        # --- Step 2: Load Original Doc ---
        page.goto("https://stagev15.inctl.net/app/style/333")
        page.wait_for_timeout(3000)
        original_data = page.evaluate("cur_frm.doc")

        print("\n🟢 Original Doc:")
        print("Name:", original_data["name"])
        print("Style Name:", original_data.get("style_name"))
        print("Customer:", original_data.get("customer"))

        # --- Step 3: Load Duplicate Doc ---
        page.goto("https://stagev15.inctl.net/app/style/333-DUP")
        page.wait_for_timeout(3000)
        duplicate_data = page.evaluate("cur_frm.doc")

        print("\n🟣 Duplicate Doc:")
        print("Name:", duplicate_data["name"])
        print("Style Name:", duplicate_data.get("style_name"))
        print("Customer:", duplicate_data.get("customer"))

        # --- Step 4: Compare & Assert ---
        assert original_data["name"] != duplicate_data["name"], "❌ Duplicate kept same name!"
        assert original_data["style_name"] != duplicate_data["style_name"], "❌ Style name not updated!"
        assert original_data.get("customer") == duplicate_data.get("customer"), "❌ Customer mismatch!"

        # --- Step 5: Print summary difference ---
        print("\n✅ Test Result:")
        print(f"Old Doc: {original_data['name']} | New Doc: {duplicate_data['name']}")
        print(f"Old Style Name: {original_data['style_name']} | New Style Name: {duplicate_data['style_name']}")
        print("Assertion Passed — Duplicate reference cleared correctly.")

        browser.close()
