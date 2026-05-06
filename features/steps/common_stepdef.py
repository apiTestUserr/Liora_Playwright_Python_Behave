from behave import given, when, then
from helper import env_reader

# pour chaque etape dans les fichiers .feature, il faut les definir ici dans les steps, a l'aide de Behave
# Chaque etape gherkin equivalente a @given, @when, @then qui se mettent au dessus des methodes

@given("the user opens OrangeHRM demo Login page")
def step_open_orangehrm_page(context):


# ici on a besoin d'appeler toutes les methodes qu'on avait preparer dans les pages, pour ce faire, on a instancier des objets lp de la classe LoginpAGE, DP DE LA CLASSE Dashboeard page
# on les a crées dans le environment.py et on les a partagé a l'aide de context, on a donc pu les utiliser ici facillement avec context.lp , context.dp etc

     context.lp.go_to_url(env_reader.get_env("BASE_URL"))
     context.lp.assert_login_page_is_displayed()


@then('the page "{}" is displayed')
def step_verify_dashboard_displayed(context, page_name):

    context.dp.verify_dashboard_page_is_displayed(page_name)


@when('the user opens the page "{}" menu')
def step_open_menu(context, menu_name):
     context.dp.click_to_menu_by_name(menu_name)