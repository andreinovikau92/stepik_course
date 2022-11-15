from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input = browser.find_elements(By.TAG_NAME, "input")
    for element in input:
        element.send_keys("Andrei")
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    
finally:
    time.sleep(3)
    browser.quit()    
    