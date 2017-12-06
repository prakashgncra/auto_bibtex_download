import urllib2  # the lib that handles the url stuff
import os
import subprocess
import sys
from bs4 import BeautifulSoup as bs
import urlparse, urllib


def __MAIN__():
	if len(sys.argv) == 1:
		print "Need name of the config file ... "
		print "Exiting the code now ... "
		exit()
	elif len(sys.argv) == 2:
		config_file	=	str(sys.argv[1])
		indx_start	=	0
		indx_end	=	0
	elif len(sys.argv) == 3: 
		config_file	=	str(sys.argv[1])
		indx_start	=	int(sys.argv[2])
		indx_start	-=	1
		indx_end	=	0
	elif len(sys.argv) == 4: 
		config_file	=	str(sys.argv[1])
		indx_start	=	int(sys.argv[2])
		indx_end	=	int(sys.argv[3])
		indx_start	-=	1	
	

	tmp_filename		=	"uvb.tmp"
	bib_filename		=	config_file.replace(".config",".bib")
	bibcode,bib_alias	=	 READ_BIBCODE_FILE(config_file)
	if indx_end			==	0: indx_end = len(bibcode)

	for indx in xrange(indx_start,indx_end):
		EXTRACT_BIBTEX_ENTERY(bibcode[indx],bib_alias[indx],tmp_filename)
		print "Data Extracted ...",bibcode[indx],bib_alias[indx].strip(),"Total Entries :",len(bibcode),"Job Done for :",indx+1

	DELETE_EXTRA_STUFF(tmp_filename,bib_filename)


def EXTRACT_BIBTEX_PAGE_LINK_FROM_TEXT(bibcode): # Very Important Code
	soup = bs(urllib.urlopen('http://adsabs.harvard.edu/abs/' + bibcode))
	kounter = 0
	for link in soup.findAll('a'):
		if link.contents == ['Bibtex entry for this abstract']:
	   		return link.attrs['href']	
	
def EXTRACT_BIBTEX_ENTERY(bibcode,bib_alias,tmp_filename):	
	#url 		=	'http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=' + bibcode + '&data_type=BIBTEX&db_key=AST&nocookieset=1'
	url 		=	EXTRACT_BIBTEX_PAGE_LINK_FROM_TEXT(bibcode)
	data 		= 	urllib2.urlopen(url) # it's a file like object and works just like a file
	filename	=	open(tmp_filename,"a")
	for line in data: # files are iterable
		filename.write(line)
	filename.close()	
	REPLACE_BIBCODE_WITH_ALIAS(tmp_filename,bibcode,bib_alias)
			
def READ_BIBCODE_FILE(filename):
	bibcode		= 	[]
	bib_alias	=	[]
	with open(filename, "r") as f:         
		for line in f.readlines():
			li = line.lstrip()
			if not li.startswith("#"):
				if li.strip()!='':
					bibcode.append(li[:19])
					hash_loc	=	li.find("#")
					bib_alias.append(li[20:hash_loc].replace(" ",""))
	return bibcode,bib_alias

def DELETE_EXTRA_STUFF(input_file,output_file):
	output		=	open("mYtEmP.txt","w")
	input_obj	=	open(input_file,"r")
	for i, line in enumerate(input_obj):
		if line.startswith('Query') or line.startswith('Retrieved'):
			continue
		else:
			output.write(line)	
	output.close()
	subprocess.call("grep -v '^$' mYtEmP.txt > " + output_file,shell=True)	
	os.remove("mYtEmP.txt")	
	os.remove(input_file)
	
	
def REPLACE_BIBCODE_WITH_ALIAS(filename,bibcode,bib_alias):
	# Read in the file
	filedata = None
	with open(filename, 'r') as file :
	  filedata = file.read()

	# Replace the target string
	filedata = filedata.replace("{" + bibcode + ",", "{" + bib_alias.strip() + ",")

	# Write the file out again
	with open(filename, 'w') as file:
	  file.write(filedata)

		
__MAIN__()





	
	
	
	
	
