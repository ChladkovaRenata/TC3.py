Nainstaluj závislosti:
pip install pytest playwright

Nainstaluj prohlížeče pro Playwright:
playwright install

Pro spuštění všech testů použij:
pytest

Pokud chceš spustit testy pouze v Chromium (nejběžnější):
pytest --headed --browser chromium

Pokud máš jiné prohlížeče tak:
pytest --headed --browser firefox
pytest --headed --browser webkit

Struktura testů 
test_homepage_title — ověřuje, že titulní stránka obsahuje text "ENGETO"
test_kurzy_page_contains_text — kontroluje, zda stránka přehledu kurzů obsahuje slovo "Kurzy"
test_otevreni_stranky_pro_firmy — otevírá stránku pro firmy a kontroluje URL - obsahuje stránku pro firmy


Task Manager Projekt 3
├── __pycache__
├── .pytest_cache
    └── v
├── test_python.py
└── README.md
