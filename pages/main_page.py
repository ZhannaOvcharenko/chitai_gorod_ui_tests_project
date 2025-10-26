from selene import browser, be


class MainPage:

    def open(self):
        browser.open("/")
        return self

    def accept_cookies_if_present(self):
        cookie_button = browser.all('[data-testid="cookie-accept-button"]').filter(be.visible)
        if cookie_button:
            cookie_button.first.click()
        return self
