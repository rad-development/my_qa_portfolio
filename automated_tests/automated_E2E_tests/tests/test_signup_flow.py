# ⬇ Связь с ручным тест-кейсом
# Тест-кейс: TC_SIGNUP_001 — Проверка успешной регистрации нового пользователя
# Расположение ручного теста: test-cases/manual-automated/TC_SIGNUP_001_register-user-flow.md

import json
import random
import string
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

# Функция для генерации паролей
def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Загрузка и подготовка данных пользователей
def load_users():
    with open("data/users.json") as f:
        users = json.load(f)
        for i, user in enumerate(users):
            timestamp = int(time.time())
            user["email"] = user["email"].replace("@", f"+{timestamp+i}@")
            user["password"] = generate_password()
        return users

@pytest.mark.parametrize("user", load_users())
def test_signup_flow(driver, user):
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

    # Проверить, что текст "Enter Account Information" присутствует
    verify_enter_info_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2//b[text()='Enter Account Information']")))
    assert "enter account information" in verify_enter_info_text.text.strip().lower(), "Enter Account Information is not visible or incorrect"
    
    signup = SignupPage(driver)
    signup.fill_account_info(user)
    signup.submit_account()

    # Проверить, что текст "Account Created!" присутствует
    verify_acc_created_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2//b[text()='Account Created!']")))
    assert "account created!" in verify_acc_created_text.text.strip().lower(), "Account Created! is not visible or incorrect"

    signup.click_continue()

    # Ожидание появления текста "Logged in as <username>"
    logged_in_text = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li/a[contains(text(),'Logged in as')]/b[text()='{user['name']}']")))
    assert logged_in_text.text == user['name'], f"Logged in username is not correct, expected {user['name']}"

    home.delete_account()

    # Проверить, что текст "ACCOUNT DELETED!" присутствует
    verify_deleted_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2//b[text()='Account Deleted!']")))
    assert "account deleted!" in verify_deleted_text.text.strip().lower(), "Account Deleted! is not visible or incorrect"

    signup.click_continue()
    
    # Проверка, что кнопка "Signup / Login" снова видна после logout
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Signup / Login')]")))
    assert login_button.is_displayed(), "Logout failed — Signup/Login button not visible"