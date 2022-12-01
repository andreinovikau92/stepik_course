from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()