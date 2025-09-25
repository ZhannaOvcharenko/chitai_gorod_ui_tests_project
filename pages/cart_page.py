from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.cart_icon_locator = (
            By.XPATH, "//span[contains(@class, 'sticky-header__controls-title') and text()='Корзина']")
        self.cart_content_locator = (By.CLASS_NAME, "cart-content")
        self.clear_cart_button_locator = (By.CLASS_NAME, "delete-many")
        self.clear_cart_text_locator = (By.XPATH, "//span[text()='Очистить корзину']")
        self.cart_cleared_message_locator = (
            By.CLASS_NAME, "cart-multiple-delete__title")  # Локатор для сообщения "Корзина очищена"

    def go_to_cart(self):
        try:
            cart_icon = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.cart_icon_locator)
            )
            cart_icon.click()
            print("Переход в корзину выполнен.")
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.cart_content_locator)
            )
        except Exception as e:
            print(f"Не удалось найти иконку корзины для перехода: {e}")

    def clear_cart(self):
        try:
            # Убедитесь, что корзина не пуста перед очисткой
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.cart_content_locator)
            )

            # Пытаемся кликнуть по тексту "Очистить корзину"
            try:
                clear_cart_text = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(self.clear_cart_text_locator)
                )
                clear_cart_text.click()
                print("Клик по тексту 'Очистить корзину' выполнен.")
            except Exception:
                # Если текст не кликабельный, кликаем по самой иконке
                clear_cart_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(self.clear_cart_button_locator)
                )
                clear_cart_button.click()
                print("Клик по иконке 'Очистить корзину' выполнен.")

            # Ожидание появления сообщения "Корзина очищена"
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.cart_cleared_message_locator)
            )
            print("Корзина успешно очищена.")
        except Exception as e:
            print(f"Не удалось найти кнопку 'Очистить корзину' или произошла ошибка: {e}")

    def is_cart_empty(self):
        try:
            # Проверяем наличие сообщения "Корзина очищена"
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.cart_cleared_message_locator)
            )
            print("Сообщение 'Корзина очищена' найдено.")
            return True
        except Exception:
            print("Сообщение 'Корзина очищена' не найдено.")
            return False
