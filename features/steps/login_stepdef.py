from behave import given, when, then
from helper import env_reader


@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.lp.login(username, password)


@given("the user is logged in")
def step_user_logged_in(context):
    context.lp.login(env_reader.get_env("USERNAME"), env_reader.get_env("PASSWORD"))
 