import allure
import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("open_main_page")
class TestMainPage:

    @allure.story("Переход в меню Книги")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_books(self):
        MainPage().open_main_page().accept_cookies_if_present()

    @allure.story("Переход в меню Игры и игрушки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_games(self):
        MainPage().open_main_page().accept_cookies_if_present()
