"""Модуль login_page.py содержит класс для работы со страницей авторизации."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для взаимодействия со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация класса LoginPage.

        Args:
            driver: WebDriver -
            экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """
        Открывает страницу авторизации в браузере.

        Returns:
            None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.

        Args:
            username: str - имя пользователя
            password: str - пароль пользователя

        Returns:
            None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
