from selene import browser, be


class BookPage:

    def open(self, url: str):
        browser.open(f"https://www.chitai-gorod.ru/{url}")
        return self

    def add_to_cart(self):
        add_button = browser.all("button.chg-app-button--primary").by(be.visible)
        if len(add_button) > 0:
            add_button.first.click()
        return self
