from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

# Открывает страницу калькулятора
    def open(self):
        self.driver.get(self.url)

# Устанавливает задержку вычислений (в секундах)
    def set_delay(self, seconds: int):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

# Нажимает кнопку калькулятора
    def click_button(self, button_text: str):
        button_mapping = {
            "7": ".keys .btn-outline-primary:nth-child(1)",
            "+": ".keys .btn-outline-success:nth-child(4)",
            "8": ".keys .btn-outline-primary:nth-child(2)",
            "=": ".keys .btn-outline-warning"
        }
        self.driver.find_element(
            By.CSS_SELECTOR, button_mapping[button_text]).click()

# Ожидает появления результата на экране
    def wait_for_result(self, timeout: int, expected_result: str):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_result)
        )

# Возвращает текущий результат с экрана калькулятора
    def get_result(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
