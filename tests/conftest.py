import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from config.settings import BASE_URL


@pytest.fixture(scope="session")
def browser():
    """Инициализация браузера для сессии с разворачиванием на полный экран."""
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()  # Разворачивание окна на полный экран
    yield browser
    browser.quit()  # Закрытие браузера после выполнения всех тестов


@pytest.fixture
def headers():
    """Фикстура для заголовков с токеном авторизации."""
    token = get_token_from_api()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': BASE_URL,
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    return headers


def get_token_from_api():
    """Получение токена доступа из cookies API."""
    response = requests.get(BASE_URL)
    cookies = response.cookies
    token = cookies.get('access-token')
    if token:
        return token[9:]  # Извлекаем токен, начиная с 9 символа
    else:
        raise ValueError("Не удалось получить токен доступа")
