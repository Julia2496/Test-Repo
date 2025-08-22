from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    try:
        # Переход на страницу логина
        driver.get("http://the-internet.herokuapp.com/login")

        # Ввод имени пользователя
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")

        # Ввод пароля
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        # Нажатие кнопки Login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Ожидание появления зеленой плашки и получение текста
        flash_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        print(flash_message.text.strip())

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    main()

