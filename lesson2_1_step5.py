from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    time.sleep(2)
    
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()    