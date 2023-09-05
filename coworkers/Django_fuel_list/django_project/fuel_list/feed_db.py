import django
import os
import pickle
from models import Price
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# django.setup()
# from setuptools import setup, find_packages
#
# setup(
#     name='utils',
#     packages=find_packages()
# )
#
file = 'utils/data.txt'


def feed_db(file_name):
    print('Start feeding DB')
    with open(file_name, 'rb') as fh:
        data = pickle.load(fh)
        for d in data:
            feed = Price()
            feed.title = d['title']
            feed.gas = d['gas']
            feed.dp = d['dp']
            feed.nf = d['nf']
            feed.nf_plus = d['nf_plus']
            feed.nt = d['nt']
            feed.save()


if __name__ == '__main__':
    feed_db(file)
