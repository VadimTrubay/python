#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import time

# pip install schedule
import schedule

import db
from common import ROOT_DIR, get_table, logger
from get_assigned_open_issues_per_project import get_assigned_open_issues_per_project

sys.path.append(str(ROOT_DIR.parent / 'wait'))
from wait import wait


def run():
    while True:
        try:
            logger.info(f'Начало')

            assigned_open_issues_per_project = get_assigned_open_issues_per_project()
            logger.info(
                'Всего задач: %s\n\n%s\n',
                sum(assigned_open_issues_per_project.values()),
                get_table(assigned_open_issues_per_project)
            )

            ok = db.add(assigned_open_issues_per_project)
            if ok is None:
                logger.info("Количество открытых задач в проектах не поменялось. Пропускаю...")
            elif ok:
                logger.info("Добавляю запись")
            else:
                logger.info("Сегодня запись уже была добавлена. Пропускаю...")

            logger.info('\n' + '-' * 100 + '\n')
            break

        except Exception:
            logger.exception('Ошибка:')

            logger.info('Через 15 минут попробую снова...')
            wait(minutes=15)


if __name__ == '__main__':
    # Каждую неделю, в субботу, в 12:00
    schedule\
        .every().week\
        .saturday.at("12:00")\
        .do(run)

    while True:
        schedule.run_pending()
        time.sleep(60)
