# Use listdir to loop through files in folder
from os import listdir

# create list of folders relative to current directory
# to loop through each using indexing
dirs = ['12_Air Force CDR 1 2 3 Oct and Nov 2013', 
	'12_State Dept CDR 1 2 3 Oct and Nov 2013',
	'12_Army CDR 1 2 3 Oct and Nov 2013']

# stored appended filename in f_ext variable
f_ext = '.clean.txt'

# Air Force
for file_name in listdir('./' + dirs[0]): 
	f = open(dirs[0] + '/' +  file_name) 
	txt = f.readlines()
	f.close()

	txt2 = []

	for line in txt:
		if 'RUN' not in line and 'PERIOD' not in line and 'REGISTER' \
				not in line and 'TOTAL' not in line and line[0] != '0':
			txt2.append(line.lstrip())	# lstrip method removes leading spaces

	f = open(dirs[0] + '/' + file_name[:-4] + f_ext, 'w')

	for line in txt2:
		f.write(line)

	f.close()

# Army
for file_name in listdir('./' + dirs[2]):
	f = open(dirs[2] + '/' +  file_name)
	txt = f.readlines()
	f.close()

	txt2 = []

	for line in txt:
		if 'RUN' not in line and 'PERIOD' not in line and 'REG' \
				not in line and 'TOTAL' not in line and line[0] != '0':
			txt2.append(line.lstrip())	# lstrip method removes leading spaces

	f = open(dirs[2] + '/' + file_name[:-4] + f_ext, 'w')

	for line in txt2:
		f.write(line)

	f.close()

# State Department
for file_name in listdir('./' + dirs[1]):
	f = open(dirs[1] + '/' +  file_name)
	txt = f.readlines()
	f.close()

	txt2 = []

	for line in txt:
		if 'RUN' not in line and 'MONTH' not in line and 'REGISTER' \
				not in line and 'TOTAL' not in line and line[0] != '0': 
			txt2.append(line.lstrip())	# lstrip method removes leading spaces 
	
	f = open(dirs[1] + '/' + file_name[:-4] + f_ext, 'w')

	for line in txt2:
		f.write(line)

	f.close()

