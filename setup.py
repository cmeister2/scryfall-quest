#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("VERSION", "rb") as f:
    data = f.read()
    version = data.decode("utf-8")


with open("LICENSE", "rb") as f:
    data = f.read()
    license = data.decode("utf-8")


setup(name="scryfall-quest",
      version=version,
      description="Python API for Scryfall.com using requests",
      url="https://github.com/cmeister2/scryfall-quest",
      author="Max Dymond",
      author_email="cmeister2@gmail.com",
      license=license,
      packages=["scryfall-quest"],
      zip_safe=False)
