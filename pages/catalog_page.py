from selene import browser, be, have


class CatalogPage:

    def open_books(self):
        books_btn = browser.all("div.chg-app-button__content").filtered_by(have.exact_text("Книги")).first
        books_btn.should(be.visible).click()
        return self

    def open_games(self):
        games_btn = browser.all("div.chg-app-button__content").filtered_by(have.exact_text("Игры и игрушки")).first
        games_btn.should(be.visible).click()
        return self
