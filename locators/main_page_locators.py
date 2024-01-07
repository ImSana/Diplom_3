from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    CREATE_BURGER_HEAD = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    ORDER_ID_DEFAULT = (By.XPATH, "//h2[text()='9999']")
    MODAL_CLOSE = (By.XPATH, "//div[contains(@class, 'container')]/button[contains(@class, 'close')]")
    CONTAINS_COUNTER = (By.XPATH, "//a[contains(@href, 'aaa72')]//p[contains(@class, 'counter')]")
    ORDER_STATUS = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_ID = (By.XPATH, "//div[contains(@class, 'container')]//h2")
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor')]")
    PLACE_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
