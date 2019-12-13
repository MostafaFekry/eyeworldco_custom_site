# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in eyeworldco_custom_site/__init__.py
from eyeworldco_custom_site import __version__ as version

setup(
	name='eyeworldco_custom_site',
	version=version,
	description='Custom app to Eye of the world Site',
	author='MostafaFekry',
	author_email='mostafa.fekry@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
