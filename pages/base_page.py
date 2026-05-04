from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        
        self.page = page

    def go_to_url(self, url: str, page: Page):

       self.page.goto(url, wait_until="networkidle")

    def assert_title_contains(self, expected_title: str):

        actual_title = self.page.title()
        assert expected_title in actual_title, (f"Expeted Title to contain '{expected_title}', and the actual title is '{actual_title}'")

    def assert_title_is(self, expected_title: str):

        actual_title = self.page.title()
        assert expected_title == actual_title,  (f"Expeted Title to contain '{expected_title}', and the actual title is '{actual_title}'")

    def click_to_element(self, locator: str):

        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    def fill(self, locator: str, text_tobe_filled: str):

       element = self.page.locator(locator)
       element.wait_for(state="visible")
       element.fill(text_tobe_filled)

    def fill_and_enter(self, locator: str, text_tobe_filled: str):

       element = self.page.locator(locator)
       element.wait_for(state="visible")
       element.fill(text_tobe_filled)
       self.page.keyboard.press("ENTER")
    
    def get_text(self, loctor: str) -> str:
       
       element = self.page.locator(loctor)
       element.wait_for(state="visible")
       return element.inner_text()


