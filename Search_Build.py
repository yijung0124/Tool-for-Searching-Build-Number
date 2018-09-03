##Web Scrab from Jenkin 

import requests
from bs4 import BeautifulSoup
import re



tdc = [] #store tdc link

##Get data/information from Jenkin
changeID = input("Please input changeID:")
version = input("Please input version:")


def output(changeID, version):
	
	#test
	if version == 'test':
		url = 'http://jenkins-tdc.video54.local:8080/view/ESPP/view/POC/view/test-platform/job/TEST_BUILD_ALL_IMAGES/'
	
	else:
		print('Error!')
		
	link = requests.get(url)
	soup = BeautifulSoup(link.text, 'html.parser')
	li = soup.find_all('div', 'pane build-name')		#Find all links
		
	for l in li:		#Each link is under 'a href'
		next_link = l.find('a', href = True)
		correct_link = 'http://jenkins-tdc.video54.local:8080'+next_link['href']
		output_link = correct_link.replace("console", "parameters")		#Link is "console" page, but we need "parameters" page
		tdc.append(output_link)		#Store each link in list

	for x in range(len(li)):		
		link2 = requests.get(tdc[x])			
		soup2 = BeautifulSoup(link2.text, 'html.parser')
		li2 = soup2.find('input', 'setting-input')		 #ChangeNo. is under "input" and 'class' = setting-input
		h = li2['value']							#Get change No.
		if changeID > h:							#if changeID > first changeNo.
			link3 = requests.get(tdc[x-1])				#Get last changeNo.
			soup3 = BeautifulSoup(link3.text,'html.parser')
			li3 = soup3.find('input', 'setting-input')
			b = li3['value']
			console_link = tdc[x-1].replace("parameters", "console")			#Output information is under "console" page
			link4 = requests.get(console_link)
			console_soup = BeautifulSoup(link4.text, 'html.parser')
			li4 = console_soup.find('pre', 'console-output')				
			if str(li4).find('FAILURE') == -1:									#if we can find "FAILURE" string(It means the build is failure)
				li4_split = str(li4).split('finish:')[1]
				print(console_link)
				print('ChangeID:', b)
				print("Result:", li4_split)
				break
			else:
				x = x-1
				break

		elif changeID == h:						#if changeID = changeNo.
			link3 = requests.get(tdc[x])
			soup3 = BeautifulSoup(link3.text,'html.parser')
			li3 = soup3.find('input', 'setting-input')
			b = li3['value']
			console_link = tdc[x].replace("parameters", "console")
			link4 = requests.get(console_link)
			console_soup = BeautifulSoup(link4.text, 'html.parser')
			li4 = console_soup.find('pre', 'console-output')
			if str(li4).find('FAILURE') == -1:
				li4_split = str(li4).split('finish:')[1]
				print(console_link)
				print('ChangeID:', b)
				print("Result:", li4_split)
				break
			else:
				x = x-1
				break
	return b			
print("ChangeID:", output(changeID, version))





