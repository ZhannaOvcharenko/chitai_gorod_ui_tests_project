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
            'button[data-testid*="catalog"]',
            'button[aria-label*="Каталог"]',
            'button[class*="chg-app-button__content"]',
            'button:has-text("Каталог")',
        ]
        for sel in selectors:
            try:
                elem = browser.element(sel)
                if elem.matching(be.visible):
                    elem.click()
                    return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError(" Не удалось открыть каталог — обновите селекторы в CatalogPage.open_catalog()")

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
