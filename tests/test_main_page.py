import allure
import pytest
from selene import browser, be


@pytest.mark.usefixtures("open_main_page")
class TestMainPage:

    @allure.story("Проверка открытия главной страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_main_page(self, open_main_page):
        browser.element('[data-testid="header-logo"]').should(be.visible)
