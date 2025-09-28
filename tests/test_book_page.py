import allure
from pages.book_page import BookPage
from pages.cart_page import CartPage


@allure.epic("UI Читай-Город")
@allure.feature("Страница книги")
class TestBookPage:

    @allure.story("Добавление книги в корзину с product страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_book_to_cart(self):
        BookPage().open("product/tri-tovarishcha-2666861").add_to_cart()
        CartPage().open().should_contain_book("Три товарища")
