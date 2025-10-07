from selenium.webdriver.common.by import By

class FinishPage:
    def __init__(self, driver):
        self.driver = driver
        self.back_button = (By.ID, "back-to-products")  # Кнопка возврата к списку товаров

    def back_to_products(self):
        # Возврат на страницу с товарами
        self.driver.find_element(*self.back_button).click()
