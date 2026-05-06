Feature: Menu Navigation Test Suite

	As a user, i want to access to the different pages
    
    @navigation @TNR
	Scenario Outline: Access to Pages by Name
		Given the user opens OrangeHRM demo Login page
        And the user is logged in
		When the user opens the page "<page_name>" menu
		Then the page "<page_name>" is displayed

		Examples: example set
			| page_name   |
			| PIM         |
			| Time        |
			| Leave       |
			| Recruitment |
