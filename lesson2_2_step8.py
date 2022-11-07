from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# импортируем модуль
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Andrei")
    #time.sleep(3)
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Novikau")
    #time.sleep(3)
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.test")
    #time.sleep(3)
    
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "text.txt"
    # получаем путь к text.txt
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    time.sleep(4)
    browser.quit()  
    