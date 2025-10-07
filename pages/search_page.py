import allure
from selene import browser, be
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException


class SearchPage:

    @allure.step("Поиск книги: {query}")
    def search_book(self, query: str):
        try:
            search_input = browser.element('input[placeholder="Что будем искать?"]')
            search_input.should(be.visible).clear().type(query).press_enter()
            return self
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            raise AssertionError(
                "Поле поиска не найдено — проверьте селектор в SearchPage.search_book()"
            )

    @allure.step("Проверить, что в результатах есть книга: {book_name}")
    def should_contain_book(self, book_name: str):
        browser.element(f'a:contains("{book_name}")').should(be.visible)
        return self
