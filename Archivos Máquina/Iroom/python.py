#!/usr/bin/env python

#ruta del archivo /var/lib/asterisk/agi-bin/python.py
import sys
from asterisk.agi import *
import urllib, json

agi = AGI()

url = ["/temperature", "/humidity", "/light", "/sound", "/motion"]

for sensor in url:
	response = urllib.urlopen("http://127.0.0.1:8000" + sensor)
	data = json.loads(response.read())
	num = data[sensor[1:]]
	agi.set_variable(sensor[1:], num)
	agi.verbose(num)
