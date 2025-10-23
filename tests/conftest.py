import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import be
from selene.support.shared import browser
from selene.core import config  # noqa: F401
from utils import attach
from pages.main_page import MainPage

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    """Настройка и запуск браузера перед каждым тестом."""

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    if os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", os.getenv("BROWSER_VERSION", "128.0"))
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    if all([selenoid_login, selenoid_pass, selenoid_url]):
        remote_url = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = os.getenv("BASE_URL", "https://www.chitai-gorod.ru")
    browser.config.window_width = int(os.getenv("WIDTH", 1920))
    browser.config.window_height = int(os.getenv("HEIGHT", 1080))
    browser.config.timeout = 10

    yield

    try:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)
    finally:
        browser.quit()


@pytest.fixture()
def open_main_page():
    """Открывает главную страницу и принимает cookies, если нужно."""
    page = MainPage()
    page.open_main_page()

    cookie_buttons = browser.all("[data-testid='accept-cookies']").by(be.visible)
    if len(cookie_buttons) > 0:
        cookie_buttons[0].click()

    return page
