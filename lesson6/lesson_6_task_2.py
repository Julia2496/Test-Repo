from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://uitestingplayground.com/textinput")

    driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    print(driver.find_element(By.ID, "updatingButton").text)

finally:
    driver.quit()
