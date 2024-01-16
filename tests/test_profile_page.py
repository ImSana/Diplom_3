import allure
from pages.profile_page import ProfilePage
from urls import URLS
from pages.main_page import MainPage


@allure.feature("Проверка функционала личного кабинета")
class TestProfilePage:
    @allure.title("Проверка перехода по клику на кнопку 'Личный кабинет'")
    @allure.description("Авторизация, открываем главную страницу сайта, жмём кнопку 'Личный кабинет', "
                        "проверяем кнопку 'Сохранить' в личном кабинета")
    def test_profile_button_click(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.check_save_button_account_page()

    @allure.title("Проверка перехода в 'Историю заказов' по клику в 'Историю заказов'")
    @allure.description("Авторизация, открываем профиль пользователя, жмём 'История заказов', "
                        "проверяем, что 'История заказов' активна")
    def test_history_link_orders_click(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_order_history_link()
        profile_page.check_history_button_active()

    @allure.title("Проверка выхода из ЛК")
    @allure.description("Авторизация, открываем профиль пользователя, жмём на 'Выход', проверяем кнопку 'Войти'")
    def test_profile_exit(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_exit_account_link()
        profile_page.check_login_button_exit_account()
