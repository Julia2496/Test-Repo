from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_add_buttons = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bolt-t-shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        self.driver.find_element(*self.item_add_buttons[item_name]).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()