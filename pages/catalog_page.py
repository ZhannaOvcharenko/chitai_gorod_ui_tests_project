from selene import browser, be, have


class CatalogPage:

    def open_catalog(self):
        browser.element('button.catalog-btn.header-sticky__catalog-menu').should(be.visible).click()
        return self

    def open_books(self):
        self.open_catalog()
        browser.all('span.categories-menu-adaptive-list__category-name').filtered_by(
            have.exact_text('Книги')).first.should(be.visible).click()
        return self

    def open_games(self):
        self.open_catalog()
        browser.all('span.categories-menu-adaptive-list__category-name').filtered_by(
            have.exact_text('Игры и игрушки')).first.should(be.visible).click()
        return self
