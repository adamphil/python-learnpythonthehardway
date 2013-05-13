try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Adam Phillips',
    'url': 'www.github.com/adamphil',
    'download_url': 'www.github.com/adamphil',
    'author_email': 'adamjaredphillips@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['MAIN'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)