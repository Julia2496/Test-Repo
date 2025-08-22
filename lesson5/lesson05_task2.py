from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def click_blue_button():
    chrome_options = Options()
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        blue_button.click()
    finally:
        driver.quit()


if __name__ == "__main__":
    click_blue_button()