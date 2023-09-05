'''Для инициализации своего проекта, создайте вспомогательную функцию do_setup(args_dict),
 которая будет вызывать функцию setup с параметрами из словаря args_dict.

Структура словаря для параметра args_dicts должна быть следующей'''

from setuptools import setup


def do_setup(args_dict):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          url=args_dict['url'],
          license=args_dict['license'],
          packages=args_dict['packages'],
         )






# from setuptools import setup
#
#
# def do_setup(args_dict):
#     setup = []
#     for i in args_dict:
#       string = i.replace(':', '=')
#       setup.append(string)
#       tuple(setup)
#     return setup


