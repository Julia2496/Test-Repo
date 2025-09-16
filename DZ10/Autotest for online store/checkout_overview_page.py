"""Модуль содержит класс для работы со страницей подтверждения заказа."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    """Класс для взаимодействия со страницей подтверждения заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация класса CheckoutOverviewPage.

        Args:
            driver: WebDriver -
            экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа из элемента на странице.

        Returns:
            str: Итоговая сумма заказа (например, "$58.29")
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")))
        return total_element.text.split()[-1]
