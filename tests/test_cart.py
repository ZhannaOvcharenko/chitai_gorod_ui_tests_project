import allure
import pytest
from pages.book_page import BookPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("open_main_page")
class TestCart:

    @allure.story("Добавление книги в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self):
        BookPage().open("product/dzheyn-eyr-2544490").add_to_cart()
        assert CartPage.has_books(), "Книга не добавилась в корзину"

    @allure.story("Удаление книги из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_from_cart(self):
        cart = CartPage().open()
        if CartPage.has_books():
            cart.remove_all_books()
        assert not CartPage.has_books(), "Книги не удалились из корзины"
