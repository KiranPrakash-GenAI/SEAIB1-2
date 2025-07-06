from playwright.sync_api import sync_playwright
def scrape_mymomscraft():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Change to False to see the browser
        context = browser.new_context()
        page = context.new_page()

        print("🌐 Visiting https://mymomscraft.com ...")
        page.goto("https://mymomscraft.com", timeout=60000)

        # Wait until page loads completely
        page.wait_for_load_state("networkidle")

        print("📝 Extracting text from the page...")
        content = page.locator("body").inner_text()

        with open("momscraft.txt", "w", encoding="utf-8") as file:
            file.write(content)

        print("✅ Text successfully saved to momscraft.txt")

        browser.close()

if __name__ == "__main__":
    scrape_mymomscraft()
