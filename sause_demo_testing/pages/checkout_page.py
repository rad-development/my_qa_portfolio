from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname = (By.ID, "first-name")          # Поле имени
        self.lastname = (By.ID, "last-name")            # Поле фамилии
        self.postal_code = (By.ID, "postal-code")       # Поле почтового индекса
        self.continue_button = (By.CLASS_NAME, "submit-button")  # Кнопка продолжения
        self.finish_button = (By.CLASS_NAME, "btn_action")       # Кнопка завершения

    def enter_user_info(self, firstname, lastname, zipcode):
        # Заполнение формы информации о пользователе
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(zipcode)

    def continue_checkout(self):
        # Переход к следующему этапу оформления
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        # Завершение оформления заказа
        self.driver.find_element(*self.finish_button).click()
