get_common_name.py opens list and prints out common name, 1 per line

odor_links.py opens list2 and prints out all 
http://mdl.shsmu.edu.cn/ODORCommon/datasource/odorant/mol/ODL00002600_7492-39-9.mol.gz


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


3) get_common_name.py will take in pubchemid_sites.txt and  print out pubchem ID + common name to pubchemid_common_name.txt
pubchemid_common_name.txt (pubchemid \t common_name)
12777    5-Octanolide
6435876    ST50827384
26333    2-ISOBUTYL-3-METHYLPYRAZINE

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
