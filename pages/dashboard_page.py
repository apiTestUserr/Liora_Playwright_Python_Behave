from pages.base_page import BasePage

class DashboardPage(BasePage):

    MENU_ITEM = "//span[normalize-space()='{}']"


    def click_to_menu_by_name(self, menu_name):

        self.click_to_element(self.MENU_ITEM.format(menu_name))

    def verify_dashboard_page_is_displayed(self, page_name):
        self.assert_page_is_displayed(page_name)

