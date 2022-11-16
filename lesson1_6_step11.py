from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Andrei")
    
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("Novikau")
    
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("test@test.com")
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
    
    #поиск элемента содержащего текст
    welcome1 = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome1
    welcome_text = welcome1.text
    
    # с помощью assert проверяем приветсвенный текст
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(2)
    browser.quit()    