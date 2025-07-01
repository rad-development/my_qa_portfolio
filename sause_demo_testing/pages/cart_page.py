from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CLASS_NAME, "checkout_button")  # Обычная кнопка "Оформить"
        self.alt_checkout_button = (By.CLASS_NAME, "btn_visual_failure")  # Альтернативная кнопка (если визуальная ошибка)

    def click_checkout(self):
        # Нажатие на кнопку оформления заказа с учетом возможных вариантов отображения
        try:
            self.driver.find_element(*self.alt_checkout_button).click()
        except NoSuchElementException:
            self.driver.find_element(*self.checkout_button).click()
