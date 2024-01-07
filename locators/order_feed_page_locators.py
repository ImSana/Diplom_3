from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    NO_ORDERS_IN_PROGRESS = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")
    ORDERING = (By.XPATH, "//p[text()='Cостав']")
    ORDER_COUNTER_FOR_TODAY = (By.XPATH, "//p[contains(text(), 'сегодня')]/following-sibling::p")
    ORDER_ID = (By.XPATH, "//div[contains(@class,'Box')]/p[contains(@class,'digits')]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'Ready')]/li")
    TOTAL_ORDER_COUNTER = (By.XPATH, "//p[contains(text(), 'время')]/following-sibling::p")
    NEW_ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'Order')]//li[contains(@class, 'list')]")
    TITLE_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")


