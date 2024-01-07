import allure
from pages.main_page import MainPage
from urls import URLS
from pages.feed_order_page import FeedOrderPage
from pages.profile_page import ProfilePage


@allure.feature("Проверка ленты заказов")
class TestFeedOrderPage:
    @allure.title("Проверка открытия деталей заказа при клике на заказ ")
    @allure.description("Аутентификация в системе, открытие ленты заказов, клик по заказу, проверка "
                        "текста 'Состав'в карточке заказа")
    def test_order_card_open(self, driver, login_to_user_system):
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_a_page()
        feed_page.click_first_order_card()
        feed_page.order_card_opened()

    @allure.title("Проверка наличия заказов в истории 'Ленты заказов'")
    @allure.description("Авторизация в системе, создаем заказ, переходим в ЛК, клик по 'Истории заказов',"
                        " проверяем созданный ID заказа в истории, переходим в ленту проверяем наличие ID заказа")
    def test_check_history_orders_feed_in_orders(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        order_id = main_page.create_new_order()
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver, URLS.MAIN_PAGE + URLS.PROFILE_PAGE)
        profile_page.click_order_history_link()
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.order_id_in_history_id(order_id)
        main_page.click_order_feed_button()
        feed_page.order_id_in_order_feed(order_id)

    @allure.title("Проверка счетчика создания заказа 'Выполнено за всё время'")
    @allure.description("Авторизация в системе, открытие 'Ленты заказов', сохраняем счетчик заказов за всё время,"
                        "переход в конструктор, создание заказа, открытие 'Ленты заказов', сравниваем счетчик")
    def test_increase_all_time_counter_feed_page(self, driver, login_to_user_system):
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_a_page()
        counter_before = feed_page.check_number_all_time_orders()
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.click_constructor_button()
        main_page.create_new_order()
        feed_page.open_a_page()
        counter_after = feed_page.check_number_all_time_orders()
        feed_page.check_increase_counter(counter_before, counter_after)

    @allure.title("Проверка счетчика 'Выполнено за сегодня' после заказа")
    @allure.description("Авторизация, открываем 'Ленту заказов', сохраняем счетчик заказов за сегодня,"
                        "переход в конструктор, создаем заказ, открываем 'Ленту заказов', сравниваем счетчик")
    def test_increase_today_counter_feed_page(self, driver, login_to_user_system):
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_a_page()
        counter_before = feed_page.check_number_of_today()
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        main_page.create_new_order()
        feed_page.open_a_page()
        counter_after = feed_page.check_number_of_today()
        feed_page.check_increase_counter(counter_before, counter_after)

    @allure.title("Проверка заказа 'В работе' после создания заказа")
    @allure.description("Авторизация, создаем заказ, переход в 'Ленту заказов', смотрим наличие ID созданного заказа"
                        "'В работе'")
    def test_orders_in_work_feed_page(self, driver, login_to_user_system):
        main_page = MainPage(driver, URLS.MAIN_PAGE)
        order_id = main_page.create_new_order()
        feed_page = FeedOrderPage(driver, URLS.MAIN_PAGE + URLS.FEED_PAGE)
        feed_page.open_a_page()
        feed_page.check_id_of_orders_in_work(order_id)
