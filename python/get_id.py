'''
'''
#testfile = open("links")
#line = testfile.readline()
b = []
#while line != '':
for line in open("odoractorhtml_3038"):
	line = line.strip()
	if line.find("cgi") != -1:
		b.append(line)
	if line != '':	
		if((line[0] == 'h') and line[-1:] == 'z'):
			if(line[46] == 'o'):
				b.append(line)
match = set()
s = ""
for piece in b:
	cid = piece.find("cid=")
	loc = piece.find("&loc")
	odl = piece.find("ODL")
	gz = piece.find("gz")
	if cid != -1:#pubchem
		s += piece[cid+4:loc]
		match.add(s)
		s = ""
	else:#odoractor
		s += piece[odl:gz-5]
		s += '\t'

for m in match:
	print m

'''
'''
'''
testfile = open("phix.fa")
skip = testfile.readline() #skip first line
a = testfile.readlines()
b = []
for i in a:
	b.append(i.strip())
t = ''.join(b)
for letter in t:
	print letter

'''
'''
b = []
testfile = open("reads.txt")
for i in xrange(3600+1):
	lin = testfile.readline()
	if i == 3459:
		b.append(lin.strip())
t = ''.join(b)
print t
'''
