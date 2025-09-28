from selene import browser, have


class CatalogPage:
    def open_books(self):
        browser.all("div.chg-app-button__content") \
            .element_by(have.exact_text("Каталог")) \
            .click()
        return self

    def open_games(self):
        browser.all("div.chg-app-button__content") \
            .element_by(have.exact_text("Каталог")) \
            .click()
        return self
