from pages.base_page import BasePage

class LoginPage(BasePage):

    # Cette classe fille herite automatiquement le constructeur de la classe mere BasePage avec ses parametres

# ie la classe LoginPage herite de la classe Base Page
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    LOGIN_FORM = "//div[contains(@class,'orangehrm-login-form')]"
    ERROR_MESSAGE = "//p[contains(@class,'oxd-alert-content-text')]"

    def assert_login_page_is_displayed(self):
        self.assert_element_visible(self.LOGIN_FORM)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click_to_element(self.LOGIN_BUTTON)

    def assert_error_message_is_displayed(self, expected_message: str):
        self.assert_element_contains_text(self.ERROR_MESSAGE, expected_message)
