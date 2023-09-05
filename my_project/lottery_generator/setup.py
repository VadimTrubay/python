from setuptools import setup, find_namespace_packages

setup(
    name='lottery',
    version='1.0.1',
    description='very helpful lottery',
    url='https://github.com/VadimTrubay/lottery_generator.git',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['lottery=lottery.main:main']}
)