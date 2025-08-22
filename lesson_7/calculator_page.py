from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_locators = {
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "=": (By.XPATH, "//span[text()='=']")
        }

    def set_delay(self, seconds):
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(str(seconds))

    def click_button(self, button):
        self.driver.find_element(*self.button_locators[button]).click()

    def get_result_text(self):
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )