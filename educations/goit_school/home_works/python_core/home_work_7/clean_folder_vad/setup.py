from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_vad',
    version='1.0.0',
    description='Very useful code for cleaning folders',
    url='https://github.com/VadimTrubay/goit_school/tree/main/home_works/home_work_7/clean_folder/clean_folder',
    author='Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder_vad.clean:main']}
)