from setuptools import setup, find_packages

setup(

	name='datetime',
	version='1.0.0',
	description='a datetime project',
	url='https://github.com/odhiambocuttice/myfirstproject',
	author='odhiambo cuttice',
	author_email='odhiambocuttice@gmail.com',

	classifiers=[
         
         'License :: OSI Approved :: MIT License',
         'Programming language :: python :: 3.6',

	],

	keywords ='datetime setuptools development',

	packages =find_packages(),
	python_requires ='>=3.6',
	install_requires=['requests'],

	)