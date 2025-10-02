import allure
import pytest
from pages.book_page import BookPage


@pytest.mark.usefixtures("open_main_page")
class TestBookPage:

    @allure.story("Добавление книги в корзину с product страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_book_to_cart(self):
        BookPage().open("product/tri-tovarishcha-2666861").add_to_cart()
