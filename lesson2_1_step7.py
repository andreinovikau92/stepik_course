from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print (x)
    y = calc(x) 
    time.sleep(2)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(2)
    
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