from selene import browser


class MainPage:

    def open_main_page(self):
        """Открывает главную страницу сайта"""
        browser.open("/")
        return self

    def accept_cookies_if_present(self):
        """Принимает куки, если есть баннер"""
        cookie_btn = browser.element("[data-testid='accept-cookies']")
        if cookie_btn.is_displayed():
            cookie_btn.click()
        return self
