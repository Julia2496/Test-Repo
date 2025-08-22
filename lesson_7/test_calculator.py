import pytest
from selenium import webdriver
from .calculator_page import CalculatorPage  # Измененный импорт

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_operations(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = CalculatorPage(browser)
    
    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    calculator.wait_for_result()
    assert calculator.get_result_text() == "15"
    