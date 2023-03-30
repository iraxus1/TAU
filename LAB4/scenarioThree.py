import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestScenarioThree(unittest.TestCase):
    
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
    
    def test_additional_feature(self):
        driver = self.driver
        # Przejście do strony logowania
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.submit.click()
        # Sprawdzenie, czy widoczna jest wiadomość o poprawnym zalogowaniu
        self.assertTrue("inventory.html" in self.driver.current_url)
        # Znajdowanie produktu i sprawdzenie, czy ma odpowiednią cenę
        product_element = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        price_element = product_element.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")
        self.assertEqual("$29.99", price_element.text)  

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
