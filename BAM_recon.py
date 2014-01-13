import re
import csv
import pandas as pd

file_name = 'C:\\Users\\jaccarey\\Documents\\Navy_FMO\\PDF to Excel\\18_AA_ReconOCT2013.txt'
f = open(file_name, 'r')
txt = f.readlines()
f.close()

txt2 = [line.replace('\n', '') for line in txt if 'For the month ended' not in line and
	'Fund Balance with Treasury Reconciliation (Treasury to Field Accounting System)' 
	not in line and 
	'Dec 19, 2013 10:36 AM' not in line]
txt3 = []
txt4 = []
txt5 = []
txt6 = []

delimiter = r"""(([a-zA-Z]|\d)[\s\t]+[\d\-])"""

def dollar_match(line):
	match = re.search(r'\d.\d{2}', line)
	if match:
		return True
	else:
		return False

for line in txt2:
	if 'Treasury Account Symbol' in line:
		temp = line.split('GWA')
		temp2 = [temp[0],
			 'GWA (Treasury)',
			 'Field Systems Total',
			 'Reconciling Balances',
			 'Reconciling Activity (Summary)']
		txt3.append(temp2)
	elif 'Less: Adjustments to Reconcile Field Systems to GWA' in line:
		txt3.append(line)
	elif not dollar_match(line):
		txt3.append(line)
	else:
		t_s = re.split(delimiter, line)
		t_l = []
		for i in range(3, len(t_s), 3):
			if i == 3:
				t_l.append(t_s[i - 3] + t_s[i - 2][0])
			
			t_l.append(t_s[i - 2][-1] + t_s[i])

		txt3.append(t_l)


for i, line in enumerate(txt3):
	if len(line) == 5:
		txt4.append(line)
		num = 5
	elif len(line) == 4:
		txt4.append(line + [''])
		num = 'unadj'
	elif len(line) == 3:
		txt4.append(line + ['', ''])
		num = 'C/D'
	elif len(line) == 1 or type(line) == str:
		txt4.append([line, '', '', '', ''])
	elif num == 'C/D':
		txt4.append([line[0], '', '', line[1], ''])
		num = 'C/D2'
	elif num == 'C/D2':
		txt4.append([line[0], '', '', '', line[1]])
	elif num == 'unadj':
		txt4.append([line[0], '', line[1], '', ''])

for line in txt4:
	if 'Treasury Account Symbol:' in line[0]:
		str_split = line[0].split(' ')
		bfy = str_split[-4]
		efy = str_split[-3]
		appn = str_split[-2]
		txt5.append(['BFY', 'EFY', 'ACCT Symbol'] + line)
	else:
		txt5.append([bfy, efy, appn] + line)
	
	if 'Adjusted FBWT Ending Balance' in line[0]:
		txt5.append(['' * 8])
		txt5.append(['' * 8])

cnt = 0

for line in txt5:
	if line[0] == 'BFY':
		cnt += 1
		line[7] = 'Reconciling Activity (Summary)'
		txt6.append(line + ['Reconciling Activity (Detail)'])
	
	elif len(line) > 1:
		if line[7] != '':
			if 'Registered' == line[3][:10]:
				txt6.append(line + [''])
			else:
				txt6.append(line[:7] + [''] + [line[7]])
		else:
			txt6.append(line + [''])
	else:
		txt6.append(line + [''])


writer = csv.writer(open('C:\\Users\\jaccarey\\Documents\\Navy_FMO\\PDF to Excel\\test.csv', 'wb'), delimiter = '|', quoting = csv.QUOTE_ALL)

writer.writerows(txt6)

