from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    btn_alle_akzeptieren = page.get_by_role("button", name="Alle akzeptieren")
    btn_verbindung_suchen =  page.get_by_role("button", name="Verbindung suchen")
    txbox_von = page.get_by_text("Von", exact=True)
    txbox_nach = page.get_by_text("Nach", exact=True)

    page.goto("https://www.bls.ch/de")

    btn_alle_akzeptieren.click()
    txbox_von.click()

    page.get_by_label("Von").fill("Bern")

    txbox_nach.click()

    page.get_by_label("Nach").fill("Köniz")

    btn_verbindung_suchen.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)