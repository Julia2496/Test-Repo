"""Модуль inventory_page.py содержит класс для работы со страницей товаров."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Класс для взаимодействия со страницей товаров интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация класса InventoryPage.

        Args:
            driver: WebDriver -
            экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver

    def add_item_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его идентификатору.

        Args:
            item_id: str - идентификатор товара (например,
            "add-to-cart-sauce-labs-backpack")

        Returns:
            None
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"[data-test='{item_id}']")))
        button.click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину, нажимая на иконку корзины.

        Returns:
            None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()
