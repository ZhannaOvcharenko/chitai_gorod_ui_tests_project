import allure
import pytest
from pages.book_page import BookPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("open_main_page")
class TestBookPage:

    @allure.story("Добавление книги в корзину с product страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_book_to_cart(self):
        BookPage().open("product/dzheyn-eyr-2544490").add_to_cart()
        assert CartPage.has_books(), "Книга не добавилась в корзину"
