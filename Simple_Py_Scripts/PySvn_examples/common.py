#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://github.com/dsoprea/PySvn

def get_log_list(url__or__file_name: str, revision_from=None, limit=None) -> list:
    import os
    if os.path.exists(url__or__file_name):
        import svn.local
        repo = svn.local.LocalClient(url__or__file_name)
    else:
        import svn.remote
        repo = svn.remote.RemoteClient(url__or__file_name)

    return list(repo.log_default(revision_from=revision_from, limit=limit))


def get_log_list_by_author(url__or__file_name: str, log_list: list = None) -> dict:
    if not log_list:
        log_list = get_log_list(url__or__file_name)

    from collections import defaultdict
    author_by_log = defaultdict(list)

    for log in log_list:
        author_by_log[log.author].append(log)

    return author_by_log
