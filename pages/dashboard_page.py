from base_page import BasePage

class DashboardPage(BasePage):

    MENU_ITEM = "//span[normalize-space()='{}']"


    def click_to_menu_by_name(self, menu_name):

        self.click_to_element(self.MENU_ITEM.format(menu_name))

