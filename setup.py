try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Managing food sales, stock over several days period',
    'author': 'Lain',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['foodOverview'],
    'scripts': [],
    'name': 'foodOverview'
}

setup(**config):

