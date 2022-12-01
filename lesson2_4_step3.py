from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    
    message = browser.find_element(By.ID, "verify_message")
    
    assert "successful" in message.text
    
finally:
    time.sleep(3)
    browser.quit()
        