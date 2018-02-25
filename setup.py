#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("VERSION", "rb") as f:
    data = f.read()
    version = data.decode("utf-8")


with open("LICENSE.txt", "rb") as f:
    data = f.read()
    license = data.decode("utf-8")


setup(name="scryfall-quest",
      version=version,
      description="Python API for Scryfall.com using requests",
      url="https://github.com/cmeister2/scryfall-quest",
      author="Max Dymond",
      author_email="cmeister2@gmail.com",
      license=license,
      packages=["scryfall_quest"],
      zip_safe=False,
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          "Development Status :: 2 - Pre-Alpha",

          # Indicate who your project is intended for
          'Intended Audience :: Developers',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      install_requires=[
          'requests',
      ],
      python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
      )
