import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestScenarioOne(unittest.TestCase):

    browser_type = ""
    
    def start_browser(self, browser_type):
        if browser_type == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_type == "edge":
            self.driver = webdriver.Edge()
        elif browser_type == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_type == "opera":
            self.driver = webdriver.Opera()
        else:
            raise ValueError("Unsupported browser type")

        return self.driver
    
    def setUp(self):
        self.driver = self.start_browser(self.browser_type)
        self.driver.get("https://www.saucedemo.com/")
        self.logo = self.driver.find_element(By.CLASS_NAME, "login_logo")
        self.wrapper = self.driver.find_element(By.CLASS_NAME, "login_wrapper")
        self.loginButton = self.driver.find_element(By.ID, "login_button_container")
        self.footer = self.driver.find_element(By.CLASS_NAME, "login_credentials_wrap")
    
    def test_page_load(self):
        driver = self.driver
        # Sprawdzenie, czy tytuł strony jest poprawny
        self.assertEqual("Swag Labs", driver.title)
        # Sprawdzenie, czy logo strony jest widoczne
        self.assertTrue(self.logo.is_displayed())
        # sprawdzenie, czy wrapper jest widoczny
        self.assertTrue(self.wrapper.is_displayed())
        # sprawdzenie, czy footer jest widoczny
        self.assertTrue(self.footer.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

