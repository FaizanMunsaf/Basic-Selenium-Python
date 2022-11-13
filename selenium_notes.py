# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:07:21 2022

@author: Faizan
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

path =  r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')
# options.add_argument('--kiosk')
# options.add_argument('--window-position=0,0')
# options.add_argument('--disable-infobars');
# options.add_argument('--window-size=1920,1080')

# =============================================================================
# This Parameter is use for run browser at backend
# ==========================================================
# options.add_argument("--headless")      
# =============================================================================

driver = webdriver.Chrome(service=Service(path),options=options)
driver.get("https://www.google.com")