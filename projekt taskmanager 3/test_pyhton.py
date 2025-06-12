import pytest
from playwright.sync_api import Page, expect, sync_playwright

def test_homepage_title(page: Page):
    page.set_default_navigation_timeout(10000)
    page.goto("https://engeto.cz/")
    assert "ENGETO" in page.title().upper()

def test_kurzy_page_contains_text(page: Page):
    page.goto("https://engeto.cz/prehled-kurzu/", timeout=10000)
    assert "Kurzy" in page.content()

def test_otevreni_stranky_pro_firmy(page: Page):
    page.goto("https://engeto.cz/pro-firmy/", timeout=15000)
    assert page.url == "https://engeto.cz/pro-firmy/"

