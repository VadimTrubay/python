from setuptools import setup, find_namespace_packages

setup(
    name='cli_assistant_bot',
    version='1.0.0',
    description='Very helpful assistant bot',
    url='https://github.com/VadimTrubay/cli_assistant_bot.git',
    author='Oleh Andrienko, Marina Krash, Yana Yakovlieva, Trubay_Vadim',
    author_email='vadnetvadnet@ukr.net',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    install_requires=['numexpr'],
    entry_points={'console_scripts': ['cli_assistant_bot=cli_assistant_bot.main:main']}
)