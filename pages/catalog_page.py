import allure
from selene import browser, be
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException


class CatalogPage:

    @allure.step("Открыть каталог")
    def open_catalog(self):
        try:
            browser.element('button.catalog-btn.header-sticky__catalog-menu').should(be.visible).click()
            return self
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            raise AssertionError(
                "Не удалось открыть каталог — проверьте селектор кнопки каталога"
            )

    @allure.step("Перейти в раздел 'Книги'")
    def open_books(self):
        self.open_catalog()
        browser.element('a[href*="books"]').should(be.visible).click()
        return self

    @allure.step("Перейти в раздел 'Игры и игрушки'")
    def open_games(self):
        self.open_catalog()
        browser.element('a[href*="games"]').should(be.visible).click()
        return self
