import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import pytesseract
from PIL import Image
import easyocr


def text_recognition(path: str):
    '''easyocr'''
    
    reader = easyocr.Reader(["en"])
    result = reader.readtext(path, detail=0)
    
    return result


def text_recognition1(path: str):
    '''pytesseract'''
    # C:\Users\Данил\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
    img = Image.open(path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Данил\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    
    return text


url_selenium = 'http://62837ecc-2085-45ec-9fc2-38141663bcbf.node.omwars.org/pages/c3725bed-cfab-48ce-bbb1-8d8b5e6ac83b.html'
path_to_driver = r"Selenium\chromedriver.exe"

# C:\Codding\CTF2023\Selenium\chromedriver.exe
# Selenium\chromedriver.exe
# with webdriver.Chrome(executable_path=r"C:\Codding\CTF2023\Selenium\chromedriver.exe") as driver:
#     driver.get(url_selenium)
#     img_src = driver.find_element(By.TAG_NAME, "img")
#     # img_src.send_keys('123')
#     print(img_src)
#     time.sleep(10)

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

s = Service(executable_path=path_to_driver)

driver = webdriver.Chrome(service=s, options=options)

try:
    count = 0
    driver.get(url_selenium)
    
    while True:
        time.sleep(1)
        img_url = driver.find_element(By.XPATH, "/html/body/img")
        img_url = img_url.get_attribute("src")
        img_name = img_url.split('.')[0].split('//')[1] + '.jpg'
        # print(img_name, "naaaamee")
        
        img_data = requests.get(img_url).content
        
        with open("Star requests/data" + img_name, 'wb') as handler:
            handler.write(img_data)
            print("end write")
        
        t1 = text_recognition("Star requests/data" + img_name)[0]
        print(t1)
        
        input = driver.find_element(By.XPATH, "/html/body/div[2]/p/input[1]")
        input.clear()
        input.send_keys(t1)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'big-button').click()
        print("click")
        time.sleep(1)
        
        img_url = driver.find_element(By.XPATH, "/html/body/img")
        img_url = img_url.get_attribute("src")
        img_name = img_url.split('.')[0].split('//')[1] + '.jpg'
        # print(img_name, "naaaamee")
        
        img_data = requests.get(img_url).content
        
        with open("Star requests/data" + img_name, 'wb') as handler:
            handler.write(img_data)
            print("end write")
        
        t2 = text_recognition1("Star requests/data" + img_name).strip()
        print(t2)
        
        input = driver.find_element(By.XPATH, "/html/body/div[2]/p/input[1]")
        input.clear()
        input.send_keys(t2)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'big-button').click()
        print("click")
        time.sleep(1)
        
        count += 1
        print(count)
        
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()