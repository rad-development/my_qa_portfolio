from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")      # Поле ввода имени пользователя
        self.password = (By.ID, "password")       # Поле ввода пароля
        self.login_button = (By.ID, "login-button")  # Кнопка входа

    def login(self, username_text, password_text):
        # Ввод имени пользователя и пароля, затем клик по кнопке входа
        self.driver.find_element(*self.username).send_keys(username_text)
        self.driver.find_element(*self.password).send_keys(password_text)
        self.driver.find_element(*self.login_button).click()
