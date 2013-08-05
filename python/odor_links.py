# Opens text file "links" and prints out ODL file links
# Based on link starting with http and ending with .gz and being odorant (not receptor) 
'''
http://mdl.shsmu.edu.cn/ODORCommon/datasource/odorant/mol/ODL00000001_100-06-1.mol.gz
http://mdl.shsmu.edu.cn/ODORCommon/datasource/odorant/mol/ODL00000002_100-09-4.mol.gz
http://mdl.shsmu.edu.cn/ODORCommon/datasource/odorant/mol/ODL00000003_100-42-5.mol.gz
'''

b = []
for line in open("3038html.txt"):
	line = line.strip()
	if line != '':	
		if((line[0] == 'h') and line[-1:] == 'z'): #starts http, ends mol.gz
			if(line[46] == 'o'): #is odorant (not receptor)
				b.append(line)
for piece in b:
	print piece # piece[58:] to print only ODL
