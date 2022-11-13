# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:22:37 2022

@author: Faizan
"""


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver_path = '/Users/myuser/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe', options=options)
driver.get('https://google.com')

driver.close()