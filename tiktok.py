# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:58:34 2022

@author: Faizan
"""

# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


# =============================================================================
# User Define Function
# =============================================================================
def dummy_send(element, word, delay):    
    driver.find_element(By.XPATH,value=element).click()
    for c in word:
        driver.find_element(By.XPATH,value=element).send_keys(c)
        sleep(delay)

# =============================================================================
# End User Define
# =============================================================================

# =============================================================================
# Disable chrome items
# =============================================================================
options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
#options.add_argument("--incognito")
# =============================================================================
# End items
# =============================================================================



path =  r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe'

# Here Chrome will be used
driver = webdriver.Chrome(service=Service(path),options=options)


# URL of website
url = "https://www.tiktok.com/foryou"

# Opening the website
driver.get(url)


# Dynamic wait
#driver.implicitly_wait(60)

# finds button using its xpath
form = driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[1]/div/div[2]/button")
form.text
form.click()
# driver.refresh()

driver.get("https://www.tiktok.com/login/phone-or-email/email")
sleep(5)


user = dummy_send('//*[@id=\"loginContainer\"]/div[1]/form/div[1]/input', 'faizan_code0', 0.2)
sleep(1)


password = dummy_send('//*[@id=\"loginContainer\"]/div[1]/form/div[2]/div/input', 'software**1', 0.2)
sleep(1)


driver.implicitly_wait(2)
login_button = driver.find_element(By.XPATH, value = "//*[@id=\"loginContainer\"]/div[1]/form/button")
sleep(1)
login_button.click()


sleep(5)
like = driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[1]/span")
# print(like)
like.click()

sleep(5)
comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[2]/span")
print(comment)
comment.click()

# =============================================================================
# Message
# =============================================================================
message = ["Great "]

sleep(5)
post_comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div")
print(post_comment)
post_comment.click()
post_comment.send_keys("Rich")


sleep(5)
post_comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[2]")
print(post_comment)
post_comment.click()


sleep(5)
cross_btn =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[3]/div[1]/button[1]")
print(cross_btn)
cross_btn.click()

# Refresh here
driver.refresh()


# after refresh
sleep(5)
like = driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[1]/span")
# print(like)
like.click()

sleep(5)
comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[2]/span")
print(comment)
comment.click()


sleep(5)
post_comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div/div/div")
print(post_comment)
post_comment.click()
post_comment.send_keys("Rich")


sleep(5)
post_comment =  driver.find_element(By.XPATH, value = "//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[2]")
print(post_comment)
post_comment.click()


