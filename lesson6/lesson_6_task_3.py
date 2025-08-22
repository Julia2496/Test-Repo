from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(
            By.CSS_SELECTOR, "#image-container img")) == 4
    )

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    if len(images) >= 3:
        third_img_src = images[2].get_attribute("src")
        print(third_img_src)
    else:
        print(f"Ошибка: найдено только {len(images)} изображений")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")

finally:
    driver.quit()
