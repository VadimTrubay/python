from setuptools import setup, find_namespace_packages

setup(
    name='gui_lottery_generator',
    version='1.0.0',
    description='very helpful lottery',
    url='https://github.com/VadimTrubay/gui_lottery_generator.git',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    entry_points={'console_scripts': ['gui_lottery_generator=gui_lottery_generator.main:main']}
)