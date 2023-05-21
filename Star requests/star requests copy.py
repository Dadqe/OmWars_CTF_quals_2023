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

# a = "357f6074-aebc-48ac-b4a8-7df50adde3b7"

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


# def main():
#     # text = text_recognition("7edffa59-caff-4045-907d-fdb5f1eacb00.jpg")[0][1]
#     text = text_recognition("Star requests/data/ff0f21fb-e1de-4d72-8077-851c3d8f399a.jpg")[0]
#     text1 = text_recognition1("Star requests/data/ff0f21fb-e1de-4d72-8077-851c3d8f399a.jpg").strip()
    
#     print(a)
#     print(text)
#     print(text1)
    
#     if text != a:
#         print('text !=')
    
#     if text1 != a:
#         print('text1 !=')
        
#     # assert text == a, "Неправильно распознал, должен быть 357f6074-aebc-48ac-b4a8-7df50adde3b7"
#     # assert text1 == a, "Неправильно распознал, должен быть 357f6074-aebc-48ac-b4a8-7df50adde3b7"


def main(jpg_path: str):
    a = jpg_path.split('/')[-1].split('.')[0]
    
    # text = text_recognition("7edffa59-caff-4045-907d-fdb5f1eacb00.jpg")[0][1]
    text = text_recognition(jpg_path)[0]
    text1 = text_recognition1(jpg_path).strip()
    
    print(a)
    print(text)
    print(text1)
    
    if text != a:
        print('text !=')
    
    if text1 != a:
        print('text1 !=')
        
    # assert text == a, "Неправильно распознал, должен быть 357f6074-aebc-48ac-b4a8-7df50adde3b7"
    # assert text1 == a, "Неправильно распознал, должен быть 357f6074-aebc-48ac-b4a8-7df50adde3b7"

# 357f6074-aebc-48ac-b4a8-7df50adde3b7
# 357f6074-aebc-48ac-b4a8-7df50adde3b7

if __name__ == "__main__":
    main("Star requests/data/old/59d984e0-4653-4250-a744-c60006046b26.jpg")