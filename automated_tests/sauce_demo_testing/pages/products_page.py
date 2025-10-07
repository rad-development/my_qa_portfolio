from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")  # Иконка корзины

    def add_item_to_cart(self, item_id):
        # Добавление товара в корзину по ID
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        # Переход в корзину
        self.driver.find_element(*self.cart_icon).click()
