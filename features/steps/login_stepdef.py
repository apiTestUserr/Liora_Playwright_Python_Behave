from behave import given, when, then
from helper import env_reader


@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.lp.login(username, password)


@then("the Dashboard page is displayed")
def step_verify_dashboard_displayed(context):

    pass