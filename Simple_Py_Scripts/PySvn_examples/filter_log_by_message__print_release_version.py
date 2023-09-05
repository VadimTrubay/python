#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import config

import svn.local
repo = svn.local.LocalClient(config.SVN_FILE_NAME)

# OR:
# import svn.remote
# repo = svn.remote.RemoteClient(config.URL_SVN)


log_list = [log for log in repo.log_default()]
print('Total commits:', len(log_list))
print()

release_version_log_list = [log for log in log_list if log.msg and 'Release version' in log.msg]
print('Release version log ({}):'.format(len(release_version_log_list)))

for i, log in enumerate(release_version_log_list, 1):
    print('    {:6}. [rev {}] {} {:15} "{}"'.format(i, log.revision, log.date, log.author, log.msg))
