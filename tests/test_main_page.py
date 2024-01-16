import allure
from pages.main_page import MainPage
from urls import URLS
from locators.main_page_locators import MainPageLocators
from pages.feed_order_page import FeedOrderPage


@allure.feature("Проверка функционала главной страницы сайта")
class TestMainPage:
    @allure.title("Проверка перехода по кнопке 'Конструктор'")
    @allure.description("Авторизация, переходим в ленту заказов, жмём кнопку 'Конструктор', "
                        "проверяем текст 'Собери бургер' на главной странице сайта")
    def test_click_constructor_button(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        main_page.check_text_create_burger()

    @allure.title("Проверка перехода в ленту заказов по кнопке 'Лента заказов'")
    @allure.description("Авторизация, жмём кнопку 'Лента заказов', проверяем текст 'Лента заказов' на странице")
    def test_feed_button_click_orders(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_order_feed_button()
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.check_text_order_on_feed_page()

    @allure.title("Проверка всплывающего окна по клику ингредиент")
    @allure.description("Авторизация, жмём на ингредиент, проверяем текст 'Детали ингредиента' в открывшейся карточке")
    def test_ingredient_card_open(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_ingredient_button()
        main_page.check_open_ingredient_card()

    @allure.title("Проверка закрытия окна деталей ингредиентов")
    @allure.description("Авторизация, жмём на закрытие окна, проверяем отсутствие текста 'Детали ингредиента'")
    def test_ingredient_card_close(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_ingredient_button()
        main_page.close_ingredient_card_button()
        main_page.check_closed_ingredient_card_()

    @allure.title("Проверка счетчика ингредиента при добавлении ингредиента в заказ")
    @allure.description("Авторизация, добавляем ингредиент, проверяем увеличение счетчика")
    def test_counter_increase_ingredient(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.add_ingredient_order(MainPageLocators.INGREDIENT_SAUCE)
        main_page.check_counter_number_ingredient()

    @allure.title("Проверка оформления заказа для авторизованного пользователя")
    @allure.description("Авторизация, добавляем ингредиент, жмём 'оформить заказ', 'Ваш заказ начали готовить'")
    def test_create_button_click(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.add_ingredient_order(MainPageLocators.INGREDIENT_BUN)
        main_page.click_create_order_button()
        main_page.check_status_order()

