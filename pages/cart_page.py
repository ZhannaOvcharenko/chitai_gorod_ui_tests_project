from selene import have
from selene.support.shared import browser


class CartPage:

    def open(self):
        browser.open("/cart")
        return self

    def should_contain_book(self, title: str):
        browser.all("[data-testid='cart-item-title']").first.should(have.text(title))
        return self

    def remove_book(self):
        browser.element("[data-testid='cart-item-remove']").click()
        return self

    def should_be_empty(self):
        browser.element("[data-testid='cart-empty-title']").should(have.text("Корзина пуста"))
        return self
