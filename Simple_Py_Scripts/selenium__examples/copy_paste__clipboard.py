#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://ru.stackoverflow.com/a/745919

# pip install pyperclip
import pyperclip
from time import sleep

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Открываем и копируем содержимое файла
with open(__file__, encoding='utf-8') as f:
    text = f.read()
    pyperclip.copy(text)

driver = webdriver.Firefox()
driver.get('https://pastebin.com/')

# Вставляем текст с буфера обмена
driver.find_element_by_id('paste_code').send_keys(Keys.CONTROL + 'v')

# sleep для того чтобы увидеть результат, перед тем как будет
# вызван driver.quit(), который закроет окно браузера
sleep(5)

driver.quit()
