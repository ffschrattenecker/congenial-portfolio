
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Load local index.html
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Take screenshot
        page.screenshot(path="verification/screenshot.png")
        print("Screenshot taken.")
        browser.close()

if __name__ == "__main__":
    run()
