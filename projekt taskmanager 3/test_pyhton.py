import pytest
import re
from playwright.sync_api import Page, expect

# Test: homepage title
def test_homepage_title(page: Page):
    page.set_default_navigation_timeout(10000)
    page.goto("https://engeto.cz/")
 
 # Ověření, že titulek stránky obsahuje "ENGETO" bez ohledu na velikost písmen
    expect(page).to_have_title(re.compile(r"ENGETO", re.IGNORECASE))


# Test: přehledu kurzů
def test_kurzy_page_contains_heading(page: Page):
    page.goto("https://engeto.cz/prehled-kurzu/", timeout=10000)
    
    # Naleznout nadpis h1 obsahující slovo "Kurzy"
    heading = page.locator("h1").filter(has_text="Kurzy")
    expect(heading).to_be_visible()


# Test: stránky pro firmy
def test_pro_firmy_page_opens_correctly(page: Page):
    page.goto("https://engeto.cz/pro-firmy/", timeout=15000)
    
    # Ověření, že to pošle skutečně na požadované stránce
    expect(page).to_have_url("https://engeto.cz/pro-firmy/")

    # Ověření, že stránka obsahuje sekci pro firmy
    expect(page.locator("h1")).to_contain_text("Firmy")
