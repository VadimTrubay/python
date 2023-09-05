import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import django
from django.conf import settings
# from setuptools import setup, find_packages
#
# setup(
#     name='fuel_list',
#     packages=find_packages()
# )

flag = True
if not settings.configured:
    django.setup()
    flag = False


def check_settings():
    print(flag)


if __name__ == "__main__":
    check_settings()
