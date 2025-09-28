from selene import browser


class CatalogPage:

    def open_books(self):
        browser.element("div.chg-app-button__content").with_text("Каталог").click()
        browser.element("div.categories-level-menu__item-title").with_text("Книги").click()
        return self

    def open_games(self):
        browser.element("div.chg-app-button__content").with_text("Каталог").click()
        browser.element("div.categories-level-menu__item-title").with_text("Игры и игрушки").click()
        return self
