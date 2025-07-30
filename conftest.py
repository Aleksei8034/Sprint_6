from selenium import webdriver
import pytest
from data import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(Urls.scooter)
    yield driver
    driver.quit()

def pytest_make_parametrize_id(val):
    return repr(val)