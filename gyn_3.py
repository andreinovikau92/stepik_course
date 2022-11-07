from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://qa.getyournest.com/forgot-password"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.ID, "email")
    input1.send_keys("andreinovikau")
    time.sleep(10)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()
    