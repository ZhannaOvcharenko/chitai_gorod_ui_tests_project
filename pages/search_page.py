from selene import browser, be, have


class SearchPage:

    def search_book(self, query: str):
        search_input = browser.element('input.search-form__input[placeholder="Хочу найти"]').should(be.visible)
        search_input.clear().type(query).press_enter()
        return self

    def should_contain_book(self, title: str):
        browser.all('.product-card__title, .product-title, .product-card__name') \
            .filtered_by(have.text(title)).first.should(be.visible)
        return self
