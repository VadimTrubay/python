#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import time
import re
import sys

# pip install selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

sys.path.append('get_all_tracks_playlist')
from common import Track, get_track, seconds_to_str
from config import profile, url
from run_first_track import play_track


SEARCHING_TRACK = 'Шишки-телепаты'


driver = None
try:
    # Mute
    profile.set_preference("media.volume_scale", "0.0")

    driver = webdriver.Firefox(profile)
    driver.implicitly_wait(2)
    driver.get(url)
    print(f'Title: {driver.title!r}')

    time.sleep(2)

    play_track(driver, SEARCHING_TRACK)

    player_progress_el = driver.find_element_by_css_selector('.player-progress')
    progress__line_el = player_progress_el.find_element_by_css_selector('.progress__bar.progress__progress > .progress__line')

    while True:
        try:
            track_playing_el = driver.find_element_by_css_selector('.d-track_playing')
            track = get_track(track_playing_el)
        except (NoSuchElementException, StaleElementReferenceException):
            continue

        total_seconds = track.get_seconds()
        value = progress__line_el.get_attribute('style')

        # Example: style="transform: scaleX(0.4728);"
        m = re.search(r'scaleX\((.+?)\);', value)
        if m:
            progress_percent = float(m.group(1))
            progress_left = total_seconds * progress_percent
            progress_left_str = seconds_to_str(progress_left)
            progress_right_str = seconds_to_str(total_seconds)
            print(f'{track.title}. {progress_left_str} / {progress_right_str} ({progress_percent:.1%})')

        time.sleep(1)

finally:
    if driver:
        driver.quit()
