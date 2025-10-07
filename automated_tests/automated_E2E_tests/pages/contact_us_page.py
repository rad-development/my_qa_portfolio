from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_input(self, by, locator, value):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.clear()
        element.send_keys(value)
    
    def fill_contact_us_form(self, user):
        self.fill_input(By.XPATH, '//input[@data-qa="name"]', user["name"])
        self.fill_input(By.XPATH, '//input[@data-qa="email"]', user["email"])
        self.fill_input(By.XPATH, '//input[@data-qa="subject"]', user["subject"])
        self.fill_input(By.XPATH, '//textarea[@data-qa="message"]', user["message"])

    def choose_file(self, user):
        file_input = self.wait.until(EC.presence_of_element_located((By.NAME, "upload_file")))
        file_input.send_keys(user["file_path"])

    def submit_feedback(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-qa="submit-button"]'))).click()
    
    def confirm_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_home_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success[href='/']"))).click()



