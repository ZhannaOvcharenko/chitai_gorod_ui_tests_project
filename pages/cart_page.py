from selene import browser, be


class CartPage:
    def open(self):
        browser.open("https://www.chitai-gorod.ru/cart")
        return self

    def remove_book(self):
        browser.element("button.cart-item__delete-button").should(be.visible).click()
        return self

    def should_be_empty(self):
        browser.element("div.cart-empty").should(be.visible)
        return self
