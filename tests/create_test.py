import unittest
import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactManagementTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Edge WebDriver in headless mode
        option = webdriver.EdgeOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Edge(options=option)

        # Get base URL from environment variable or use default
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost/"  

        # Generate a random name for contact creation
        cls.name_query = ''.join(random.choices(string.ascii_letters, k=10))

    def test_create(self):
        self.login()
        self.create_contact()
       

    def login(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def create_contact(self):
        create_url = self.url + '/create.php'
        self.browser.get(create_url)
      
        email_field = self.browser.find_element(By.ID, "email")
        email_field.send_keys("test@example.com")
        phone_field = self.browser.find_element(By.ID, "phone")
        phone_field.send_keys("test1234567890")
        title_field = self.browser.find_element(By.ID, "title")
        title_field.send_keys("Developer")
        name_field = self.browser.find_element(By.ID, "name")
        name_field.send_keys(self.name_query)
        
        # Submit the form
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Verify redirection to index.php
        WebDriverWait(self.browser, 10).until(EC.url_to_be(self.url + "/index.php"))

    

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')

