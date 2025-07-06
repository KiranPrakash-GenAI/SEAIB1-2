from playwright.sync_api import sync_playwright, TimeoutError
import time

def count_emails():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="gmail_login_state.json")
        page = context.new_page()

        print("📬 Opening Gmail...")
        page.goto("https://mail.google.com", timeout=60000)

        try:
            print("⌛ Waiting for inbox to load...")
            page.wait_for_selector("table[role='grid']", timeout=20000)
            print("✅ Inbox loaded.")
        except TimeoutError:
            print("❌ Inbox didn't load.")
            browser.close()
            return

        # Count total emails on the current page
        email_rows = page.locator("css=table[role='grid'] tr.zA")
        total_emails = email_rows.count()

        # Count unread emails (have 'zE' class)
        unread_emails = page.locator("css=table[role='grid'] tr.zA.zE").count()

        print(f"📨 Total emails visible: {total_emails}")
        print(f"📬 Unread emails visible: {unread_emails}")

        time.sleep(3)
        browser.close()

if __name__ == "__main__":
    count_emails()
