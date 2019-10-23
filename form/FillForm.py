from selenium import webdriver
from json import load
from sys import argv

# 1 -> website URL
# python form/FillForm.py https://goodboysinc.weebly.com/contact.html

url = argv[1]

print(url)

with open("form/userInfo.json",'r') as file:
    userInfo = load(file)

print(userInfo)

driver = webdriver.Chrome()

driver.get(url)

formInputs = driver.find_elements_by_css_selector('.wsite-form-input.wsite-input')


formInputs[0].send_keys(userInfo['first-name'])
formInputs[1].send_keys(userInfo['second-name'])
formInputs[2].send_keys(userInfo['email'])
formInputs[3].send_keys(userInfo['additional'])

formInputs[0].submit()