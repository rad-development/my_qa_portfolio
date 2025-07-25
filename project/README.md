# UI Автотесты для AutomationExercise.com

Проект содержит автоматизированные UI-тесты для сайта [automationexercise.com](https://automationexercise.com), реализованные с использованием **Selenium**, **pytest** и **Page Object Model (POM)**.

Автотесты покрывают ключевые пользовательские сценарии, включая регистрацию, авторизацию, отправку форм и поиск товаров.

🔍 Связанные ручные тест-кейсы расположены в директории:  
[test-cases/manual-automated/](/test-cases/manual-automated/)

---

## 📁 Структура проекта

```
project/
│
├── pages/
│   └── signup_page.py              # Page Object модель для страницы регистрации
│   └── login_page.py               # Page Object модель для страницы входа
│   └── home_page.py                # Page Object модель для главной страницы 
│   └── contact_us_page.py          # Page Object модель для страницы "Обратная связь"
│   └── products_page.py            # Page Object модель для страницы товаров
│
├── data/
│   ├── registered_users.json       # Данные зарегистрированных пользователей
│   ├── unregistered_users.json     # Данные незарегистрированных пользователей
│   ├── users.json                  # Тестовые пользователи для регистрации и последующего удаления в тестах
│   ├── users_contact_us_form.json  # Тестовые пользователи для страницы "Обратная связь"
│   ├── product_search.json         # Набор поисковых запросов для проверки поиска товаров 
│   └── files/                      # Файлы, прикрепляемые к форме обратной связи в test_contact_us.py
│       ├── geeta_file.txt
│       ├── liam_file.txt
│       └── natalie_file.txt
│
├── tests/
│   └── test_signup.py              # Тест-кейс на успешную регистрацию
│   └── test_login.py               # Тест-кейс на успешный вход
│   └── test_failed_login.py        # Тест-кейс на вход с неправильным email и паролем
│   └── test_failed_signup.py       # Тест-кейс регистрации с существующим email
│   └── test_contact_us.py          # Тест-кейс формы "Обратная связь"
│   └── test_cases_page_test.py     # Тест-кейс: Проверка страницы с тест-кейсами
│   └── test_products_page.py       # Тест-кейс: Проверка страницы товаров
│   └── test_product_search.py      # Тест-кейс: Проверка поиска товаров
│
├── conftest.py                     # Общие фикстуры и настройки окружения
├── requirements.txt                # Список зависимостей
└── README.md                       # Документация проекта

```
## Используемые технологии

- Python 3.10+  
- Selenium WebDriver  
- Pytest  
- Firefox WebDriver (GeckoDriver)  
- Chrome WebDriver (ChromeDriver)

## 🚀 Как запустить

Установите зависимости:

```bash
pip install -r requirements.txt
```

Запустите все тесты:

```bash
pytest tests/
```

Или отдельный тест-файл:

```bash
pytest tests/test_signup_flow.py

pytest tests/test_product_search.py -s -v
```