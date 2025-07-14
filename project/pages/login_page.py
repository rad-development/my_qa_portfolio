from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_signup(self):
        self.driver.get("https://automationexercise.com/")
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()

    def fill_input(self, by, locator, value):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.clear()
        element.send_keys(value)

    def fill_login_form(self, user):
        self.fill_input(By.XPATH, '//input[@data-qa="login-email"]', user["email"])
        self.fill_input(By.XPATH, '//input[@data-qa="login-password"]', user["password"])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="login-button"]'))).click()
        
    def fill_signup_form(self, user):
        self.fill_input(By.XPATH, '//input[@data-qa="signup-name"]', user["name"])
        self.fill_input(By.XPATH, '//input[@data-qa="signup-email"]', user["email"])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="signup-button"]'))).click()

