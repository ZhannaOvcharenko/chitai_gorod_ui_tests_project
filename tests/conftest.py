import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from utils import attach
from dotenv import load_dotenv
from pages.main_page import MainPage

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    if not all([selenoid_login, selenoid_pass, selenoid_url]):
        raise ValueError(
            "Ошибка: переменные SELENOID_LOGIN, SELENOID_PASS или SELENOID_URL не заданы."
        )

    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", os.getenv("BROWSER_VERSION", "128.0"))
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.driver = driver
    browser.config.base_url = os.getenv("BASE_URL", "https://www.chitai-gorod.ru")
    browser.config.window_width = int(os.getenv("WIDTH", 1920))
    browser.config.window_height = int(os.getenv("HEIGHT", 1080))
    browser.config.timeout = 10

    yield

    # Allure attachments
    try:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)
    finally:
        browser.quit()


@pytest.fixture()
def open_main_page():
    """Фикстура для открытия главной страницы"""
    page = MainPage()
    page.open_main_page().accept_cookies_if_present()
    return page
