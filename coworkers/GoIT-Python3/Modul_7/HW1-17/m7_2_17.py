'''Модифицируем пример предыдущей задачи. Для функции do_setup необходимо предусмотреть второй параметр,
 который будет являться списком зависимостей.

Функция do_setup(args_dict, requiers) должна вызывать функцию setup с параметрами из словаря args_dict
 и параметром install_requires, который принимает значение requiers'''

from setuptools import setup


def do_setup(args_dict, requires):
    a = {'install_requires':requires}
    args_dict.update(a)
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=args_dict['install_requires'])