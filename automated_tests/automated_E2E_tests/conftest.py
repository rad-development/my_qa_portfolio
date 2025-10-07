import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

@pytest.fixture
def driver():
    profile = FirefoxProfile()
    # Отключаем загрузку изображений
    profile.set_preference("permissions.default.image", 2)
    options = Options()
    options.profile = profile

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def chrome_driver():
    options = ChromeOptions()
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()