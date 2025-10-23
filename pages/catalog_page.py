from selene import browser, be, have


class CatalogPage:
    def open_catalog(self):  # noqa: R0201
        browser.element('[data-testid="header-catalog-button"]').should(be.clickable).click()

    def open_books(self):
        self.open_catalog()
        browser.element('[href="/catalog/books-18000"]').should(be.clickable).click()
        browser.should(have.url_containing("/catalog/books-18000"))

    def open_games(self):
        self.open_catalog()
        browser.element('[href="/catalog/igrushki-i-igry-2824"]').should(be.clickable).click()
        browser.should(have.url_containing("/catalog/igrushki-i-igry-2824"))
