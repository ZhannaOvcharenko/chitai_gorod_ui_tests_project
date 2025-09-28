import allure
from pages.main_page import MainPage


@allure.epic("UI Читай-Город")
@allure.feature("Поиск")
class TestSearch:

    @allure.story("Поиск существующей книги")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_book(self, open_main_page):
        open_main_page.search("Война и мир").should_see_results("Война и мир")
