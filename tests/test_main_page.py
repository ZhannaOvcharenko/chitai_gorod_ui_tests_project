import allure
from pages.main_page import MainPage


@allure.epic("UI Читай-Город")
@allure.feature("Главная страница")
class TestMainPage:

    @allure.story("Открытие главной страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_main_page_accessible(self, open_main_page):
        open_main_page
