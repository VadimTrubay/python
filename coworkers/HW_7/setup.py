from setuptools import setup, find_packages

setup(
    name = 'clean_folder_Andrii_OSA',
    version = '1.0',
    author = 'GoIT',
    entry_points = {
        'console_scripts': ['clean-folder = clean_folder.main:path_function'],
    },
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    description = 'Clean folder script'
)