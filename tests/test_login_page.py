import time
import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:
    @pytest.mark.regression
    def test_login_page(self, driver):
        driver.get("https://www.redbus.in/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='account_dd']/div[1]/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='user_sign_in_sign_up']/span").click()
        time.sleep(5)
        assert driver.find_element(By.XPATH, "//iframe[@class='modalIframe']")

    @pytest.mark.smoke
    def test_validate_url(self, driver):
        driver.get("https://www.redbus.in/")
        time.sleep(2)
        actual_url = driver.current_url
        assert actual_url == "https://www.redbus.in/"

    def pytest_sessionstart(session):
        print("pytest_session start")

    def pytest_sessionfinish(session):
        print("pytest_session finish")

    @pytest.mark.skip
    def test_skip(self):
        pass
