import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pages.signup_page import SignupPage

def setup_driver():
    profile = FirefoxProfile()
    # Disable image loading for faster execution
    profile.set_preference("permissions.default.image", 2)
    options = Options()
    options.profile = profile

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver

def register_users():
    # Load users from the JSON file
    with open("data/registered_users.json", encoding='utf-8') as f:
        users = json.load(f)

    for user in users:
        driver = setup_driver()
        signup = SignupPage(driver)
        try:
            print(f"Registering user: {user['name']}")
            
            signup.go_to_signup()
            signup.fill_signup_form(user)
            signup.fill_account_info(user)
            signup.submit_account()
            signup.click_continue()
            
            print(f"Successfully registered user: {user['name']}")
        
        except Exception as e:
            print(f"Failed to register user {user['name']}: {str(e)}")
        
        finally:
            driver.quit()

if __name__ == "__main__":
    register_users()