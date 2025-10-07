from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_website(self):
        self.driver.get("https://automationexercise.com/")

    def go_to_signup(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()
    
    def go_to_test_cases(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Test Cases"))).click()

    def go_to_products(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li/a[contains(., 'Products')]"))).click()
         
    def go_to_contact_us(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact us"))).click()

    def delete_account(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))).click()
    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    def go_to_home_page(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
