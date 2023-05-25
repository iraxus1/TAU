from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I open the website')
def open_website(context):
    context.driver.get("https://www.saucedemo.com/")

@when('I enter valid username and password')
def enter_valid_credentials(context):
    username = context.driver.find_element(By.ID, "user-name")
    password = context.driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

@when('I click the login button')
def click_login_button(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then('I should be redirected to the inventory page')
def verify_redirect_to_inventory_page(context):
    assert "inventory.html" in context.driver.current_url

@then('I should not be redirected to the inventory page')
def verify_not_redirect_to_inventory_page(context):
    assert "inventory.html" not in context.driver.current_url

@when('I leave the username field empty')
def leave_username_field_empty(context):
    username = context.driver.find_element(By.ID, "user-name")
    username.clear()

@when('I enter a valid password')
def enter_valid_password(context):
    password = context.driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

@then('I should see an error message "{message}"')
def verify_error_message(context, message):
    assert message in context.driver.page_source