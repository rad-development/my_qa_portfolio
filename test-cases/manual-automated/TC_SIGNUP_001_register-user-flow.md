# Тест-кейс: TC_SIGNUP_001

**Название:** Проверка успешной регистрации нового пользователя

**Модуль:** Регистрация

**Тип теста:** Функциональный

**Приоритет:** Высокий

**Связанный автотест:** [project/tests/test_signup_flow.py](/project/tests/test_signup_flow.py)

---

### 🔧 Предусловия:
- Пользователь не должен быть зарегистрирован с используемым email.

---

### 🧪 Тестовые данные:

Тестовые данные находятся в файле:  
`project/data/users.json`

Для данного теста используются поля:
- **Title:** Mrs  
- **Name:** alice_smith  
- **Email:** alice_@example.com  
- **Password:** AlphaPass!2025  
- **Date of Birth (Day/Month/Year):** 15 / May / 1990  
- **Newsletter Subscription:** Да  
- **Special Offers Subscription:** Да  
- **First Name:** Alice  
- **Last Name:** Smith  
- **Company:** Alpha Corp  
- **Address (Line 1):** 123 Maple St  
- **Address (Line 2):** Suite 101  
- **Country:** Canada  
- **State:** Ontario  
- **City:** Toronto  
- **Zipcode:** M4B1B3  
- **Mobile Number:** 1234567890
---

### 📋 Описание действий:

1. Открыть браузер  
2. Перейти на сайт [http://automationexercise.com](http://automationexercise.com)   
3. Нажать кнопку **‘Signup / Login’**  
4. Ввести имя и email в разделе New User Signup!
5. Нажать кнопку **‘Signup’**  
6. Заполнить поля: Title, Name, Email, Password, Date of birth  
7. Отметить чекбокс **‘Sign up for our newsletter!’**  
8. Отметить чекбокс **‘Receive special offers from our partners!’**  
9. Заполнить поля: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number  
10. Нажать кнопку **‘Create Account’**  
11. Нажать кнопку **‘Continue’**  
12. Нажать **‘Delete Account’**  

---

### ✅ Ожидаемый результат:
- После нажатия кнопки ‘Create Account’ появляется сообщение:
"Account Created! Congratulations! Your new account has been successfully created! You can now take advantage of member privileges to enhance your online shopping experience with us."
- После нажатия кнопки ‘Delete Account’ появляется сообщение:
"Account Deleted! Your account has been permanently deleted! You can create new account to take advantage of member privileges to enhance your online shopping experience with us."
- Пользователь успешно проходит процесс регистрации, авторизуется и может удалить свой аккаунт.
- Все шаги выполняются без ошибок, все элементы видимы и активны.

---

### ❗ Фактический результат:
(заполняется после выполнения теста)

---

### 📌 Статус:
- Не выполнен / В процессе / Пройден / Не пройден (отметить после выполнения)

---

**Исполнитель:** [Имя]

**Дата создания:** 2025-07-24

**Дата выполнения:** (не выполнен)
