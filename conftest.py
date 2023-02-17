import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service


@pytest.fixture()
def driver():
    driver_service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()
