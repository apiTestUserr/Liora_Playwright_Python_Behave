from behave import given, when, then
from helper import env_reader

@given("the user opens OrangeHRM demo Login page")
def step_open_orangehrm_page(context):

     context.lp.go_to_url(env_reader.get_env("BASE_URL"))
     context.lp.assert_login_page_is_displayed()
