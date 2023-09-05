#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGIN = '<LOGIN>'
PASSWORD = '<PASSWORD>'

driver = webdriver.Firefox()
driver.get('https://vk.com/')
print('Title: "{}"'.format(driver.title))

driver.find_element_by_id('index_email').send_keys(LOGIN)
driver.find_element_by_id('index_pass').send_keys(PASSWORD)

# Делаем скриншот результата
driver.save_screenshot('before_auth.png')

driver.find_element_by_id("index_login_button").click()

wait = WebDriverWait(driver, timeout=10)

l_msg = wait.until(
    EC.presence_of_element_located((By.ID, 'l_msg'))
)

print('Title: "{}"'.format(driver.title))

# Делаем скриншот результата
driver.save_screenshot('after_auth.png')

l_msg.click()

im_dialogs = wait.until(
    EC.presence_of_element_located((By.ID, 'im_dialogs'))
)
im_dialogs.screenshot('dialogs_page.png')

print('Title: "{}"'.format(driver.title))

dialog_items = driver.find_elements_by_class_name('_im_dialog_link')

for dialog in dialog_items:
    print(dialog.text)

driver.quit()
