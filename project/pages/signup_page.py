from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SignupPage:
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

    def fill_account_info(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, "first_name")))
        self.fill_input(By.ID, "first_name", user["first_name"])
        self.fill_input(By.ID, "last_name", user["last_name"])
        self.fill_input(By.XPATH, '//input[@data-qa="company"]', user["company"])
        self.fill_input(By.XPATH, '//input[@data-qa="address"]', user["address"])
        self.fill_input(By.XPATH, '//input[@data-qa="address2"]', user["address2"])
        self.fill_input(By.XPATH, '//input[@data-qa="state"]', user["state"])
        self.fill_input(By.XPATH, '//input[@data-qa="city"]', user["city"])
        self.fill_input(By.XPATH, '//input[@data-qa="zipcode"]', user["zipcode"])
        self.fill_input(By.XPATH, '//input[@data-qa="mobile_number"]', user["mobile"])
        self.fill_input(By.XPATH, '//input[@data-qa="password"]', user["password"])

        self.wait.until(EC.element_to_be_clickable((By.ID, "newsletter"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "optin"))).click()

        if user["gender"] == "Mr":
            self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))).click()
        elif user["gender"] == "Mrs":
            self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender2"))).click() 

        Select(self.driver.find_element(By.ID, "days")).select_by_value(str(user["date"]["day"]))
        Select(self.driver.find_element(By.ID, "months")).select_by_value(str(user["date"]["month"]))
        Select(self.driver.find_element(By.ID, "years")).select_by_value(str(user["date"]["year"]))

        country_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "country")))
        Select(country_dropdown).select_by_visible_text(user["country"])

    def submit_account(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="create-account"]'))).click()

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-qa="continue-button"]'))).click()

    def delete_account(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete Account"))).click()
    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    def go_to_home_page(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()

