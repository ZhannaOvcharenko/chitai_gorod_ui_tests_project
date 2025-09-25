import requests
import pytest
import allure
from config.settings import BASE_URL
from pages.main_page import MainPage
from pages.book_page import BookPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на доступность главной страницы")
def test_page_accessible(browser):
    main_page = MainPage(browser)

    with allure.step("Отправка запроса на главную страницу"):
        response = requests.get(BASE_URL)
        assert response.status_code == 200, "Страница не открылась, статус отличается от 200"

    with allure.step("Открытие главной страницы в браузере"):
        browser.get(BASE_URL)

    with allure.step("Закрытие всплывающего окна"):
        main_page.close_pop_up()
        assert main_page.is_pop_up_closed(), "Всплывающее окно не закрыто"

    with allure.step("Закрытие уведомления о куки"):
        main_page.close_cookie_notice()
        assert main_page.is_cookie_notice_closed(), "Уведомление о куки не закрыто"


@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на открытие страницы информации о книге")
def test_open_book_page(browser):
    main_page = MainPage(browser)
    book_page = BookPage(browser)

    with allure.step("Переход на страницу информации о книге"):
        book_page.open_book_page()

    with allure.step("Проверка статуса кода 200 для страницы информации о книге"):
        book_page_url = browser.current_url
        response = requests.get(book_page_url)
        assert response.status_code == 200, "Страница информации о книге не открылась, статус отличается от 200"


@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на добавление книги в корзину с проверкой иконки")
def test_add_book_to_cart(browser):
    book_page = BookPage(browser)

    with allure.step("Нажатие на кнопку 'Купить'"):
        book_page.add_book_to_cart()

    with allure.step("Проверка, что в значке корзины появилась цифра '1'"):
        try:
            cart_badge = WebDriverWait(browser, 10).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "header-cart__badge"), "1")
            )
            assert cart_badge, "Цифра '1' не появилась в значке корзины"
        except Exception as e:
            print(f"Ошибка при проверке значка корзины: {e}")
            assert False, "Цифра '1' не появилась в значке корзины"


@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на переход в корзину после добавления книги")
def test_go_to_cart(browser):
    cart_page = CartPage(browser)
    cart_url = f"{BASE_URL}/cart"

    with allure.step("Нажатие на иконку корзины"):
        cart_page.go_to_cart()

    with allure.step("Проверка статус кода 200 для страницы корзины"):
        response = requests.get(cart_url)
        assert response.status_code == 200, "Страница корзины не открылась, статус отличается от 200"


@allure.severity("critical")
@allure.feature("UI тесты")
@allure.title("Тест на очистку корзины")
def test_clear_cart(browser):
    cart_page = CartPage(browser)

    with allure.step("Нажатие на кнопку 'Очистить корзину'"):
        cart_page.clear_cart()

    assert cart_page.is_cart_empty(), "Сообщение 'Корзина очищена' не появилось"