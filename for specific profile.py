# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:46:39 2022

@author: Faizan
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


path =  r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe'

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Faizan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 25")
driver = webdriver.Chrome(service=Service(path), options=options)
driver.get("https://www.google.co.in")

