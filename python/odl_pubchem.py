'''
'''
#testfile = open("links")
#line = testfile.readline()
b = []
#while line != '':
for line in open("links"):
	line = line.strip()
	if line != '':	
		if((line[0] == 'h') and line[-1:] == 'z'):
			if(line[46] == 'o'):
				b.append(line)
for piece in b:
	print piece[58:]#print only ODL

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
