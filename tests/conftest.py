import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
from selenium.common.exceptions import WebDriverException

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():

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

    for attach_func in (attach.add_screenshot, attach.add_logs, attach.add_video):
        try:
            attach_func(browser)
        except WebDriverException as e:
            print(f"Не удалось добавить артефакт {attach_func.__name__}: {e}")

    browser.quit()


@pytest.fixture()
def open_main_page(setup_browser):

    from pages.main_page import MainPage

    main_page = MainPage()
    main_page.open()
    try:
        main_page.accept_cookies_if_present()
    except AttributeError:
        # Если метод или кнопка отсутствует, просто продолжаем
        pass

    return main_page
