#!/usr/bin/env python3
from hashlib import new
import requests
import re
from datetime import datetime
import time
#pass url like this => https://zone-xsec.com/archive/page=

t1=datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

url = raw_input("URL => ")
pnum = int(input("Pages => "))
try:
	for a in range(1,pnum+1):
		r = requests.get(url+str(a)).text
		r = r.replace("\r\n", "")
		print('\n',url,a,'\n')		
		#print(r)
		preg = re.findall("            <td></td>            <td>(.*?)</td>            <td><a", r)
		preg = [preg for preg in preg if preg != '']
		#print(preg)
		for line in preg:
			#print(line)
			line = line.split('</td>            <td></td>            <td>')
			line = (line[-1])
			line = line.split('/')
			line = line[0]
			line = line.replace('.c...','.com')
			line = line.replace('.com...','.com')
			line = line.replace('.co...','.com')
			line = line.replace('...','.com')
			if "<a" in line or "href=" in line or "<img" in line:
				pass
			else:
				print('http://'+line)
				with open('zxrez/'+t1+'.txt', 'a') as rrr:
					rrr.write('http://'+line+'\n')
except Exception as e :
	print(e)
