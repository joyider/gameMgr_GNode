#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# gameMgr_GNode (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of gameMgr_GNode.
#
#    gameMgr_GNode is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 9/4/16 :: 10:06 PM
from setuptools import setup, find_packages
import versioneer

with open('README.rst') as file:
	long_description = file.read()
with open('CHANGES.rst') as file:
	long_description += '\n\n' + file.read()

setup(
	name='gameMgr_GNode',
	version=versioneer.get_version(),
	cmdclass=versioneer.get_cmdclass(),
	description="Norse Game Manager-Node installation ",
	long_description=long_description,
	classifiers=[
		"Programming Language :: Python",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: System :: Boot",
		"Topic :: System :: Systems Administration",
		"Topic :: Internet :: WWW/HTTP :: Site Management",
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: GPLv3",
		"Development Status :: 3 - Alpha",
	],
	keywords='http,web,norse,game,joyider',
	author='André Karlsson',
	author_email='andre.karlsson@protractus.se',
	url='https://github.com/joyider/gameMgr_GNode',
	license='GPLv3',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=True,
	# install_requires=['requests','http-signature'],
)
