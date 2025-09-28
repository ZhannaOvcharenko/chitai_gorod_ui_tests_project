import allure
from pages.main_page import MainPage
from selene import browser


@allure.epic("UI Читай-Город")
@allure.feature("Навигация по меню")
class TestMainPage:

    @allure.story("Переход в меню Книги")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_books(self):
        MainPage().open_main_page().accept_cookies_if_present()
        browser.element("div.categories-level-menu__item-title").should_have_text("Книги").click()

    @allure.story("Переход в меню Игры и игрушки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_games(self):
        MainPage().open_main_page().accept_cookies_if_present()
        browser.element("div.categories-level-menu__item-title").should_have_text("Игры и игрушки").click()
