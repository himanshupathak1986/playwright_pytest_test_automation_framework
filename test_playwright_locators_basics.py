from typing import Any
from playwright.sync_api import Page
import pytest

@pytest.fixture(scope="function")
def setup_browser_launch(playwright: Any):
    print("Setting up the browser for the test.")

    
    
def test_verify_user_name(page:Page, setup_browser_launch):
    print("Launching browser in fixture.")
    page.goto("https://github.com/himanshupathak1986")
    print("Page title:", page.title())
    assert "Himanshu Pathak" in page.locator(".vcard-names").inner_text()