try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple Catmat (SIASG) XML Parser',
    'author': 'Oswaldo Ferreira',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'oswluizf@gmail.com',
    'version': '0.1',
    'packages': ['catmat-parser'],
    'scripts': [],
    'name': 'catmat-parser'
}

setup(**config)
