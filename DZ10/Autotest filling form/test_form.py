"""Модуль test_form содержит тесты для проверки формы."""
import pytest
import allure
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from form_page import FormPage


@pytest.fixture(scope="module")
def browser():
    """Фикстура для инициализации и завершения работы браузера.

    Returns:
        Экземпляр WebDriver для управления браузером.
    """
    driver = webdriver.Edge(
        service=Service(
            executable_path='C:/Users/Сергей/Desktop/Edge/msedgedriver.exe')
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка валидации формы")
@allure.description("Тест проверяет корректность заполнения и отправки формы")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_validation(browser):
    """Тест проверяет валидацию формы и подсветку полей."""
    page = FormPage(browser)

    with allure.step("Открытие страницы с формой"):
        page.open()

    with allure.step("Заполнение полей формы"):
        fields_to_fill = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields_to_fill.items():
            page.fill_field(field_name, value)

    with allure.step("Отправка формы"):
        page.submit()

    with allure.step("Проверка подсветки поля Zip code"):
        assert "alert-danger" in page.get_field_alert_class(
            "#zip-code"
        ), "Zip code не красный"

    with allure.step("Проверка успешно заполненных полей"):
        success_fields = [
            ("#first-name", "Иван"),
            ("#last-name", "Петров"),
            ("#address", "Ленина, 55-3"),
            ("#e-mail", "test@skypro.com"),
            ("#phone", "+7985899998787"),
            ("#city", "Москва"),
            ("#country", "Россия"),
            ("#job-position", "QA"),
            ("#company", "SkyPro")
        ]

        for field_id, expected_value in success_fields:
            with allure.step(f"Проверка поля {field_id}"):
                assert "alert-success" in page.get_field_alert_class(
                    field_id
                ), f"Поле {field_id} не зеленое"
                assert expected_value in page.get_field_text(
                    field_id
                ), f"Текст в {field_id} не совпадает"
