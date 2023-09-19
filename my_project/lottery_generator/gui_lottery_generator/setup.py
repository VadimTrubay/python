from setuptools import setup, find_namespace_packages

setup(
    name='gui_lottery_generator',
    version='1.0.0',
    description='very gui_lottery_generator',
    url='https://github.com/VadimTrubay/python/tree/main/my_project/lottery_generator/gui_lottery_generator',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    entry_points={'console_scripts': ['gui_lottery_generator=gui_lottery_generator.main:main']}
)