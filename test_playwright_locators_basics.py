from typing import Any
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function")
def setup_browser_launch(playwright: Any):
    print("Setting up the browser for the test.")
    
def test_verify_user_name(page:Page, setup_browser_launch):
    print("Launching browser in fixture.")
    page.goto("https://github.com/himanshupathak1986")
    print("Page title:", page.title())
    assert "Himanshu Pathak" in page.locator(".vcard-names").inner_text()
    
    
def test_login_into_lpl_financials_page_with_dummy_values(playwright: Any):
    print("Testing login into LPL Financials page with dummy values.")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lpl.com/accounts/log-in.html")

    print("Page loaded successfully")
    page.get_by_text("Login to Resource Center ").click()
    print(f"New page title is: {page.title()}")
    expect(page).to_have_title("LPL Financial | Advisor & Investor Log In", timeout=10000) # You can specify a custom timeout if needed
    textbox_locators = page.locator('input[role="textbox"][type="text"]')  
    user_name_control = textbox_locators.filter(has=page.locator('[type="text"]'))
    user_name_control.fill("dummy_user")
    page.get_by_role("textbox", type="password").fill("dummy_password")
    page.click('button[type="submit"]')
    print("Login attempted with dummy credentials")
