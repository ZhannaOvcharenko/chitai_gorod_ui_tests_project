import allure
from selene.support.shared import browser
from selene import have


@allure.epic("UI Читай-Город")
@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход в раздел 'Книги'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_books(self, open_main_page):
        browser.element("[data-testid='menu-books']").click()
        browser.element("h1").should(have.text("Книги"))

    @allure.story("Переход в раздел 'Игры и игрушки'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_games(self, open_main_page):
        browser.element("[data-testid='menu-games']").click()
        browser.element("h1").should(have.text("Игры и игрушки"))
