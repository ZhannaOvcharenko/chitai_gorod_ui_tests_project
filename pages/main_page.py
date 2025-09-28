from selene import have, be
from selene.support.shared import browser


class MainPage:

    def open(self):
        browser.open("/")
        return self

    def accept_cookies_if_present(self):
        if browser.element("[data-testid='cookie-policy-close']").matching(be.visible):
            browser.element("[data-testid='cookie-policy-close']").click()
        return self

    def search(self, query: str):
        browser.element("[data-testid='search-input']").type(query).press_enter()
        return self

    def should_see_results(self, text: str):
        browser.all("[data-testid='product-card-title']").first.should(have.text(text))
        return self
