import allure
import pytest
from pages.catalog_page import CatalogPage


@allure.epic("UI Tests")
@allure.feature("Навигация по сайту")
@pytest.mark.ui
@pytest.mark.usefixtures("open_main_page")
class TestNavigation:

    @allure.story("Переход в раздел 'Книги'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_books(self):
        CatalogPage().open_books()

    @allure.story("Переход в раздел 'Игры и игрушки'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_games(self):
        CatalogPage().open_games()
