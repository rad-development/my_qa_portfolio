from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage

def test_cases_page_test(driver):
    wait = WebDriverWait(driver, 10)

    home = HomePage(driver)
    home.open_website()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed(), "Logo image is not present"

    home.go_to_test_cases()
    
    # Проверить, что заголовок "Test Cases" присутствует
    test_cases_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2/b[text()='Test Cases']")))
    assert test_cases_heading.is_displayed(), "Test Cases heading is not visible"

