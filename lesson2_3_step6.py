from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    browser.switch_to.window(first_window)
    
finally:
    time.sleep(8)
    browser.quit()
        