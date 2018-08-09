import pprint
import cirpy as cr
import os
import mkInvDefs
import datetime as dt
import requests

again = ''
line = {'CAS':'','name':'','amount':'','units':'','comments':'','phase':'','location':''}
phaseOptions = mkInvDefs.phaseOptions
unitsOptions = mkInvDefs.unitsOptions
locations = mkInvDefs.locations
comments = mkInvDefs.comments
today = dt.datetime.today()
timestamp = today.strftime('%Y-%m-%d_%H%M')
fileName = 'output{0}.csv'.format(timestamp)
newHeader = os.path.isfile(fileName)
#print(newHeader)
if newHeader==False:
	print('Creating {0}'.format(fileName))
	a = open(fileName,'x')
	titleString = str()
	a.write('name|CAS|amount|units|comments|phase|location\n')
	a.close()
else:print('{0} exists, appending to existing file.'.format(fileName))

with open(fileName,'a') as output:
	while again != 'n':
		line = {'CAS':'','name':'','amount':'','units':'','comments':'','phase':'','location':''}
		# input CAS
		CAS = input('CAS number: ')
		#print(CAS)
		line['CAS'] = CAS
		if CAS == '':
			res = input('Enter the chemical name manually: ')
			line['name'] = res
		else:
			try:
				#'https://cactus.nci.nih.gov/chemical/structure/555-55-5/names'
				url='https://cactus.nci.nih.gov/chemical/structure/{0}/names'.format(CAS)
				response = None
				response=requests.get(url,timeout=5)
				nameList=response.text.splitlines() # if the request times out, response.text will be undefined: then except

				#nameList = cr.resolve(CAS,'names')
				if len(nameList) == 1:
					if nameList == ['<h1>Page not found (404)</h1>']:
						raise Exception()
					line['name'] = nameList
					print(nameList)
				elif len(nameList) > 1:
					for i,name in enumerate(nameList):
						print(str(i)+') '+name)
					nameIndex = input('Use which name? ')
					line['name'] = nameList[int(nameIndex)]

			except:
				print('The CAS number could not be resolved.')
				print('This is somewhat common.')
				res = input('Enter the chemical name manually: ')
				line['name'] = res
		try:


			#line['units'] = input('Units? ')
			#print('Error entering the entry.')
			# Phase block

			print('====================')
			for i,phase in enumerate(phaseOptions):
				print(str(i)+') '+phase)
			print('====================')
			p = input('What is the phase? ')
			line['phase'] = phaseOptions[int(p)]
			# print('Error in phase entry.')
			# Unit block
			print('Amount: Only enter the value of the amount, not the units.')
			line['amount'] = input('Amount?  ')
			print('====================')
			for i,units in enumerate(unitsOptions):
				print(str(i)+') '+units)
			print('====================')
			print('For units: number to specify an item on the list, or type new unit name.)')
			p = input('What are the units? ')
			if p.isdigit(): line['units'] = unitsOptions[int(p)]
			elif p.isalpha():
				 line['units'] = p
				 unitsOptions.append(p)
			# print('Error in units entry.')
			if len(locations) > 0:
				print('====================')
				print('=Use integer to specify previous location=')
				for i,l in enumerate(locations):
					print(str(i)+') '+l)
				#print('===============')
				print()
			else:pass
			#print('(Enter an integer or location name.): ')
			lInp = input('Where is the chemical located? ')
			if lInp.isdigit():
				if int(lInp) in list(range(len(locations))):
					#print(locations[int(lInp)])
					line['location'] = locations[int(lInp)]
				else:print('LOCATION NAMES MUST CONTAIN NON-NUMERIC CHARACTERS')
			else:
				line['location'] = lInp
				locations.append(lInp)
			if len(comments) > 0:
				for i,c in enumerate(comments):
					print(str(i)+') '+c)
			else: pass
			print('====================')
			comm = input('Any comments? ')
			if comm.isdigit():
				if len(comments) > 0:
					if int(comm) in list(range(len(comments))):
						line['comments'] = comments[int(comm)]
					else:print("COMMENTS MUST CONTAIN NON-NUMERIC CHARACTERS")
			else:
				line['comments'] = comm
				comments.append(comm)
			formattedLine = line['name']+'|'+line['CAS']+'|'+line['amount']+'|'+line['units']+'|'+line['comments']+'|'+line['phase']+'|'+line['location']+'\n'
			output.write(formattedLine)
			print(formattedLine)
		except:print('ERROR ENTERING THE ENTRY.')
		again = input('Type "n" to exit, any other key to continue. ')




# choose name
# enter amount
# enter phase
# enter comments
