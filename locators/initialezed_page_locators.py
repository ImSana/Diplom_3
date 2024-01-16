from selenium.webdriver.common.by import By


class InitializedPageLocators:
    EMAIL_INPUT_FIELD = (By.NAME, "name")
    PASSWORD_INPUT_FIELD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
