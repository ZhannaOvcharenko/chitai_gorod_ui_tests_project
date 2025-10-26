import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    """
    Настройка и запуск браузера перед каждым тестом.
    Поддерживает как локальный запуск, так и удалённый (через Selenoid).
    """

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument('--headless')

    if selenoid_url:
        browser.config.driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options,
        )
    else:
        browser.config.driver = webdriver.Chrome(options=options)

    browser.config.base_url = "https://www.chitai-gorod.ru"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def open_main_page(setup_browser):
    """
    Открывает главную страницу Читай-город.
    Использует PageObject MainPage при наличии, иначе просто browser.open('/').
    """

    from pages.main_page import MainPage

    main_page = MainPage()

    if hasattr(main_page, "open") and callable(main_page.open):
        main_page.open()
    else:
        browser.open("/")

    if hasattr(main_page, "accept_cookies_if_present") and callable(main_page.accept_cookies_if_present):
        try:
            main_page.accept_cookies_if_present()
        except (AttributeError, RuntimeError):
            pass

    return main_page
