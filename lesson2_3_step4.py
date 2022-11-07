from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    time.sleep(2)
    
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button1.click()
    
finally:
    time.sleep(5)
    browser.quit()
    