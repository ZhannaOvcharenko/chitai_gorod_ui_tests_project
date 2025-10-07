import allure
from selene import browser, be, have
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selene.core.exceptions import TimeoutException


class SearchPage:

    @allure.step("Поиск книги: {query}")
    def search_book(self, query: str):
        selectors = [
            'input[type="search"]',
            'input[placeholder*="найти"]',
            'input.search-form__input',
            'input[class*="search"]',
            'input[data-testid*="search"]'
        ]
        for sel in selectors:
            try:
                el = browser.element(sel)
                if el.matching(be.visible):
                    el.clear().type(query).press_enter()
                    return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError("Поле поиска не найдено — обновите селектор в pages/search_page.py")

    @allure.step("Проверить, что результаты поиска содержат '{title}'")
    def should_contain_book(self, title: str):
        browser.all('.product-card__title, .product-title, .product-card__name, .product-card__title a') \
            .filtered_by(have.text(title)).first.should(be.visible)
        return self
