import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage

# Тест выполняется для каждого указанного пользователя
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])

def test_sauce_demo(username, password):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    try:
        # Авторизация
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        login = LoginPage(driver)
        login.login(username, password)

        # Проверка успешного входа
        wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
        assert "inventory.html" in driver.current_url

        # Добавление товаров в корзину
        wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        products = ProductsPage(driver)
        products.add_item_to_cart("add-to-cart-sauce-labs-backpack")
        products.add_item_to_cart("add-to-cart-sauce-labs-bike-light")
        products.add_item_to_cart("add-to-cart-sauce-labs-fleece-jacket")
        if username != "visual_user":  # Один товар пропускается для visual_user
            products.add_item_to_cart("add-to-cart-sauce-labs-onesie")
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_count == "4"

        # Переход в корзину
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
        products.go_to_cart()

        # Оформление заказа
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button")))
        cart = CartPage(driver)
        cart.click_checkout()

        # Ввод данных пользователя
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        checkout = CheckoutPage(driver)
        checkout.enter_user_info("First", "Last", "12345")

        # Продолжение оформления
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-button")))
        checkout.continue_checkout()

        # Завершение оформления
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_action")))
        checkout.finish_checkout()

        # Проверка завершения и возврат к списку товаров
        wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
        finish = FinishPage(driver)
        assert "checkout-complete.html" in driver.current_url 
        finish.back_to_products()
    finally:
        # Закрытие браузера в любом случае (даже при ошибке)
        driver.quit()
