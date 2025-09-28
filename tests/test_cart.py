import allure
from pages.book_page import BookPage
from pages.cart_page import CartPage


@allure.epic("UI Читай-Город")
@allure.feature("Корзина")
class TestCart:

    @allure.story("Добавление книги в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self):
        book_page = BookPage().open("/product/vojna-i-mir-123456").add_to_cart()
        CartPage().open().should_contain_book("Война и мир")

    @allure.story("Удаление книги из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_from_cart(self):
        CartPage().open().remove_book().should_be_empty()
