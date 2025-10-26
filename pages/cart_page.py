from selene import browser, be

class CartPage:

    def open(self):
        browser.open("https://www.chitai-gorod.ru/cart")
        return self

    @staticmethod
    def has_books():
        books = browser.all(".cart-item")
        return books.with_(timeout=3).exists()

    def remove_all_books(self):
        remove_buttons = browser.all("button.remove-item").filter(be.visible)
        for btn in remove_buttons:
            btn.click()
            browser.sleep(0.5)
        return self