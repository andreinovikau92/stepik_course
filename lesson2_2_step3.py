import select
from xml.etree.ElementPath import find
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    c = str(int(a) +int(b))
    
    input = browser.find_element(By.TAG_NAME, "select")
    input.send_keys(c)
    input.click()
    time.sleep(2)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
        