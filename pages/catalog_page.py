import allure
from selene import be, browser
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
)


class CatalogPage:

    @allure.step("Открыть каталог")
    def open_catalog(self):
        selectors = [
            'button[aria-label="Каталог товаров"]',
            'button[aria-label*="Каталог"]',
            'button:has-text("Каталог")',
            'button.header__button',
        ]
        for sel in selectors:
            try:
                elem = browser.element(sel)
                elem.should(be.visible).click()
                return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError("Не удалось открыть каталог — обновите селекторы в CatalogPage.open_catalog()")

    @allure.step("Открыть раздел 'Книги'")
    def open_books(self):
        self.open_catalog()
        browser.element('a[href*="/catalog/books"]').should(be.visible).click()
        return self

    @allure.step("Открыть раздел 'Игры и игрушки'")
    def open_games(self):
        self.open_catalog()
        browser.element('a[href*="/catalog/games"]').should(be.visible).click()
        return self
