from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-exampleform',
	version=version,
	description="Simple example form for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Ross Thompson',
	author_email='ross.thompson@statcan.gc.ca',
	url='https://github.com/thriuin',
	license='GPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.exampleform'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	    example_form=ckanext.exampleform.plugins:ExampleFormPlugin
	""",
)
