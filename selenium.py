# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:56:32 2022

@author: Faizan
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path = r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe')

driver.get("https://www.tiktok.com/")

# driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);


## find element using xpath 
l = driver.find_element_by_xpath('//a[@href="/documentation/webdriver/"]')


driver.close()
