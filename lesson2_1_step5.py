from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
   
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x) 
     
    time.sleep(2)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input1.send_keys(y)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    time.sleep(2)
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    time.sleep(2)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()
    