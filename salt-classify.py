#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  salt-classifier.py
#  
#  Copyright 2017 Manuel Oloarte <manuel@oloarte.ch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
dic_country = {
  'ch': 'switzerland',
  'ua': 'ukraine',
  'au': 'australia',
  'de': 'germany',
}
dic_city = {
	'syd': 'sydney',
	'iev': 'kiev',
	'zrh': 'zurich',
	'fra': 'frankfurt',
}
dic_environment = {
	'tst': 'testing',
	'dev': 'development',
	'stg': 'staging',
	'prd': 'production',
}


import sys
import re

def main():
	fqdn = sys.argv[1]
	fragments = fqdn.split('.')
	my_args = fragments[::-1]
	getCountry (my_args[0])
	getCity (my_args[1])
	getEnvironment (my_args[2])
	getCluster (my_args[3])
	print 'function:', my_args[4:]

def getCountry(my_tld):
	for tld, country in dic_country.iteritems():
		if tld == my_tld:
			print 'country: ' + country

def getCity(my_code):
	for code, city in dic_city.iteritems():
		if code == my_code:
			print 'city: ' + city

def getEnvironment(my_env):
	for env, environment in dic_environment.iteritems():
		if env == my_env:
			print 'environment: ' + environment

def getCluster(my_cluster):
	cluster_group = re.findall('\d+', my_cluster)
	cluster_name = re.findall('[a-z]+', my_cluster)
	print 'cluster_group: ' + ''.join(cluster_group)
	print 'cluster_name: ' + ''.join(cluster_name)

if __name__ == '__main__':
	main()

