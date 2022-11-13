# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:41:11 2022

@author: Faizan
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from email.message import EmailMessage
from time import sleep
import smtplib
import random
import ssl


# =============================================================================
# User Define Function (Slow Typing with delay and conditions)
# =============================================================================
def dummy_send(element, word, delay, clicks):
    driver.find_element(By.XPATH, value=element).click()

    if clicks == 0:
        for c in word:
            driver.find_element(By.XPATH, value=element).send_keys(c)
            sleep(delay)

    elif clicks == 1:
        for c in word:
            driver.find_element(By.XPATH, value=element).send_keys(c)
            sleep(delay)
        driver.find_element(By.XPATH, value=element).send_keys(Keys.ENTER)

    else:
        for c in word:
            driver.find_element(By.XPATH, value=element).send_keys(c)
            sleep(delay)

# =============================================================================
# End User Define
# =============================================================================

# =============================================================================
# User Define Function (Email Sender)
# =============================================================================


def Email_Send(subject, body):
    sender_email = "email.tester.faizan@gmail.com"
    email_password = "hcbsqtdwdpniazgg"
    reciver_email = "faizanmunsafcode@gmail.com"

    em = EmailMessage()

    em['From'] = sender_email
    em['To'] = reciver_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, email_password)
        smtp.sendmail(sender_email, reciver_email, em.as_string())
# =============================================================================
# End User Define
# =============================================================================



# =============================================================================
# Disable chrome items
# =============================================================================
profile = "C:\\Users\\Faizan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 25"
options = uc.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.add_argument("user-data-dir={}".format(profile))
# options.add_argument("--incognito")
# =============================================================================
# End items
# =============================================================================


driver = uc.Chrome(version_main=107, options=options)


driver.get('chrome://settings/clearBrowserData')
sleep(5)

action = ActionChains(driver)

action.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ARROW_DOWN)
sleep(5)

clear_btn = driver.execute_script("return document.querySelector(\"settings-ui\").shadowRoot.querySelector(\"settings-main\").shadowRoot.querySelector(\"settings-basic-page\").shadowRoot.querySelector(\"settings-section > settings-privacy-page\").shadowRoot.querySelector(\"settings-clear-browsing-data-dialog\").shadowRoot.querySelector(\"#clearBrowsingDataConfirm\")")
clear_btn.click()
sleep(2)


try:
    driver.get('https://www.tiktok.com/login/phone-or-email/email')
    sleep(5)

    user = dummy_send(
        '//*[@id=\"loginContainer\"]/div[1]/form/div[1]/input', 'faizan_code0', 0.2, 0)
    sleep(1)

    password = dummy_send(
        '//*[@id=\"loginContainer\"]/div[1]/form/div[2]/div/input', 'software**1', 0.2, 0)
    sleep(1)

    # =============================================================================
    # Login Button
    # =============================================================================
    driver.implicitly_wait(2)
    login_button = driver.find_element(
        By.XPATH, value="//*[@id=\"loginContainer\"]/div[1]/form/button")
    sleep(1)
    login_button.click()
    sleep(2)
    error = driver.find_element(By.CLASS_NAME, value="#tiktok-3i0bsv-DivTextContainer e3v3zbj0")
    if error.is_displayed() == True:

        body = f'Hey Faizan! There is Error occur || {error.text} ||, I am Sorry for that'

        Email_Send("Field Error", body)

        print(error.text)

    elif error.is_displayed() == False:
        print("login SuccessFull ! ")
        
    else:
        print("Captcha Error ! ")


except Exception as e:

    print(e)
    driver.find_element(By.XPATH,value="//*[@id=\"verify-bar-close\"]")
   #captcha = driver.find_element(By.CSS_SELECTOR, vlaue = "//*[@id=\"captcha-verify-image\"]")
    
   


# =============================================================================
# Message
# =============================================================================
message = ["Great ", "Amazing", "Wow Amazing Video"]
random_message = random.randrange(len(message))
ran_message = message[random_message]

# =============================================================================
# Like videos And Comment it
# =============================================================================
for i in range(0, 2, 1):
    sleep(5)
    like = driver.find_element(
        By.XPATH, value="//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[1]/span")
    # print(like)
    like.click()

    sleep(5)
    comment = driver.find_element(
        By.XPATH, value="//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[2]/span")
    # print(comment)
    comment.click()

    sleep(5)
    type_comment = dummy_send(
        "//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[1]/div/div[1]/div/div/div/div/div/div/div", ran_message, 0.2, 0)
    # print(type_comment)

    sleep(5)
    post_comment = driver.find_element(
        By.XPATH, value="//*[@id=\"app\"]/div[2]/div[3]/div[2]/div[4]/div/div[2]")
    # print(post_comment)
    post_comment.click()

    sleep(5)
    cross_btn = driver.find_element(
        By.XPATH, value="//*[@id=\"app\"]/div[2]/div[3]/div[1]/button[1]")
    # print(cross_btn)
    cross_btn.click()

    # Refresh here
    driver.refresh()

# =============================================================================
# Search Bar for Searching Username
# =============================================================================
sleep(5)
search_bar = dummy_send(
    "//*[@id=\"app\"]/div[1]/div/div[1]/div/form/input", "khang_19.90", 0.2, 1)


for i in range(1,6,1):
    print(i)
    follow = f"//*[@id=\"app\"]/div[2]/div[2]/div[2]/div[{i}]"
    find_user_list = driver.find_element(By.XPATH, value=follow)
    print(find_user_list.text)
    
    
    
    
follow_btn = driver.find_element(By.XPATH, value ="//*[@id=\"app\"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button")
print(follow_btn.text)
follow_btn.click()

message_btn = driver.find_element(By.XPATH, value ="//*[@id=\"app\"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/a/button")

print(message_btn.text)

driver.refresh()


driver.get("https://www.tiktok.com/logout")