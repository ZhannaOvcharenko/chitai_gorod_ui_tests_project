from selene import have
from selene.support.shared import browser


class BookPage:

    def open(self, book_url: str):
        browser.open(book_url)
        return self

    def should_have_title(self, title: str):
        browser.element("h1").should(have.text(title))
        return self

    def add_to_cart(self):
        browser.element("[data-testid='button-cart']").click()
        return self
