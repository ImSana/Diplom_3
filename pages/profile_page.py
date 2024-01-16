import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.initialezed_page_locators import InitializedPageLocators


class ProfilePage(BasePage):
    @allure.step("Нажать 'История заказов'")
    def click_order_history_link(self):
        self.find_element_click(AccountPageLocators.ORDER_HISTORY)

    @allure.step("Нажать на 'Выход'")
    def click_exit_account_link(self):
        self.find_element_click(AccountPageLocators.EXIT_BUTTON)

    @allure.step("Проверка выхода из профиля")
    def check_login_button_exit_account(self):
        assert self.element_present(InitializedPageLocators.LOGIN_BUTTON), ("Выход из профиля не осуществлен, кнопка "
                                                                         "'Войти' отсутствует")

    @allure.step("Проверка перехода на страницу профиля по наличию кнопки 'Сохранить'")
    def check_save_button_account_page(self):
        assert self.element_displayed_on_the_page(AccountPageLocators.SAVE_BUTTON), ("Кнопка 'Сохранить' на станице "
                                                                                    "профиля не найдена")

    @allure.step("Проверка переход в историю заказов по активной ссылке")
    def check_history_button_active(self):
        history_link = self.find_element(AccountPageLocators.ORDER_HISTORY)
        assert 'link_active' in history_link.get_attribute('class'), ("Переход на страницу 'История заказов' не "
                                                                      "осуществлен, ссылка 'История заказов'"
                                                                      "не активна")
