from playwright.sync_api import sync_playwright
from helper import env_reader
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import os

## Dans ce fichier, on rajoute les fixtures, before and after
# before_scenario c'est reservé a behave pour s'executer avant chaque scenario
def before_scenario(context, scenario):
       # ici on lance le .start() - dans le after_scenario il faut le fermer (close)

    context.playwright = sync_playwright().start()

# si je choisi chrome, le playwright doit lancer le navigateur chromium, si je choisi firefox, il doit lancer firefox
# Il faut lier ce fichier avec la variable BROWSER dans le .env
# il faut donc charger le .env puis recuperer la valeur de la variable BROWSER a partir de .env


    BROWSER =env_reader.get_env("BROWSER")
    HEADLESS = env_reader.get_bool_env("HEADLESS")

    if BROWSER == "chrome":
      
       browser = context.playwright.chromium.launch(headless=HEADLESS)
       # ici on lance le chromium - dans le after_scenario il faut le fermer (stop)
    elif BROWSER == "firefox":
       
        browser =  context.playwright.firefox.launch(headless=HEADLESS)
    else:
       browser =   context.playwright.webkit.launch(headless=HEADLESS)
   

   # Instanciation des objets de types classes pages object models comme LoginPage etc pour pouvoir appeler et executer les methodes dans ces classes


    context.browser_context =browser.new_context()        # ici on ouvre un nouveau context - dans le after_scenario il faut le fermer (stop)

    # Il faut preparer un new contexte pour pouvoir appeler la methode new_page qui est l'instanciation de la varibale page 
    
    context.page = context.browser_context.new_page()
    
    context.lp = LoginPage(context.page)
    context.dp = DashboardPage(context.page)


def after_scenario(context, scenario):

# En cas de fail il faut prendre un screenshot et l'enregistrer dans un dossier qu'on crée

# ici il y a un objet reservé du behave (python) ou bien cucumber ( java ou js) = scenario pour pouvoir recuperer le status, le nom etc du scenario

    if scenario.status == "failed" and hasattr(context, "page"):
        os.makedirs("screenshots")
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")
        context.page.screenshot(path=f"screenshots/{safe_name}.png")

    if hasattr(context, "browser_context"):
        context.browser_context.close()   

    if hasattr(context, "browser"):
        context.browser.close()
    
    if hasattr(context, "playwright"):
        context.playwright.stop()
