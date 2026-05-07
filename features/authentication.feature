Feature:   Authentication Test Suite

	As a user, a want to authenticate wth admin, user, super user

    Background: shared preconditions
		Given the user opens OrangeHRM demo Login page

	# "<user>" : veut dire que j'ai creer une variable user et que j'ai initialiser sa valeur dans le tableau

	@auth	@TNR
	Scenario Outline: Successful Login
		When the user logs in with username "<user>" and password "<pwd>"
		Then the page "<page_name>" is displayed

		Examples:
			| user   | pwd      | page_name |
			| Admin  | admin123 | Dashboard |

	@auth1	@TNR
	Scenario: Successful Login2
		When the user logs in with username "Admin" and password "admin123"
		Then the page "Dashboard" is displayed

	@auth3 @TNR
    Scenario: Invalid login
   		 When the user logs in with username "wrong" and password "wrong"
   		 Then the login error message "Invalid credentials" should be displayed




