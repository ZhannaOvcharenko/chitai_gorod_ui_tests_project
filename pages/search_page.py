import allure
from selene import be, browser, have
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
)


class SearchPage:

    @allure.step("Поиск книги: {query}")
    def search_book(self, query: str):
        selectors = [
            'input[data-testid="search-input"]',
            'input[name="q"]',
            'input[type="search"]',
        ]
        for sel in selectors:
            try:
                el = browser.element(sel)
                el.should(be.visible).clear().type(query).press_enter()
                return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError("Поле поиска не найдено — обновите селектор в SearchPage.search_book()")

    @allure.step("Проверка, что в результатах поиска есть книга '{expected_title}'")
    def should_contain_book(self, expected_title: str):
        try:
            browser.element(f'a[title*="{expected_title}"]').should(be.visible)
            return self
        except (NoSuchElementException, TimeoutException):
            browser.all('.product-card__name').element_by(have.text(expected_title)).should(be.visible)
            return self
