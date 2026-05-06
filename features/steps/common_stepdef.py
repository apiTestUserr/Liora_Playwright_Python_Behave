from behave import given, when, then
from helper import env_reader

@given("the user opens OrangeHRM demo Login page")
def step_open_orangehrm_page(context):

     context.lp.go_to_url(env_reader.get_env("BASE_URL"))
     context.lp.assert_login_page_is_displayed()


@then('the page "{}" is displayed')
def step_verify_dashboard_displayed(context, page_name):

    context.dp.verify_dashboard_page_is_displayed(page_name)


@when('the user opens the page "{}" menu')
def step_open_menu(context, menu_name):
     context.dp.click_to_menu_by_name(menu_name)