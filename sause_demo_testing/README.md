SauceDemo Selenium Test (Pytest)

Этот код — учебный автоматизированный тест на Python с использованием **Selenium** и **Pytest**.

**Описание**:  
Тест покрывает полный пользовательский путь на (https://www.saucedemo.com/):
- авторизация
- добавление товаров в корзину
- оформление заказа
- завершение покупки

**Структура Кода**:  
Используется паттерн Page Object Model (`/pages/`) для упрощения поддержки и масштабирования.

**Технологии**:
- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Pytest-HTML (для отчётов)

**Запуск теста с HTML-отчётом**:
```bash
pytest --html=report.html --self-contained-html
```