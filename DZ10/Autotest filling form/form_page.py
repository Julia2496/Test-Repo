"""Модуль form_page содержит класс для работы со страницей формы."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """Класс для взаимодействия со страницей формы.

    Позволяет открывать страницу, заполнять поля формы,
    отправлять форму и проверять результаты.
    """

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует экземпляр класса FormPage.

        Args:
            driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def open(self) -> None:
        """Открывает страницу с формой в браузере."""
        self.driver.get(self.url)

    def fill_field(self, field_name: str, value: str) -> None:
        """Заполняет указанное поле формы заданным значением.

        Args:
            field_name: Имя поля для заполнения.
            value: Значение, которое нужно ввести в поле.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, f'input[name="{field_name}"]'
        ).send_keys(value)

    def submit(self) -> None:
        """Отправляет форму на сервер."""
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

    def get_field_alert_class(self, field_id: str) -> str:
        """Получает класс CSS для указанного поля.

        Args:
            field_id: CSS-селектор поля.

        Returns:
            Строка с классами CSS элемента.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, field_id)
        return element.get_attribute("class")

    def get_field_text(self, field_id: str) -> str:
        """Получает текст из указанного поля.

        Args:
            field_id: CSS-селектор поля.

        Returns:
            Текст содержимого поля.
        """
        return self.driver.find_element(By.CSS_SELECTOR, field_id).text
