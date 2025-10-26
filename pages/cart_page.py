from selene import browser, be


class CartPage:

    def open(self):
        browser.open("https://www.chitai-gorod.ru/cart")
        return self

    @staticmethod
    def has_books():
        books = browser.all(".cart-item").filter(be.visible)
        return len(books) > 0

    def remove_all_books(self):
        remove_buttons = browser.all("button.remove-item").filter(be.visible)
        for btn in remove_buttons:
            btn.click()
        return self
