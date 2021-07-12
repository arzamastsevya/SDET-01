from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPage:

    def __init__(self, browser, base_url):
        self.base_url = base_url
        self.driver = browser

    def goto_site(self):
        return self.driver.get(self.base_url)

    def back_page(self):
        return self.driver.back()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
        f"Can't find element by locator {locator}")

    def find_element_NOT(self, locator, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.presence_of_element_located(locator),
        f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), 
        f"Can't find elements by locators {locator}")

    def close_page(self):
        return self.driver.close()