from playwright.sync_api import sync_playwright
from helper import env_reader
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

## Dans ce fichier, on rajoute les fixtures, before and after

def before_each_scenario():

    playwright = sync_playwright().start()

# si je choisi chrome, le playwright doit lancer le navigateur chromium, si je choisi firefox, il doit lancer firefox
# Il faut lier ce fichier avec la variable BROWSER dans le .env
# il faut donc charger le .env puis recuperer la valeur de la variable BROWSER a partir de .env


    BROWSER =env_reader.get_env("BROSWER")
    HEADLESS = env_reader.get_bool_env("HEADLESS")

    if BROWSER == "chrome":
      
        playwright.chromium.launch(headless=HEADLESS)
    elif BROWSER == "firefox":
       
        playwright.firefox.launch(headless=HEADLESS)
    else:
        playwright.webkit.launch(headless=HEADLESS)
   


