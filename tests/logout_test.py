import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Use a compatible browser driver (adjust as needed)
        option = webdriver.EdgeOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Edge(options=option)

        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost/BadCRUD"

    def test_logout(self):
        self.login()
        self.logout()

    def login(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        # Fill in login form and submit
        username_field = self.browser.find_element(By.ID, 'inputUsername')
        username_field.send_keys('admin')
        password_field = self.browser.find_element(By.ID, 'inputPassword')
        password_field.send_keys('nimda666!')
        login_button = self.browser.find_element(By.TAG_NAME, 'button')
        login_button.click()

        # Verify successful login
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Halo, admin')]"))
        )  # Adjusted XPath for specificity

    def logout(self):
        logout_url = self.url + '/logout.php'  # Access logout URL directly
        self.browser.get(logout_url)

        # Assert redirection to login page
        WebDriverWait(self.browser, 10).until(
            EC.title_is("Login")  # Adjusted to match expected title
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
