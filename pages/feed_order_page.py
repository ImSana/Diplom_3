import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class FeedOrderPage(BasePage):
    @allure.step("Получить историю заказов")
    def get_id_history_list(self):
        self.element_present(OrderFeedPageLocators.ORDER_ID)
        return self.find_elements(OrderFeedPageLocators.ORDER_ID)

    @allure.step("Получить список заказов с статусом в работе")
    def get_orders_list_in_work(self):
        self.check_element_gone()
        return self.find_elements(OrderFeedPageLocators.ORDERS_IN_PROGRESS)

    @allure.step("Получить первый заказ в ленте заказов")
    def click_first_order_card(self):
        self.find_element_click(OrderFeedPageLocators.NEW_ORDER_FEED_LIST)

    @allure.step("Проверка ID заказа в истории заказов")
    def order_id_in_history_id(self, order_id):
        orders_list = self.get_id_history_list()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, f"Созданный заказ(ID: {order_id}) отсутствует в истории заказов"

    @allure.step("Проверка ID заказа в ленте заказов")
    def order_id_in_order_feed(self, order_id):
        orders_list = self.get_id_history_list()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, f"Созданный заказ (ID: {order_id}) отсутствует в ленте заказов"

    @allure.step("Проверка заказов за всё время")
    def check_number_all_time_orders(self):
        return int(self.find_element(OrderFeedPageLocators.TOTAL_ORDER_COUNTER).text)

    @allure.step("Проверка заказов за сегодня")
    def check_number_of_today(self):
        return int(self.find_element(OrderFeedPageLocators.ORDER_COUNTER_FOR_TODAY).text)

    @allure.step("Проверка что элемент пропал со страницы")
    def check_element_gone(self):
        self.find_element(OrderFeedPageLocators.NO_ORDERS_IN_PROGRESS)
        self.element_no_more_located(OrderFeedPageLocators.NO_ORDERS_IN_PROGRESS)

    @allure.step("Проверка ID заказа в списке заказов в работе")
    def check_id_of_orders_in_work(self, order_id):
        orders_list = self.get_orders_list_in_work()
        orders_from_list = [int(c.text[1:]) for c in orders_list]
        assert order_id in orders_from_list, "Созданный заказ отсутствует в списке заказов в работе"

    @allure.step("Проверка карточки заказа")
    def order_card_opened(self):
        assert self.find_element(OrderFeedPageLocators.ORDERING).text == 'Cостав', ("Карточка заказа не открылась, текст "
                                                                                 "'Состав' отсутствует")

    @allure.step("Проверка перехода в ленту")
    def check_text_order_on_feed_page(self):
        assert self.element_displayed_on_the_page(OrderFeedPageLocators.TITLE_ORDER_FEED), ("Текст 'Лента заказов' не найден "
                                                                                     "на странице ленты заказов")

    @allure.step("Проверка счетчика заказов")
    def check_increase_counter(self, counter_before, counter_after):
        assert counter_before + 1 == counter_after, (f"Счетчик не увеличился на совершенный заказ. Значение до заказа:"
                                                     f" {counter_before}, значение после заказа: {counter_after}")
