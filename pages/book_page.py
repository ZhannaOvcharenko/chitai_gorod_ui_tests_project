from selene import browser, be


class BookPage:
    def open(self, url):
        browser.open(f"https://www.chitai-gorod.ru/{url}")
        return self

    def add_to_cart(self):
        add_button = browser.all("button.chg-app-button--primary").filter(be.visible)
        if add_button.count() > 0:
            add_button.first.click()
        return self
