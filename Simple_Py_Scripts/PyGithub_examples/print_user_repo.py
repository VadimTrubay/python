#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install pygithub
from github import Github
from config import LOGIN, PASSWORD

# TODO: сделать версию с gui

# Пользователь, чьи репозитории собираемся вывести в консоль
user = 'gil9red'

gh = Github(LOGIN, PASSWORD)

# Словарь, у которого ключом является название репозитория, значением -- объект репозитория
repo_by_name_dict = {repo.name: repo for repo in gh.get_user(user).get_repos()}

# Подсчет количества репозиториев по языкам
from collections import Counter

counter_langs = Counter(repo.language for _, repo in repo_by_name_dict.items())
counter_langs = sorted(counter_langs.items(), key=lambda x: x[1], reverse=True)

# Словарь, у которого ключом является язык репозитория, значением -- объект репозитория
from collections import defaultdict

repo_by_lang_dict = defaultdict(list)

for _, repo in repo_by_name_dict.items():
    repo_by_lang_dict[repo.language].append(repo)

# Отсортировка репозиториев по количеству поставленных звезд
for _, repos in repo_by_lang_dict.items():
    repos.sort(key=lambda x: x.stargazers_count, reverse=True)

# Вывод репозиториев в соответствии их языку и популярности
for lang, number in counter_langs:
    print("{} ({}):".format(lang, number))

    for i, repo in enumerate(repo_by_lang_dict[lang], 1):
        print("    {}. {}: '{}' ({} star): {}".format(i, repo.name, repo.description,
                                                      repo.stargazers_count, repo.html_url))

    print()
