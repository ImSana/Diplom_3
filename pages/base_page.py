from selenium.webdriver import Remote as RemoteWebDriver
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver: RemoteWebDriver, url):
        self.driver = driver
        self.url = url

    def open_a_page(self):
        self.driver.get(self.url)

    def element_present(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def element_clickable(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def find_element(self, locator):
        self.element_present(locator)
        return self.driver.find_element(*locator)

    def find_element_click(self, locator):
        self.element_clickable(locator)
        self.driver.find_element(*locator).click()

    def find_the_element_and_send_the_text(self, locator, text):
        self.element_present(locator)
        self.driver.find_element(*locator).send_keys(text)

    def find_elements(self, locator):
        self.element_present(locator)
        return self.driver.find_elements(*locator)

    def element_no_more_located(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element(locator))

    def element_displayed_on_the_page(self, locator):
        return self.find_element(locator).is_displayed()
