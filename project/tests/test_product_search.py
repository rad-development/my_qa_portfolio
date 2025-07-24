from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage

def test_product_search(driver):
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

    # Поиск товаров по запросу "Dress"
    signup_page = SignupPage(driver)
    signup_page.fill_input(By.ID, "search_product", "Dress")

    product_page = ProductsPage(driver)
    product_page.click_confirm_button()

    # Проверить, что текст "Searched Products" присутствует
    product_search_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Searched Products']")))
    assert product_search_heading.is_displayed(), "Searched Products heading is not visible"

    product_page.wait_for_products_container()

    # Получаем список товаров
    products = product_page.get_all_products() 
    assert len(products) > 0, "Список продуктов пуст"
    print("Количество найденных товаров по запросу Dress =",len(products))

 

