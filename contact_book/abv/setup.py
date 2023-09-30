from setuptools import setup, find_namespace_packages

setup(
    name='Addressbook',
    version='1.0.0',
    description='Very helpful assistant bot',
    url='https://github.com/VadimTrubay/abv.git',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    install_requires=['numexpr'],
    entry_points={'console_scripts': ['Addressbook=Addressbook.main:main']},
    package_data={'Addressbook': ['Addressbook/*.txt', 'Addressbook/*.bin']}
)