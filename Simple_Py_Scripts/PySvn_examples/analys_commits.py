#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from common import get_log_list, get_log_list_by_author

import config
url = config.SVN_FILE_NAME

log_list = get_log_list(url)
print('Total commits ({}):'.format(len(log_list)))

author_by_log = get_log_list_by_author(url, log_list)

for author, logs in sorted(author_by_log.items(), key=lambda item: len(item[1]), reverse=True):
    print('    {}: {}'.format(author, len(logs)))
