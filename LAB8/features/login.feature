Feature: Login Tests

  Scenario: Valid Login
    Given I am on the login page
    When I enter valid username and password
    And I click the submit button
    Then I should be redirected to the inventory page

  Scenario: Invalid Login
    Given I am on the login page
    When I enter invalid username and password
    And I click the submit button
    Then I should see an error message

  Scenario: Empty Username
    Given I am on the login page
    When I leave the username field empty
    And I enter a valid password
    And I click the submit button
    Then I should see an error message for empty username

  Scenario: Empty Password
    Given I am on the login page
    When I enter a valid username
    And I leave the password field empty
    And I click the submit button
    Then I should see an error message for empty password

  Scenario: Special Characters in Username
    Given I am on the login page
    When I enter a username with special characters
    And I enter a valid password
    And I click the submit button
    Then I should see an error message for invalid credentials

  Scenario: Special Characters in Password
    Given I am on the login page
    When I enter a valid username
    And I enter a password with special characters
    And I click the submit button
    Then I should see an error message for invalid credentials

  Scenario: Uppercase Username
    Given I am on the login page
    When I enter an uppercase username
    And I enter a valid password
    And I click the submit button
    Then I should see an error message for invalid credentials

  Scenario: Uppercase Password
    Given I am on the login page
    When I enter a valid username
    And I enter an uppercase password
    And I click the submit button
    Then I should see an error message for invalid credentials
