from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = browser.find_element(By.ID, "num1").text # получаем текст из a и b
    b = browser.find_element(By.ID, "num2").text
    c = str(int(a) +int(b)) # передаём a и b в с, но делаем из них цифры с помощью int
    
    input = browser.find_element(By.TAG_NAME, "select")
    input.send_keys(c)
    input.click()
    time.sleep(2)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()    