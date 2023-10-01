from setuptools import setup

setup(name='sort_your_folder',
      version='2022',
      description='Script will sort your useless folder',
      url='https://github.com/Dreamwave7/HW6/blob/main/HW6m.py',
      author='Dreamwave7',
      author_email='dima190179@gmail.com',
      license='MIT',
      packages=['clean_folder'])
      entry_points={'console_scripts':['foldsort = sort_your_name.clean.main']}
)