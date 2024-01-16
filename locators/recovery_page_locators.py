from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVERY_PASSWORD_BUTTON = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name='name']")
    SHOW_HIDDEN_BUTTON = (By.XPATH, "//div[contains(@class, 'action')]")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div")
    PASSWORD_RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


