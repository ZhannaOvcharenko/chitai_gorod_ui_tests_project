from selene import browser, be, have


class CatalogPage:
    def open_catalog(self):
        browser.element('[data-testid="header-catalog-button"]').should(be.clickable).click()
        return self

    def open_books(self):
        self.open_catalog()
        browser.element('[href="product/dzheyn-eyr-2544490"]').should(be.clickable).click()
        browser.should(have.url_containing("dzheyn-eyr-2544490")).with_(timeout=5)
        return self

    def open_games(self):
        self.open_catalog()
        browser.element('[href="product/nastolnaya-igra-gemenot-misterium-1006-2578863"]').should(be.clickable).click()
        browser.should(have.url_containing("nastolnaya-igra-gemenot-misterium-1006-2578863")).with_(timeout=5)
        return self
