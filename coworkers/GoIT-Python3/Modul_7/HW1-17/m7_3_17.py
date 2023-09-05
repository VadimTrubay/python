'''Продолжаем модифицировать пример. Для функции do_setup необходимо предусмотреть третий параметр,
который будет являться словарем, где мы можем указать список "точек входа" для ключа console_scripts.

Функция do_setup(args_dict, requiers, entry_points) должна вызывать функцию setup с параметрами из словаря args_dict
и параметром install_requires, который принимает значение requiers. Третий параметр entry_points принимает словарь,
где мы можем указать список "точек входа" для ключа console_scripts.'''

from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    b = {'console_scripts': entry_points}
    args_dict.update(b)
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points=args_dict['console_scripts']
          )