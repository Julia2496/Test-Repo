"""Модуль содержит класс для работы со страницей оформления заказа."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для взаимодействия со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация класса CheckoutPage.

        Args:
            driver: WebDriver -
            экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver

    def fill_shipping_info(self, first_name: str,
                           last_name: str,
                           zip_code: str) -> None:
        """
        Заполняет форму доставки информацией о покупателе.

        Args:
            first_name: str - имя покупателя
            last_name: str - фамилия покупателя
            zip_code: str - почтовый индекс

        Returns:
            None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
