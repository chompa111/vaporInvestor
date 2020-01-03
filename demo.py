from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
path  = r'.\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)
browser.get("https://steamcommunity.com/market/listings/730/Shattered%20Web%20Case")
time.sleep(3)
raw_page_string=browser.page_source

raw_price_rex=re.search(r"var line1=\[(\[.*\])*.*\]",raw_page_string)
raw_price_string=raw_price_rex.group(1)

raw_objects=re.findall(r"\[(.*?)\],",raw_price_string)

for obj in raw_objects:
	print("os dados são------>"+obj)


'''
for i in range(10):
	menu = browser.find_element_by_css_selector("#result_"+str(i))
	menu.click()
	time.sleep(2)
	browser.back()
	time.sleep(2)
'''