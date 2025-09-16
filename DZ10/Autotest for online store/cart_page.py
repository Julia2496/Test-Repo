"""Модуль cart_page.py содержит класс для работы со страницей корзины."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для взаимодействия со страницей корзины интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация класса CartPage.

        Args:
            driver: WebDriver -
            экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver

    def proceed_to_checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout' для перехода к оформлению заказа.

        Returns:
            None
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
