from selene import browser, be


class BookPage:

    def open(self, url: str):
        browser.open(f"https://www.chitai-gorod.ru/{url}")
        return self

    def add_to_cart(self):
        add_buttons = browser.all("button.chg-app-button--primary").filter(be.visible)
        if add_buttons:
            add_buttons.first.click()
        return self
