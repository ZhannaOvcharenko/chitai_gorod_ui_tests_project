import allure
from selene import be, browser
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
)


class SearchPage:

    @allure.step("Поиск книги: {query}")
    def search_book(self, query: str):
        selectors = [
            'input.search-form__input--search',
            'input[placeholder*="Что будем искать?"]',
            'input[name="search"]',
        ]
        for sel in selectors:
            try:
                el = browser.element(sel)
                if el.matching(be.visible):
                    el.clear().type(query).press_enter()
                    return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError(
            "Поле поиска не найдено — проверьте селекторы в SearchPage.search_book()"
        )

    @allure.step("Проверка, что в результатах поиска есть книга '{expected_title}'")
    def should_contain_book(self, expected_title: str):
        browser.element(f'[title*="{expected_title}"], :has-text("{expected_title}")').should(be.visible)
        return self
