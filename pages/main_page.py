import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    @allure.step("Нажать кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.find_element_click(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.find_element_click(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.element_present(MainPageLocators.ORDER_FEED_TAB)
        self.find_element(MainPageLocators.ORDER_FEED_TAB).click()

    @allure.step("Нажать ингредиент")
    def click_ingredient_button(self):
        self.find_element_click(MainPageLocators.INGREDIENT_SAUCE)

    @allure.step("Нажать на закрытие карточки ингредиента")
    def close_ingredient_card_button(self):
        self.find_element_click(MainPageLocators.MODAL_CLOSE)

    @allure.step("Выбрать ингредиент")
    def choose_an_ingredient(self, ingredient_locator):
        return self.find_element(ingredient_locator)

    @allure.step("Выбрать конструктор заказа ингредиента")
    def choose_field_ingredients(self):
        return self.find_element(MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Добавить ингредиент в конструктор заказа")
    def add_ingredient_order(self, ingredient_locator):
        ingredient = self.choose_an_ingredient(ingredient_locator)
        field = self.choose_field_ingredients()
        action = ActionChains(self.driver)
        action.drag_and_drop(ingredient, field).perform()

    @allure.step("Нажать кнопку создания заказа")
    def click_create_order_button(self):
        self.find_element_click(MainPageLocators.PLACE_AN_ORDER)

    @allure.step("Получить ID заказа")
    def get_order_id(self):
        self.element_no_more_located(MainPageLocators.ORDER_ID_DEFAULT)
        return self.find_element(MainPageLocators.ORDER_ID).text

    @allure.step("Закрыть данные заказа")
    def close_order_card(self):
        self.find_element_click(MainPageLocators.MODAL_CLOSE)

    @allure.step("Создать новый заказ")
    def create_new_order(self):
        self.open_a_page()
        self.add_ingredient_order(MainPageLocators.INGREDIENT_BUN)
        self.add_ingredient_order(MainPageLocators.INGREDIENT_SAUCE)
        self.click_create_order_button()
        order_id = self.get_order_id()
        self.close_order_card()
        return int(order_id)

    @allure.step("Проверка перехода на главную страницу по тексту 'Соберите бургер'")
    def check_text_create_burger(self):
        assert self.element_displayed_on_the_page(MainPageLocators.CREATE_BURGER_HEAD), ("Текст 'Соберите бургер' не "
                                                                                        "найден на главной странице "
                                                                                        "сайта")

    @allure.step("Проверка закрытия карточки ингредиента")
    def check_closed_ingredient_card_(self):
        assert self.element_no_more_located(MainPageLocators.INGREDIENT_DETAILS), ("Карточка ингредиента не "
                                                                                      "закрылась, текст 'Детали "
                                                                                      "ингредиента' по прежнему "
                                                                                      "присутствует на странице")

    @allure.step("Проверка открытия карточки ингредиента")
    def check_open_ingredient_card(self):
        assert self.element_displayed_on_the_page(MainPageLocators.INGREDIENT_DETAILS), ("Карточка деталей ингредиента "
                                                                                        "не открылась - текст 'Детали "
                                                                                        "ингредиента' не найден")

    @allure.step("Проверка счетчика ингредиента")
    def check_counter_number_ingredient(self):
        counter_number = self.find_element(MainPageLocators.CONTAINS_COUNTER).text
        assert counter_number == '1', (f"Количество ингредиента не соответствует. Ожидаемое: 1, "
                                       f"фактическое: {counter_number}")

    @allure.step("Проверка создания заказа с текстом 'Ваш заказ начали готовить'")
    def check_status_order(self):
        status = self.find_element(MainPageLocators.ORDER_STATUS).text
        assert status == "Ваш заказ начали готовить", "Заказ не оформлен, текст 'Ваш заказ начали готовить' не найден"
