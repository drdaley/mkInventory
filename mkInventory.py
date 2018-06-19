import pprint
import cirpy as cr
import os

# if os.path.isfile('output.csv'):
# 	output = open('output.csv','w')
# elif not os.path.isfile('output.csv')
# 	output = open('output.csv','x')
# 	output.write('name|CAS|amount|units|comments|phase|location\n')

#output = open('output.csv','w')
again = ''
line = {'CAS':'','name':'','amount':'','units':'','comments':'','phase':'','location':''}
phaseOptions = ['solid','liquid','solution','gas']
unitsOptions = ['kg','g','mg','L','mL','lbs']
locations = list()
newHeader = os.path.isfile('output.csv')
print(newHeader)
if newHeader==False:
	a = open('output.csv','x')
	a.write('name|CAS|amount|units|comments|phase|location\n')
	a.close()
else:pass

with open('output.csv','a') as output:
	while again != 'n':
		# input CAS
		CAS = input('CAS number: ')
		#print(CAS)
		line['CAS'] = CAS
		try:
			nameList = cr.resolve(CAS,'names')
			if len(nameList) == 1:
				line['name'] = nameList
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
			line['amount'] = input('Amount? ')
			print('====================')
			for i,units in enumerate(unitsOptions):
				print(str(i)+') '+units)
			print('====================')
			p = input('What are the units? ')
			line['units'] = unitsOptions[int(p)]
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
					line['location'] = locations[int(lInp)]
				else:print('LOCATION NAMES MUST CONTAIN NON-NUMERIC CHARACTERS')
			else:
				line['location'] = lInp
				locations.append(lInp)
			line['comments'] = input('Any comments? ')
			formattedLine = line['name']+'|'+line['CAS']+'|'+line['amount']+'|'+line['units']+'|'+line['comments']+'|'+line['phase']+'|'+line['location']+'\n'
			output.write(formattedLine)
			print(formattedLine)
		except:print('ERROR ENTERING THE ENTRY.')
		again = input('Type "n" to exit, any other key to continue. ')




# choose name
# enter amount
# enter phase
# enter comments
