import allure
import pytest
from selene import browser

from pages.search_page import SearchPage


@allure.epic("UI Tests")
@allure.feature("Поиск товаров")
@pytest.mark.ui
@pytest.mark.usefixtures("open_main_page")
class TestSearch:

    @allure.story("Поиск книги по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_book(self):
        SearchPage().search_book("Дюна").should_contain_book("Дюна")
        assert "Дюна" in browser.driver.current_url or "dune" in browser.driver.current_url.lower()
