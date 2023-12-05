import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Tear down
    driver.quit()