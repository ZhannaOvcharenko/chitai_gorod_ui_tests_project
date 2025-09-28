import allure
from pages.book_page import BookPage


@allure.epic("UI Читай-Город")
@allure.feature("Карточка книги")
class TestBookPage:

    @allure.story("Открытие карточки книги")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_book_page(self):
        BookPage().open("/product/vojna-i-mir-123456")
        BookPage().should_have_title("Война и мир")
