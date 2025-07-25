# ⬇ Связь с ручным тест-кейсом
# Тест-кейс: TC_SIGNUP_002 — Попытка регистрации с уже зарегистрированным email
# Расположение ручного теста: test-cases/manual-automated/TC_SIGNUP_002_existing-email.md

import json
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Загрузка и подготовка данных пользователей
def load_users():
    with open("data/registered_users.json") as f:
        users = json.load(f)
        return users

@pytest.mark.parametrize("user", load_users())
def test_failed_signup(driver, user):
    wait = WebDriverWait(driver, 10)
    
    home = HomePage(driver)
    home.open_website()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed() or logo.get_attribute("src"), "Logo image is not present"

    home.go_to_signup()

    # Проверить, что текст "New User Signup!" присутствует
    signup_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
    assert signup_heading.is_displayed(), "New User Signup! heading is not visible"
    
    login = LoginPage(driver)
    login.fill_signup_form(user)

    # Проверить, что текст "Email Address already exist!" присутствует
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Email Address already exist!']")))
    assert "email address already exist!" in error_message.text.strip().lower(), "Error message is not visible or incorrect"
