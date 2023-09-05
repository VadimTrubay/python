# helpme_pack
Guide to create package for Pypi.org:
1) Clone this repository to you local computer
2) Go to PyCharm or VSC and create 'Virtual Environment'
Unix/macOS: python3 -m venv myenv
            source myenv/bin/activate
Windows: py -m venv myenv
         myenv\Scripts\activate
3) Upgrade necessary tools:
Unix/macOS: python3 -m pip install --upgrade pip
            python3 -m pip install --upgrade pip setuptools wheel
            python3 -m pip install --upgrade build
            python3 -m pip install --upgrade twine
Windows:    py -m pip install --upgrade pip 
            py -m pip install --upgrade pip setuptools wheel
            py -m pip install --upgrade build
            py -m pip install --upgrade twine

4) Edit file 'setup.py' - write your: fullname, email, website
5) Start building your package
Unix/macOS:  python3 -m build
Windows:     py -m build
6) If building is Successfull:
7) Start upload to test.pypi.org(you can be registered in test.pypi.org)
Unix/macOS:  python3 -m twine upload --repository testpypi dist/*
Windows:     py -m twine upload --repository testpypi dist/*
8) Excelent - you succesfully uploud your package on www.test.pypi.org 
9) If you want upload to pypi.org? Do next steps!(You can be registered in pypi.org)
Unix/macOS:  twine upload dist/*
Windows:     twine upload dist/*
 
