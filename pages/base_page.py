from playwright.sync_api import Page, expect

class BasePage:

    def __init__(self, page: Page):
        
        # Ici pas d'instanciation de Page juste on a declaré une variable page de type la classe Page 
        self.page = page

# NAVIGATION

    def go_to_url(self, url: str, charging_time: float = 10000):
       
       self.page.goto(url, timeout=charging_time, wait_until="networkidle")
    
    def go_back(self):

        self.page.go_back()

    def go_forward(self):

        self.page.go_forward()
    
    def refresh_page(self):

        self.page.reload()



# ASSERTIONS AND WAITS

    def wait_for_url_contains(self, expected_txt: str, charging_time: float = 10000):
        """
        networkidle c'est attendre qu'il y a plus de requete reseau en cours
        """
        self.page.wait_for_url(f"**{expected_txt}**", wait_until="networkidle" , timeout=charging_time)

    def assert_title_contains(self, expected_title: str):

        actual_title = self.page.title()
        assert expected_title in actual_title, (f"Expeted Title to contain '{expected_title}', and the actual title is '{actual_title}'")

    def assert_title_is(self, expected_title: str):

        actual_title = self.page.title()
        assert expected_title == actual_title,  (f"Expeted Title to contain '{expected_title}', and the actual title is '{actual_title}'")


    def assert_element_contains_text(self, locator: str, text: str):

        expect (self.page.locator(locator)).to_contain_text(text)
        
    def _wait_for_element_to_be_visible(self, element):
        """
        Methode locale qui commence par _ et qui pourrait etre appelée seulement dans toutes les methodes de cette classe BasePage avec le slef
        """
        element.wait_for(state="visible")


# BASIC ACTIONS
    def click_to_element(self, locator: str):

        element = self.page.locator(locator)
        self._wait_for_element_to_be_visible(element)
        element.click()

    def fill(self, locator: str, text_tobe_filled: str):

       element = self.page.locator(locator)
       self._wait_for_element_to_be_visible(element)
       element.fill(text_tobe_filled)

    def fill_and_enter(self, locator: str, text_tobe_filled: str):

       element = self.page.locator(locator)
       self._wait_for_element_to_be_visible(element)
       element.fill(text_tobe_filled)
       self.page.keyboard.press("ENTER")
    
    def get_text(self, loctor: str) -> str:
       
       element = self.page.locator(loctor)
       self._wait_for_element_to_be_visible(element)
       return element.inner_text()

# ALERTS
    
    def handle_alert(self, action: str = "ok"):
        """
        Gere une alerte javascript, accepet : cliquer sur ok
                                    dismiss : cliquer sur cancel
        
        ici c est avec la methode on que vous aller switcher, ici pas de switch to alert

        dialog == alert                            
                                    
        if condition1 true:
            action   
        elif condition2 true:
            action
        else:                         
                                    
        """
        def dialog_handle(dialog): 
          if action == "ok":
              dialog.accept()
          elif action == "cancel":  
              dialog.dismiss()
          else:
              raise RuntimeError("Action is Invalid")
          
        self.page.on("dialog", dialog_handle )


            
# DROPDOWN

    def select_option_by_visible_text(self, select_locator: str, visible_text: str):
       
       select_element =self.page.locator(select_locator)
       self._wait_for_element_to_be_visible(select_element)
       select_element.select_option(label=visible_text)

    def click_on_option_by_visible_text(self, select_locator: str, option_locator: str):

        self.click_to_element(select_locator)
        self.click_to_element(option_locator)


# HOVER

    def hover_to_element(self, locator: str):
        """
        Une methode pour placer la souris sur un element bien determiné sans pour autant cliquer dessus
        """
        element =self.page.locator(locator)
        self._wait_for_element_to_be_visible(element)
        element.hover()
