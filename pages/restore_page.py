import allure
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators
from creat_user import CreateUser

class RestorePage(BasePage):
    @allure.step("Нажать 'Восстановление пароля'")
    def recovery_page_open(self):
        self.find_element_click(RecoveryPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step("Заполнить поле 'email'")
    def email_field_input(self):
        self.find_the_element_and_send_the_text(RecoveryPageLocators.EMAIL_INPUT_FIELD, CreateUser.creat_user()['email'])

    @allure.step("Нажать кнопку 'Восстановить'")
    def recover_button_click(self):
        self.find_element_click(RecoveryPageLocators.PASSWORD_RECOVER_BUTTON)

    @allure.step("Нажать кнопку 'Показать/скрыть пароль'")
    def show_password_click(self):
        self.find_element_click(RecoveryPageLocators.SHOW_HIDDEN_BUTTON)

    @allure.step("Проверка активного поля пароля")
    def check_field_active(self):
        password_field = self.find_element(RecoveryPageLocators.PASSWORD_FIELD)
        assert 'active' in password_field.get_attribute('class'), f"Поле 'Пароль' не активно"

    @allure.step("Проверка перехода на восстановление пароля по наличию поля 'email' на странице")
    def check_email_on_recovery_page(self):
        assert self.element_displayed_on_the_page(RecoveryPageLocators.EMAIL_INPUT_FIELD), (f"Поле email на странице "
                                                                                    f"восстановления пароля не "
                                                                                    f"найдено.")

    @allure.step("Проверка перехода по кнопке 'Восстановить' по наличию поля 'Пароль'")
    def check_password_recovery_button(self):
        assert self.element_displayed_on_the_page(RecoveryPageLocators.PASSWORD_FIELD), ("Поле 'Пароль' на странице "
                                                                                       "восстановления пароля не "
                                                                                       "найдено.")
