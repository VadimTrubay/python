#!/bin/sh
python manage.py runserver 0.0.0.0:8080
python fuel_list/utils/schedule_scrap.py