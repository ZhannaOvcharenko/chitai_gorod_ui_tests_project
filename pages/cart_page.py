from selene import browser


class CartPage:

    def open(self):
        """Открывает страницу корзины"""
        browser.open("/cart")
        return self

    def should_contain_book(self, book_title: str):
        """Проверяет, что корзина содержит книгу"""
        browser.element(".cart-item__title").should_have_text(book_title)
        return self

    def remove_book(self):
        """Удаляет первую книгу из корзины"""
        browser.element("button.cart-item__delete-button").click()
        return self

    def should_be_empty(self):
        """Проверяет, что корзина пуста"""
        browser.element(".cart-empty__title").should_be_visible()
        return self
