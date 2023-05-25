Feature: Additional Feature

Background:
Given I open the website

Scenario: Verify additional feature
When I enter valid username and password
And I click the login button
Then I should be redirected to the inventory page
And I find a product with the correct price "$29.99"