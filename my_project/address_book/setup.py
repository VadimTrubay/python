from setuptools import setup, find_namespace_packages

setup(
    name='address_book',
    version='1.0.0',
    description='very helpful assistant bot',
    url='https://github.com/VadimTrubay/address_book.git',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    install_requires=['numexpr', 'colorama'],
    entry_points={'console_scripts': ['address_book=address_book.main:main']},
    package_data={'address_book': ['address_book/*.txt', 'address_book/*.bin']}
)