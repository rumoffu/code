Working from the website http://mdl.shsmu.edu.cn/ODORactor/module/browse/browse.jsp
we wanted to get all odorant (ligand) molecules.  Because of the poor web design format, we
manually copied the html source from the 61 tabs of odorant molecules into the file
odoractorhtml_3038 which I fixed into 3038html.txt (see "Bonus" exercise at the bottom).

The goals were to: 
1) get a list of links to download all 3038 odorant mol.gz files,
2) get a tab separated list to link the 3038 ODL_cas# to their pubchem_id
3) get a tab separated list to link the pubchem_id to their common_name

1) odor_links.py
# Opens text file "3038html.txt" and extracts ODL file names
# Based on link starting with http and ending with .gz 
'''
ODL00000001_100-06-1.mol.gz
ODL00000002_100-09-4.mol.gz
ODL00000003_100-42-5.mol.gz
ODL00000004_100-46-9.mol.gz
'''


1) take links and links2 and extract pubChem ID
(from http://mdl.shsmu.edu.cn/ODORactor/module/browse/browse.jsp)
all in odoractorhtml_3038 --- modify odor_links.py to print ODL# and pubChem
odl_pubchem.py will do it
actually get_id.py does it..


sirus@sirus-VirtualBox:~/research/html_parse$ python get_id.py > ODL_pubchem.txt

ODL_pubchem.txt
ODL- CAS# \t pubchemid
7370-92-5    110977

2) build list to have all pubchem id
pubchemid_only.py 
# Opens ODL_pubchem.txt that has ODL# \t pubchemid
# will print out pubchemid

sirus@sirus-VirtualBox:~/research/html_parse$ vi pubchemids.txt

has all pubchemids

site_builder.py will take in pubchemids.txt and build 
pubchemid_sites.txt which will be sites for all the pubchemids
http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=66955
http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=110977


3) use pubchem IDs to output pubchem ID + common name to pubchemid_common_name.txt
get_common_name.py
# Opens a file called "pubchemid_sites.txt" in the same directory. 
# opens all sites of that list, and extracts compound name 
# and prints the pubchem ID then a tab then the common name
'''
5365976  allyl alpha-ionone
21149427  CAMPHOLENE ACETATE
643779	citral
7720	2-ethylhexanol
'''


End result:

ODL_pubchem.txt
ODL- CAS# \t pubchemid
7370-92-5    110977

pubchemid_common_name.txt (pubchemid \t common_name)
12777    5-Octanolide
6435876    ST50827384
26333    2-ISOBUTYL-3-METHYLPYRAZINE

sirus@sirus-VirtualBox:~/research/html_parse$ python get_id.py > ODLfull_pubchemid.txt

ODLfull_pubchemid.txt (ODL \t pubchemid)
ODL00000077_103-45-7    7654
ODL00001041_2345-24-6    5365991


Bonus: sed (a text file filter command) and cat (a text outputting command) linux commands exercise:
To convert odoractorhtml_3038 (which had a repeat section and an out of order section) 
to 3038html.txt (html for ODL 1 to 3038 all in order and without repeats)

odoractorhtml_3038:
had ODL 
1 through 2550, 
2651 to 2700, 
2601 to 3038, 
2551 to 2600
for a total of 3088 ODL instead of the actual 3038... it repeated ODL 2651 to 2700

So the task was to: insert 2551 through 2600 and remove 2651 through 2700 (the repeats)

and my (programming?) solution was to:
sed lines 1 to 40790 (ODL 1-2550)
sed lines 48704 to 49488 (ODL 2551-2600)
sed lines 42060 to 48703 (ODL 2601 to 3038)

where the actual commands to consolidate it to 3038html.txt were:
sed -n '1,40790p' odoractorhtml_3038 > part1
sed -n '48704,49488p' odoractorhtml_3038 > part2
sed -n '42060,48703p' odoractorhtml_3038 > part3
cat part1 part2 part3 > 3038html.txt
