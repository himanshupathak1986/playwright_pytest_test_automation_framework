from typing import Any
from playwright.sync_api import Page


def test_playwright_browser_launch(playwright: Any):
    print("Testing Playwright browser launch.")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/himanshupathak1986")
    print("Page title:", page.title());
    assert "Himanshu Pathak" in page.title()
    
    
#shortcut method to launch the browser in new headless mode
def test_playwright_browser_shortcut_launch(page: Page):
    print("Testing Playwright browser shortcut launch.")
    page.goto("https://github.com/himanshupathak1986")
    print("Page title:", page.title());
    assert "Himanshu Pathak" in page.title()
    
