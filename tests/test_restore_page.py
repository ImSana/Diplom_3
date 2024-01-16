import allure
from pages.restore_page import RestorePage
from urls import URLS


@allure.feature("Проверка функционала в восстановления пароля")
class TestRestorePage:
    @allure.title("Проверка перехода на восстановление пароля по ссылке 'Восстановить пароль'")
    @allure.description("Открываем страницу входа, жмём 'Восстановить пароль', проверяем "
                        "поле 'email' на странице восстановления пароля")
    def test_restore_link_password_click(self, driver):
        login_page = RestorePage(driver, URLS.MAIN_PAGE + URLS.LOGIN_PAGE)
        login_page.open_a_page()
        restore_page = RestorePage(driver, URLS.MAIN_PAGE + URLS.RESTORE_PAGE)
        restore_page.recovery_page_open()
        restore_page.check_email_on_recovery_page()

    @allure.title("Проверка ввода почты и нажатие на кнопку 'Восстановить'")
    @allure.description("Открываем восстановления пароля, вводим email, жмём кнопку 'Восстановить', "
                        "проверяем поле 'Пароль' восстановлении пароля")
    def test_input_email_restore_button_click(self, driver):
        restore_page = RestorePage(driver, URLS.MAIN_PAGE + URLS.RESTORE_PAGE)
        restore_page.open_a_page()
        restore_page.email_field_input()
        restore_page.recover_button_click()
        restore_page.check_password_recovery_button()

    @allure.title("Проверка подсвечивания поля пароль, после нажатия кнопки 'показать/скрыть пароль'")
    @allure.description("Открываем восстановление пароля, ввод email, нажатие кнопки 'Восстановить', "
                        "жмём кнопку 'показать/скрыть пароль', проверяем, что поле стало активно")
    def test_field_active_show_restore_password_click(self, driver):
        restore_page = RestorePage(driver, URLS.MAIN_PAGE + URLS.RESTORE_PAGE)
        restore_page.open_a_page()
        restore_page.email_field_input()
        restore_page.recover_button_click()
        restore_page.show_password_click()
        restore_page.check_field_active()
