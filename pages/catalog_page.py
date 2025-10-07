import allure
from selene import browser, be, have
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selene.core.exceptions import TimeoutException


class CatalogPage:

    @allure.step("Открыть каталог")
    def open_catalog(self):
        selectors = [
            'button[class*="catalog"]',
            'button[data-testid*="catalog"]',
            'button[aria-label*="Каталог"]',
            'button[class*="catalog-btn"]',
            'button:has-text("Каталог")'
        ]
        for sel in selectors:
            try:
                elem = browser.element(sel)
                if elem.matching(be.visible):
                    elem.click()
                    return self
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                continue

        raise AssertionError("Не удалось открыть каталог — обновите селекторы в pages/catalog_page.py")

    @allure.step("Открыть раздел 'Книги'")
    def open_books(self):
        self.open_catalog()
        browser.all('span.categories-menu-adaptive-list__category-name, a.catalog-link__title') \
            .filtered_by(have.exact_text('Книги')).first.should(be.visible).click()
        browser.element('h1').should(have.text('Книги'))
        return self

    @allure.step("Открыть раздел 'Игры и игрушки'")
    def open_games(self):
        self.open_catalog()
        browser.all('span.categories-menu-adaptive-list__category-name, a.catalog-link__title') \
            .filtered_by(have.exact_text('Игры и игрушки')).first.should(be.visible).click()
        browser.element('h1').should(have.text('Игры и игрушки'))
        return self
