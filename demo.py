from selenium import webdriver
from selenium.webdriver.common.by import By

path  = r'.\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)
browser.get("https://steamcommunity.com/market/search?q=#p2_popular_desc")