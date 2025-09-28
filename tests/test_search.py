import allure
from selene import browser, be


@allure.epic("UI Читай-Город")
@allure.feature("Поиск")
class TestSearch:

    @allure.story("Поиск существующей книги")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_book(self):
        browser.open("https://www.chitai-gorod.ru/")
        browser.element("input[type='search']").type("Дюна").press_enter()
        browser.element("div.product-card").should(be.visible)
