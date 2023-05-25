from behave import given, then
from selenium.webdriver.common.by import By

@given('I open the website')
def open_website(context):
    context.driver.get("https://www.saucedemo.com/")

@then('I see the page title "{title}"')
def verify_page_title(context, title):
    assert title == context.driver.title

@then('I see the logo displayed')
def verify_logo_displayed(context):
    logo = context.driver.find_element(By.CLASS_NAME, "login_logo")
    assert logo.is_displayed()

@then('I see the wrapper displayed')
def verify_wrapper_displayed(context):
    wrapper = context.driver.find_element(By.CLASS_NAME, "login_wrapper")
    assert wrapper.is_displayed()

@then('I see the footer displayed')
def verify_footer_displayed(context):
    footer = context.driver.find_element(By.CLASS_NAME, "login_credentials_wrap")
    assert footer.is_displayed()