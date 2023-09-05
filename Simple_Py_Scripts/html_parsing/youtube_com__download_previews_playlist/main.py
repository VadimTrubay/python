#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
from pathlib import Path

sys.path.append('..')
sys.path.append('../..')
from get_valid_filename import get_valid_filename
from youtube_com__results_search_query import Playlist


def download_playlist_video_previews(url_or_id: str):
    playlist = Playlist.get_from(url_or_id)
    safe_playlist_title = get_valid_filename(playlist.title)

    dir_name = Path(f'{safe_playlist_title}. {playlist.id}')
    dir_name.mkdir(parents=True, exist_ok=True)

    for video in playlist.video_list:
        safe_title = get_valid_filename(video.title)
        img_data = video.get_thumbnail_for_maxresdefault()

        file_name = dir_name / f'{video.seq}. {safe_title}. {video.id}.jpg'
        file_name.write_bytes(img_data)


if __name__ == '__main__':
    download_playlist_video_previews('PLKom48yw6lJrkPuqimEiH3PT1ibALMh0k')
    download_playlist_video_previews('PLejGw9J2xE9XCDw_lFIo9RJCnzpr6P_0Z')

    url = 'https://www.youtube.com/playlist?list=PLndO6DOY2cLyxQYX7pkDspTJ42JWx07AO'
    download_playlist_video_previews(url)
