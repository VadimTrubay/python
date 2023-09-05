#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)  # seconds

try:
    driver.get('https://www.google.ru/')
    print('Title: "{}"'.format(driver.title))

    with open('hplogo.png', 'wb') as f:
        image_data = driver.find_element_by_id('hplogo').screenshot_as_png
        f.write(image_data)

    with open('searchform.png', 'wb') as f:
        image_data = driver.find_element_by_id('searchform').screenshot_as_png
        f.write(image_data)

    driver.save_screenshot('screenshot.png')

finally:
    driver.quit()
