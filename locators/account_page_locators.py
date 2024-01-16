from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    HISTORY_BOX = (By.XPATH, "//div[contains(@class, 'OrderHistory')]")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
