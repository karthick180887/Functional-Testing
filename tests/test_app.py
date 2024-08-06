import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
import time

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Specify the path to the ChromeDriver executable if necessary
        chrome_service = ChromeService(executable_path='C:\\Users\\Karthick Selvam\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # Update with your path
        cls.driver = webdriver.Chrome(service=chrome_service)

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except NoSuchWindowException:
            pass

    def test_home_page(self):
        try:
            self.driver.get('http://127.0.0.1:5000/')
            self.assertIn("Welcome to the Flask App", self.driver.page_source)
        except NoSuchWindowException:
            self.fail("Window closed unexpectedly")
        except WebDriverException as e:
            self.fail(f"WebDriverException occurred: {e}")

    def test_form_submission(self):
        try:
            self.driver.get('http://127.0.0.1:5000/')
            name_input = self.driver.find_element(By.ID, 'name')
            email_input = self.driver.find_element(By.ID, 'email')
            password_input = self.driver.find_element(By.ID, 'password')
            dob_input = self.driver.find_element(By.ID, 'dob')

            name_input.send_keys("John Doe")
            email_input.send_keys("john@example.com")
            password_input.send_keys("password123")

            # Clear the date input field and set the date value using JavaScript
            self.driver.execute_script("arguments[0].value = '';", dob_input)
            self.driver.execute_script("arguments[0].value = '2000-01-01';", dob_input)

            submit_button = self.driver.find_element(By.TAG_NAME, 'button')
            submit_button.click()

            time.sleep(2)  # Wait for the response

            self.assertIn("Received: John Doe, john@example.com, password123, 2000-01-01", self.driver.page_source)
        except NoSuchWindowException:
            self.fail("Window closed unexpectedly")
        except WebDriverException as e:
            self.fail(f"WebDriverException occurred: {e}")

if __name__ == '__main__':
    unittest.main()
