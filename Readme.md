
This module allows to extract bibtex entry from NASA ADS using bibcode entries.
This will also asign the citealias. 
Useful for managing references with bibcode than bibtex file as a whole.


============= Pre-requisite ===============

You need following python modules

beautifulsoup4 (can be installed using pip install beautifulsoup4), urllib2

============= Installation ===============

1) Copy the folder in your machine.

2) cd to that directory

3) run installation.sh shell file. Make it executable if needed

4) This will create a dir named '.github_extras/auto_bibtex_download' in your home folder
This directory contains the file Auto_bibtex_copy.py

5) The above script will also create shell function auto_bibtex_download
If needed change it from path/to/your/home/.github_extras/bash_functions.sh file

================ Usage ==================

6) Create your own bibcode entry file which has syntax as follows

# column-1 -->> bibcode
# column-2 -->> citealias
# column-3 -->> Comment e.g. (why do you cite this paper) 
A sample config file is attached.
The file must have .config as extension. Note Strings starting with # are ignored

7) Now use the following commands to download the bibtex entries

auto_bibtex_download sample.config

This will download all the bibcode entries

To download from 2 to 4 bibcode entries use command

auto_bibtex_download sample.config 2 4

To download from 3 to last bibcode entry use command

auto_bibtex_download sample.config 3

To download up to 4th bibcode entry use command

auto_bibtex_download sample.config 1 4


================ License ==================

Written by Prakash Gaikwad 

GNU GENERAL PUBLIC LICENSE see license.txt









