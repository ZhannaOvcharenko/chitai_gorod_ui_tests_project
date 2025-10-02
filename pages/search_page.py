from selene import browser, be, have


class SearchPage:

    def search_book(self, query: str):
        search_input = browser.element("input[name='q']").should(be.visible)
        search_input.clear().type(query).press_enter()
        return self

    def should_contain_book(self, title: str):
        browser.all(".product-card__title").filtered_by(have.exact_text(title)).first.should(be.visible)
        return self
