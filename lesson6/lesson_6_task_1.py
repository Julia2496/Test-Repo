from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.ID, "ajaxButton").click()

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#content p"),
            "Data loaded with AJAX get request."
        )
    )

    result = driver.find_element(By.CSS_SELECTOR, "#content p").text
    print(result)

finally:
    driver.quit()
