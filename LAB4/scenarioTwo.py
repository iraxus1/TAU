import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScenarioTwo(unittest.TestCase):
    usernameErrorMessage = "Epic sadface: Username is required"
    passwordErrorMessage = "Epic sadface: Password is required"
    invalidCredentialsErrorMessage = "Epic sadface: Username and password do not match any user in this service"
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
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        self.submit = self.driver.find_element(By.ID, "login-button")

    def tearDown(self):
        self.driver.quit()

    def testValidLogin(self): 
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertTrue("inventory.html" in self.driver.current_url)

    def testInvalidLogin(self):
        self.username.send_keys("invalid_user")
        self.password.send_keys("invalid_password")
        self.submit.click()

        self.assertFalse("inventory.html" in self.driver.current_url)

    def testEmptyUsername(self):
        self.username.send_keys("")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.usernameErrorMessage, self.driver.page_source)

    def testEmptyPassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("")
        self.submit.click()

        self.assertIn(self.passwordErrorMessage, self.driver.page_source)

    def testSpecialCharactersInUsername(self):
        self.username.send_keys("#$%^&*")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testSpecialCharactersInPassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("#$%^&*")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testCaseUppercaseUsername(self):
        self.username.send_keys("STANDARD_USER")
        self.password.send_keys("secret_sauce")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

    def testCaseUppercasePassword(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("SECRET_SAUCE")
        self.submit.click()

        self.assertIn(self.invalidCredentialsErrorMessage, self.driver.page_source)

if __name__ == "__main__":
    unittest.main()