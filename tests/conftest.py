import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config.settings import BASE_URL
from utils import attach


@pytest.fixture(scope="function")
def browser():
    """Инициализация браузера для каждого теста с разворачиванием на полный экран."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    try:
        attach.add_screenshot(driver)
        attach.add_html(driver)
        attach.add_logs(driver)
        attach.add_video(driver)
    except Exception as e:
        allure.attach(str(e), name="attach_error", attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture
def headers():
    """Фикстура для заголовков с токеном авторизации."""
    token = get_token_from_api()
    return {
        'accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': BASE_URL,
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }


def get_token_from_api():
    """Получение токена доступа из cookies API."""
    response = requests.get(BASE_URL)
    cookies = response.cookies
    token = cookies.get('access-token')
    if token:
        return token[9:]
    raise ValueError("Не удалось получить токен доступа")
