# Opens text file "links" and extracts ODL file names
# Based on link starting with http and ending with .gz 
'''
ODL00000001_100-06-1.mol.gz
ODL00000002_100-09-4.mol.gz
ODL00000003_100-42-5.mol.gz
ODL00000004_100-46-9.mol.gz
'''

b = []
for line in open("links"):
	line = line.strip()
	if line != '':	
		if((line[0] == 'h') and line[-1:] == 'z'):
			if(line[46] == 'o'):
				b.append(line)
for piece in b:
	print piece[58:]#print only ODL
