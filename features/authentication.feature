Feature:   Authentication Test Suite

	As a user, a want to authenticate wth admin, user, super user

    Background: shared preconditions
		Given the user opens OrangeHRM demo Login page

	@auth	@TNR
	Scenario Outline: Successful Login
		When the user logs in with username "<user>" and password "<pwd>"
		Then the page "<page_name>" is displayed

		Examples:
			| user   | pwd      | page_name |
			| Admin  | admin123 | Dashboard |

