import allure
from pages.base_page import BasePage
from locators.initialezed_page_locators import InitializedPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    @allure.step("Заполнение поля 'email'")
    def email_field_input(self, login):
        self.find_the_element_and_send_the_text(InitializedPageLocators.EMAIL_INPUT_FIELD, login)

    @allure.step("Заполнение поля 'пароль'")
    def input_field_password(self, password):
        self.find_the_element_and_send_the_text(InitializedPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step("Нажатие на кнопки 'Войти'")
    def login_button_click(self):
        self.find_element_click(InitializedPageLocators.LOGIN_BUTTON)

    @allure.step("Проверка логина")
    def login_verification(self):
        assert self.element_present(MainPageLocators.PLACE_AN_ORDER), 'Логин в систему не осуществлен'

    @allure.step("Авторизоваться с логином")
    def login(self, login, password):
        self.email_field_input(login)
        self.input_field_password(password)
        self.login_button_click()
        self.login_verification()
