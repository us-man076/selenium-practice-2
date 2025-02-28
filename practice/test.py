from playwright.sync_api import sync_playwright

def search_and_open_daraz():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for background execution
        page = browser.new_page()
        
        # Open Google
        page.goto("https://www.google.com")
        
        # Accept cookies (if any, Google sometimes shows a consent popup)
        if page.locator('text=Accept all').count() > 0:
            page.locator('text=Accept all').click()
        
        # Search for "daraz . pk"
        page.fill("textarea[name='q']", "daraz . pk")
        page.press("textarea[name='q']", "Enter")
        
        # Wait for search results to load
        page.wait_for_selector("h3")
        
        # Click the first search result
        page.locator("h3").first.click()
        
        # Keep the browser open for review
        page.wait_for_timeout(1500)  # Wait for 5 seconds
        browser.close()

# Run the function
search_and_open_daraz()
