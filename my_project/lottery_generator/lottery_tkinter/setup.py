from setuptools import setup, find_namespace_packages

setup(
    name='lottery_tkinter',
    version='1.0.0',
    description='very helpful lottery_tkinter',
    url='https://github.com/VadimTrubay/lottery_tkinter',
    author='TrubayVadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    entry_points={'console_scripts': ['lottery_tkinter=lottery_tkinter.main:main']}
)