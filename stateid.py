#This shifts the compound_id to 3039 and also tracks tautomers with a state id
#now 3869 to move past old ones
count = 3869
#compounds = open('jeninitialcompounds_halfcompounds.csv', 'w')
#states = open('jeninitialcompounds_state.csv', 'w')
nameid_dict = {}
nametautomer_dict = {}
#write all except tautomer
with open('jeninitialcompounds_clean.csv', 'r') as inp:
  all = inp.readlines()
  for line in all:
    newline = line.split('\t')
    smile = newline[1]
    state_id = str(0) #default
    c_name = newline[4] #the common name
    response = newline[5]
    c_id = count #start at count and reassign if tautomer
    tautomer = 'F' #default F
    unique = True
    if '@' in c_name: #tautomer
      namesplit = c_name.split('@')
      c_name = namesplit[0]
      state_id = namesplit[1]
      tautomer = 'T'
      if c_name in nameid_dict:
        c_id = nameid_dict[c_name] #get the id
        count = count - 1
        unique = False
      else: 
        print 'Error in %s %s but c_id and count will be fine. Continuing.' % (c_name, state_id)
    nameid_dict[c_name] = c_id
    nametautomer_dict[c_name] = tautomer
    if unique: #compound_id must be unique for initialcompounds
      compounds.write(str(c_id) + '\t' + smile + '\tnull\tnull\t' + c_name + '\t' + response + '\tnull\n')
    states.write(str(c_id) + '\t' + state_id + '\t' + smile + '\n')
    count = count + 1 #set to new id, if tautomer, resume at old count by incrementing back

compounds.close()
states.close()
#write in tautomer and ending 3 parts
halfcompounds = open('jeninitialcompounds_halfcompounds.csv', 'r')
fullcompounds = open('jeninitialcompounds_uniquefullcompounds.csv', 'w')
halflines = halfcompounds.readlines()
for line in halflines:
  c_name = line.split('\t')[4]
  fullcompounds.write(line.strip() + '\t' + nametautomer_dict[c_name] + '\tsdf_fn\tsmi_fn\tcompound_dir\n')
fullcompounds.close()
