Feature:   Authentication Test Suite

	As a user, a want to authenticate wth admin, user, super user

	Scenario Outline: Successful Login
		Given the user opens OrangeHRM demo Login page
		When the user logs in with username "<user>" and password "<pwd>"
		Then the Dashboard page is displayed

		Examples:
			| user   | pwd      |
			| Admin  | admin123 |
			| Admin2 | admin128 |
			| Admin2 | admin128 |
