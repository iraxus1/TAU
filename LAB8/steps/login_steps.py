from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@when("I am on the login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@given("I enter valid username and password")
def step_impl(context):
    context.username = context.driver.find_element(By.ID, "user-name")
    context.password = context.driver.find_element(By.ID, "password")
    context.username.send_keys("standard_user")
    context.password.send_keys("secret_sauce")

@given("I enter invalid username and password")
def step_impl(context):
    context.username = context.driver.find_element(By.ID, "user-name")
    context.password = context.driver.find_element(By.ID, "password")
    context.username.send_keys("invalid_user")
    context.password.send_keys("invalid_password")

@given("I leave the username field empty")
def step_impl(context):
    context.username = context.driver.find_element(By.ID, "user-name")
    context.password = context.driver.find_element(By.ID, "password")
    context.username.send_keys("")

@given("I enter a valid password")
def step_impl(context):
    context.password.send_keys("secret_sauce")

@given("I enter a valid username")
def step_impl(context):
    context.username.send_keys("standard_user")

@given("I leave the password field empty")
def step_impl(context):
    context.password.send_keys("")

@given("I enter a username with special characters")
def step_impl(context):
    context.username.send_keys("#$%^&*")

@given("I enter a password with special characters")
def step_impl(context):
    context.password.send_keys("#$%^&*")

@given("I enter an uppercase username")
def step_impl(context):
    context.username.send_keys("STANDARD_USER")

@given("I enter an uppercase password")
def step_impl(context):
    context.password.send_keys("SECRET_SAUCE")

@when("I click the submit button")
def step_impl(context):
    context.submit = context.driver.find_element(By.ID, "login-button")
    context.submit.click()

@then("I should be redirected to the inventory page")
def step_impl(context):
    assert "inventory.html" in context.driver.current_url

@then("I should see an error message")
def step_impl(context):
    assert "inventory.html" not in context.driver.current_url

@then("I should see an error message for empty username")
def step_impl(context):
    error_message = context.driver.page_source
    assert "Epic sadface: Username is required" in error_message

@then("I should see an error message for empty password")
def step_impl(context):
    error_message = context.driver.page_source
    assert "Epic sadface: Password is required" in error_message

@then("I should see an error message for invalid credentials")
def step_impl(context):
    error_message = context.driver.page_source
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def after_scenario(context, scenario):
    context.driver.quit()
