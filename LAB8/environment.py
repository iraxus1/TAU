from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()

def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)
