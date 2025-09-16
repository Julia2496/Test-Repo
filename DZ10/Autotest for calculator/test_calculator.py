"""Тесты функциональности медленного калькулятора."""

import pytest
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для инициализации и передачи экземпляра WebDriver."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options)
    yield driver
    driver.quit()


@allure.title("Тестирование функциональности медленного калькулятора")
@allure.description("Проверка корректной работы калькулятора с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(browser):
    """Тестирует работу калькулятора с задержкой."""
    calculator = CalculatorPage(browser)

    with allure.step("Открытие страницы калькулятора"):
        calculator.open()

    with allure.step("Установка задержки вычислений в 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Выполнение вычисления: 7 + 8 ="):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидание и проверка результата"):
        calculator.wait_for_result(46, "15")
        with allure.step("Проверка, что результат равен 15"):
            assert "15" in calculator.get_result(), (
                f"Ожидался результат 15, получено: {calculator.get_result()}")
            print("Тест пройден! Результат 15 отобразился корректно")
