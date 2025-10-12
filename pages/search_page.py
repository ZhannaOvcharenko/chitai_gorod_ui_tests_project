from selene import browser, be, have


class SearchPage:
    def search_book(self, query: str):
        search_input = browser.element('[data-testid="header-search-input"]')
        search_input.should(be.visible).clear().type(query).press_enter()
        return self

    def should_contain_book(self, title: str):  # noqa: R0201
        browser.all('[data-testid="product-card"]').element_by(have.text(title)).should(be.visible)
