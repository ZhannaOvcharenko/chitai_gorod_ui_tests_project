from selene import browser, be


class MainPage:

    def open_main_page(self):
        browser.open("https://www.chitai-gorod.ru/")
        return self

    def accept_cookies_if_present(self):
        cookie_btn = browser.element('[data-testid="accept-cookies"]')
        if cookie_btn.matching(be.visible):
            cookie_btn.click()
        return self