#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


FILE_NAME_REPO = '1_000__commits__repo'
FILE_NAME_COUNTER = FILE_NAME_REPO + '/' + 'counter.txt'

import os
ABS_FILE_NAME_COUNTER = os.path.abspath(FILE_NAME_COUNTER)

# ONLY NEW REPO
if os.path.exists(FILE_NAME_REPO):
    import shutil
    shutil.rmtree(FILE_NAME_REPO)


# pip install GitPython
import git
try:
    repo = git.Repo(FILE_NAME_REPO)
except:
    repo = git.Repo.init(FILE_NAME_REPO)

print('Repo:', repo)
print()

for i in range(1, 1000 + 1):
    print(i)

    with open(ABS_FILE_NAME_COUNTER, 'w') as f:
        f.write(str(i))

    repo.index.add([ABS_FILE_NAME_COUNTER])
    repo.index.commit('#' + str(i))

logs = repo.git.log('--pretty=format:%H%x09%an%x09%ad%x09%s').splitlines()
print('\nLogs[{}]:'.format(len(logs)))

for log in logs:
    print(log)
