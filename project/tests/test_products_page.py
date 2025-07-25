# ⬇ Связь с ручным тест-кейсом
# Тест-кейс: TC_PRODUCTS_001 — Проверка страницы товаров и деталей товара
# Расположение ручного теста: test-cases/manual-automated/TC_PRODUCTS_001_product-details.md

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.products_page import ProductsPage

def test_products_page(driver):
    wait = WebDriverWait(driver, 10)

    home = HomePage(driver)
    home.open_website()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed() or logo.get_attribute("src"), "Logo image is not present"

    home.go_to_products()

    # Проверить, что текст "All Products" присутствует
    products_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='All Products']")))
    assert products_heading.is_displayed(), "All Products heading is not visible"

    product_page = ProductsPage(driver)
    product_page.wait_for_products_container()

    # Получаем список товаров
    products = product_page.get_all_products() 
    assert len(products) > 0, "Список продуктов пуст"

    # Кликаем по "View Product" первого товара 
    product_page.click_first_product_view(products)
    assert "product_details" in driver.current_url, "User is not on product detail page"
    
    # Находим контейнер с информацией о товаре на странице детали продукта
    product_info = driver.find_element(By.CSS_SELECTOR, "div.product-information")

    # 1. Название продукта
    product_name = product_info.find_element(By.TAG_NAME, "h2")
    assert product_name.is_displayed(), "Product name is not visible"

    # 2. Категория 
    category = product_info.find_element(By.XPATH, ".//p[starts-with(text(), 'Category:')]")
    assert category.is_displayed(), "Category is not visible"

    # 3. Цена
    price = product_info.find_element(By.XPATH, ".//span/span")
    assert price.is_displayed(), "Price is not visible"

    # 4. Наличие товара
    availability = product_info.find_element(By.XPATH, ".//p[./b[text()='Availability:']]")
    assert availability.is_displayed(), "Availability is not visible"

    # 5. Состояние
    condition = product_info.find_element(By.XPATH, ".//p[./b[text()='Condition:']]")
    assert condition.is_displayed(), "Condition is not visible"

    # 6. Бренд
    brand = product_info.find_element(By.XPATH, ".//p[./b[text()='Brand:']]")
    assert brand.is_displayed(), "Brand is not visible"


