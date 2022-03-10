from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")


@pytest.mark.sample
def test_datas1():
    driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("www.google.com")
    assert driver.title == "Google"
@pytest.mark.sample
def test_datas2():
    driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("www.youtube.com")
    assert driver.title == "youtube"