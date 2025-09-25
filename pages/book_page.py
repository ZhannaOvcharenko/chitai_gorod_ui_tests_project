from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookPage:
    def __init__(self, browser):
        self.browser = browser
        self.book_element_locator = (By.CLASS_NAME, "product-picture__img")
        self.book_detail_locator = (By.CLASS_NAME, "product-detail")
        self.buy_button_locator = (
            By.XPATH,
            "//button[contains(@class, 'product-offer-button') and contains(@class, 'chg-app-button--primary')]")
        self.confirmation_locator = (By.CLASS_NAME, "added-to-cart-confirmation")

    def open_book_page(self):
        try:
            book_element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.book_element_locator)
            )
            book_element.click()
            print("Переход на страницу информации о книге выполнен.")
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.book_detail_locator)
            )
        except Exception as e:
            print(f"Не удалось найти элемент книги для перехода на страницу информации: {e}")

    def add_book_to_cart(self):
        try:
            buy_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.buy_button_locator)
            )
            buy_button.click()
            print("Кнопка 'Купить' нажата, книга добавлена в корзину.")
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.confirmation_locator)
            )
        except Exception as e:
            print(f"Не удалось найти кнопку 'Купить' на странице книги: {e}")
