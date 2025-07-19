from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_products_container(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.features_items")))

    def get_all_products(self):
        container = self.wait_for_products_container()
        return container.find_elements(By.CSS_SELECTOR, "div.col-sm-4")

    def click_first_product_view(self, products):
        first_view_button = products[0].find_element(By.LINK_TEXT, "View Product")
        first_view_button.click()
