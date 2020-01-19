try:  # Python 3
    from setuptools import setup
except ImportError:  # Python 2
    from distutils.core import setup

config = {
    "description": "Simple 2D game engine in pure Python",
    "author": "Kevin Feng",
    "url": "https://github.com/HereIsKevin/TwoDimensional",
    "downloard_url": "https://github.com/HereIsKevin/TwoDimensional",
    "version": "0.1.0",
    "install_requires": ["pillow"],
    "packages": ["TwoDimensional"],
    "scripts": [],
    "name": "TwoDimensional",
}

setup(**config)
