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

@then('I find a product with the correct price "{price}"')
def verify_product_price(context, price):
    product_element = context.driver.find_element(By.CLASS_NAME, "inventory_item_name")
    price_element = product_element.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")
    assert price == price_element.text