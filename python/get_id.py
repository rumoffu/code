# Opens text file "3038html.txt" and prints out ODL_cas# and pubchem_id (if it exists), 1 set per line
# Based on link with http and ending with .gz and being odorant (not receptor) for ODL_cas#, and cgi for pubchem_id
'''
ODL00000001_100-06-1	7476
ODL00000002_100-09-4	7478
ODL00000003_100-42-5	7501
'''
b = []
for line in open("3038html.txt"):
	line = line.strip()
	if line != '':	# avoids problems with checking blank lines after the strip()
		if((line[0] == 'h') and line[-1:] == 'z'): # starts with http and ends with mol.gz
			if(line[46] == 'o'): # only get odorant (not receptor)
				b.append(line)
	if line.find("cgi") != -1: #gets lines with the pubchem_id which comes after cgi
		b.append(line)
s = ""
for piece in b:
	# ODL_cas# is http://mdl.shsmu.edu.cn/ODORCommon/datasource/odorant/mol/ODL00000010_100-86-7.mol.gz
	# pubchem id is http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=7476&loc=ec_rcs
	cid = piece.find("cid=") # pubchem_id starts after cid= 
	loc = piece.find("&loc") # pubchem_id ends before &loc
	odl = piece.find("ODL") # get index of ODL
	gz = piece.find("gz") # get index of gz

	if odl != -1: # ODL_cas# in this line
		s += piece[odl:gz-5] # get from ODL and cut off the .mol.
		s += '\t' # add a tab
	else: #elif cid != -1: # piece has pubchem_id
		s += piece[cid+4:loc] # get pubchem_id which starts 4 after cid and ends before loc
		print s
		s = ""

