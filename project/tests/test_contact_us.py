# ⬇ Связь с ручным тест-кейсом
# Тест-кейс: TC_CONTACT_001 — Отправка формы "Contact Us"
# Расположение ручного теста: test-cases/manual-automated/TC_CONTACT_001_contact-us-form.md

import json
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage

# Загрузка и подготовка данных пользователей
def load_users():
    with open("data/users_contact_us_form.json") as f:
        users = json.load(f)
        return users

@pytest.mark.parametrize("user", load_users())
def test_contact_us(driver, user):
    wait = WebDriverWait(driver, 10)

    home = HomePage(driver)
    home.open_website()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed(), "Logo image is not present"

    home.go_to_contact_us()

    # Проверить, что текст Get In Touch присутствует
    contact_form_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Get In Touch']")))
    assert contact_form_heading.is_displayed(), "New User Signup! heading is not visible"

    contact_us = ContactUsPage(driver)
    contact_us.fill_contact_us_form(user)
    contact_us.choose_file(user)

    # Проверить, загрузился ли файл
    file_input = driver.find_element(By.NAME, "upload_file")
    assert file_input.get_attribute("value"), "Файл не выбран: значение пустое"

    contact_us.submit_feedback()
    contact_us.confirm_alert()

    # Проверяем, что сообщение об успехе отображается
    success_message_text = "Success! Your details have been submitted successfully."
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.status.alert.alert-success")))
    assert success_message_text in success_message.text, "Успешное сообщение не отображается или текст отличается"

    contact_us.click_home_button()

    # Проверить, что логотип присутствует
    logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left img")
    assert logo.is_displayed(), "Logo image is not present"



