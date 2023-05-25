Feature: Login Functionality

Background:
Given I open the website

Scenario: Valid Login
When I enter valid username and password
And I click the login button
Then I should be redirected to the inventory page

Scenario: Invalid Login
When I enter invalid username and password
And I click the login button
Then I should not be redirected to the inventory page

Scenario: Empty Username
When I leave the username field empty
And I enter a valid password
And I click the login button
Then I should see an error message "Epic sadface: Username is required"

Scenario: Empty Password
When I enter a valid username
And I leave the password field empty
And I click the login button
Then I should see an error message "Epic sadface: Password is required"

Scenario: Special Characters in Username
When I enter special characters in the username field
And I enter a valid password
And I click the login button
Then I should see an error message "Epic sadface: Username and password do not match any user in this service"

Scenario: Special Characters in Password
When I enter a valid username
And I enter special characters in the password field
And I click the login button
Then I should see an error message "Epic sadface: Username and password do not match any user in this service"

Scenario: Uppercase Username
When I enter an uppercase username
And I enter a valid password
And I click the login button
Then I should see an error message "Epic sadface: Username and password do not match any user in this service"

Scenario: Uppercase Password
When I enter a valid username
And I enter an uppercase password
And I click the login button
Then I should see an error message "Epic sadface: Username and password do not match any user in this service"
