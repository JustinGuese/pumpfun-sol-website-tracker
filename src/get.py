from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://photon-sol.tinyastro.io/en/discover"

options = webdriver.FirefoxOptions()
options.
options.add_argument(
    "--load-extension=/phantom_app-24.26.0.xpi"
)  # Add this line to include the extension
browser = webdriver.Remote(
    command_executor=environ["SELENIUM_HOST"] + "/wd/hub", options=options
)
try:
    browser.get(BASE_URL)
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[data-icon='user-octagon']")
        )
    )
finally:
    browser.quit()
