import allure
import pytest
from selene import browser
from pages.search_page import SearchPage


@pytest.mark.usefixtures("open_main_page")
@allure.epic("UI Tests")
@allure.feature("Поиск товаров")
class TestSearch:

    @allure.story("Поиск книги по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_book(self):
        SearchPage().search_book("Дюна").should_contain_book("Дюна")
        assert "duna" in browser.driver.current_url.lower() or "дюна" in browser.driver.current_url.lower()
