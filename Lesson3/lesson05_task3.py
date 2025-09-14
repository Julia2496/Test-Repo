from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()

    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")

        # Находим поле ввода
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

        # Вводим текст "Sky"
        input_field.send_keys("Sky")

        # Очищаем поле
        input_field.clear()

        # Вводим текст "Pro"
        input_field.send_keys("Pro")

    finally:
        # Закрываем браузер
        driver.quit()


if __name__ == "__main__":
    main()