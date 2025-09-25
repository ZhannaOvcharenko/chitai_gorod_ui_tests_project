from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.close_button_locator = (By.CLASS_NAME, "popmechanic-close")
        self.cookie_button_locator = (By.CLASS_NAME, "cookie-notice__button")

    def close_pop_up(self):
        try:
            close_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.close_button_locator)
            )
            close_button.click()
            print("Всплывающее окно закрыто.")
        except Exception as e:
            print(f"Всплывающее окно не найдено или не было закрыто: {e}")

    def is_pop_up_closed(self):
        try:
            # Проверяем, что всплывающее окно больше не видно
            WebDriverWait(self.browser, 10).until_not(
                EC.visibility_of_element_located(self.close_button_locator)
            )
            return True
        except Exception:
            return False

    def close_cookie_notice(self):
        try:
            cookie_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.cookie_button_locator)
            )
            cookie_button.click()
            print("Уведомление о куки закрыто.")
        except Exception as e:
            print(f"Уведомление о куки не найдено или не было закрыто: {e}")

    def is_cookie_notice_closed(self):
        try:
            # Проверяем, что уведомление о куки больше не видно
            WebDriverWait(self.browser, 10).until_not(
                EC.visibility_of_element_located(self.cookie_button_locator)
            )
            return True
        except Exception:
            return False
