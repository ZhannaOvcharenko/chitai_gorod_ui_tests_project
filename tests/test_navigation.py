import allure
import pytest
from pages.catalog_page import CatalogPage


@pytest.mark.usefixtures("open_main_page")
class TestNavigation:

    @allure.story("Переход в раздел 'Книги'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_books(self):
        CatalogPage().open_books()
        from selene import browser, have
        browser.element("h1").should(have.text("Книги"))

    @allure.story("Переход в раздел 'Игры и игрушки'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_games(self):
        CatalogPage().open_games()
        from selene import browser, have
        browser.element("h1").should(have.text("Игры и игрушки"))