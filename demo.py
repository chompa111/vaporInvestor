from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path  = r'.\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)
browser.get("https://steamcommunity.com/market/search?q=#p2_popular_desc")
time.sleep(2)
menu = browser.find_element_by_css_selector("#result_0")
menu.click()