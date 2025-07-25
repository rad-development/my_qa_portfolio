# ⬇ Связь с ручным тест-кейсом
# Тест-кейс: TC_LOGIN_003 — Вход пользователя с некорректным email и паролем
# Расположение ручного теста: test-cases/manual-automated/TC_LOGIN_003_invalid-credentials.md

import json
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Загрузка и подготовка данных пользователей
def load_users():
    with open("data/unregistered_users.json") as f:
        users = json.load(f)
        return users

@pytest.mark.parametrize("user", load_users())
def test_failed_login(driver, user):
    wait = WebDriverWait(driver, 10)
    
    home = HomePage(driver)
    home.open_website()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed() or logo.get_attribute("src"), "Logo image is not present"
    
    home.go_to_signup()

    # Проверить, что текст "Login to your account" присутствует
    login_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
    assert login_heading.is_displayed(), "Login to your account heading is not visible"
    
    login = LoginPage(driver)
    login.fill_login_form(user)
        
    # Ожидание появления текста "Your email or password is incorrect!"
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']")))
    assert error_message.text.strip() == "Your email or password is incorrect!", "Incorrect or missing login error message"
