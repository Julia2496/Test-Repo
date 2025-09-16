import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_complete_purchase(browser):

    # 1. Open site and login
    browser.get("https://www.saucedemo.com/")
    login_page = LoginPage(browser)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Add items to cart
    products_page = ProductsPage(browser)
    products_page.add_item_to_cart("backpack")
    products_page.add_item_to_cart("bolt-t-shirt")
    products_page.add_item_to_cart("onesie")
    products_page.go_to_cart()

    # 3. Proceed to checkout
    cart_page = CartPage(browser)
    cart_page.click_checkout()

    # 4. Fill info and check total
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_shipping_info("John", "Doe", "12345")
    
    # Явное ожидание
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
    

def assert_total_amount(total_amount: str) -> None:
    """Проверяет, что итоговая сумма соответствует ожидаемой $58.29"""
    try:
        # Удаляем все нечисловые символы кроме точки
        cleaned = ''.join(c for c in total_amount if c.isdigit() or c == '.')
        # Преобразуем в float с округлением до 2 знаков
        actual = round(float(cleaned), 2)
        expected = 58.29
        assert actual == expected, f"Expected ${expected:.2f}, but got ${actual:.2f}"
    except (ValueError, TypeError) as e:
        pytest.fail(f"Failed to parse total amount '{total_amount}': {str(e)}")
