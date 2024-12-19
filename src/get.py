from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://photon-sol.tinyastro.io/en/discover"

options = webdriver.FirefoxOptions()
options.add_extension("/phantom_app-24.26.0.xpi")  # Add this line to include the extension
browser = webdriver.Remote(
    command_executor=environ["SELENIUM_HOST"] + "/wd/hub", options=options
)

try:
    browser.get(BASE_URL)
    
    # Log into the extension with user/password
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-icon='user-octagon']"))
    )
    browser.find_element(By.CSS_SELECTOR, "div[data-icon='user-octagon']").click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("your_password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Log into the website with the given extension/wallet
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-id='connect-wallet']"))
    )
    browser.find_element(By.CSS_SELECTOR, "button[data-id='connect-wallet']").click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-id='phantom-wallet']"))
    )
    browser.find_element(By.CSS_SELECTOR, "button[data-id='phantom-wallet']").click()
    
finally:
    browser.quit()
