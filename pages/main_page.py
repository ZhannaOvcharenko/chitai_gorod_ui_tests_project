from selene import browser, be


class MainPage:

    def open_main_page(self):
        browser.open("https://www.chitai-gorod.ru/")
        return self

    def accept_cookies_if_present(self):
        cookie_btns = browser.all("[data-testid='accept-cookies']").by(be.visible)
        if len(cookie_btns) > 0:
            cookie_btns.first.click()
        return self
