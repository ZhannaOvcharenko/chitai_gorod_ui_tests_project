from selene import browser


class BookPage:

    def open(self, book_url: str):
        """Открывает страницу книги по относительному URL"""
        browser.open(f"/{book_url}")
        return self

    def add_to_cart(self):
        """Добавляет книгу в корзину"""
        browser.element("button.chg-app-button--primary").click()
        return self
