from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
chrome_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_path)
url="https://www.flipkart.com/search?q=samsung&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
page=8
for i in range(1,page):
    new_url=url+str(i)
    driver.get(new_url)
time.sleep(3)








