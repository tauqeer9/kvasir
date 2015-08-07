#!/usr/bin/env 
# by Kevin Bonham, PhD (2015)
# for Dutton Lab, Harvard Center for Systems Biology, Cambridge MA
# CC-BY

'''
- Create directories `path/input/` and `path/output/`
- Put genbank files into `path/input/`
- Must have Mongod running, in terminal: `mongod --dbpath path/to/db`
- run `python run_kvasir.py [run_name]` from `path/`
'''

import os
import sys
import DataImport, FixGbk, MakeBlastDB, KvasirBlast
from get_outputs import get_outputs
from KvDataStructures import mongo_init, reset_database

print 'Here we go!'

gbk_folder = os.path.abspath('input/')
exp_name = sys.argv[1]

mongo_init(exp_name)
reset_database(exp_name)

check_file_names = str(raw_input("Manually enter species names? [y/n]"))
if check_file_names == 'y':
    check_file_names = True
elif check_file_names == 'n':
    check_file_names = False
else:
    "Must enter 'y' or 'n', start over"
    break

new_folder = 'output/{0}/'.format(exp_name)
if not os.path.isdir(new_folder):
   os.makedirs(new_folder)
os.chdir(new_folder)

print 'Checking and importing files...'
for the_file in os.listdir(gbk_folder):
    path_to_file = '{0}/{1}'.format(gbk_folder, the_file)
    if the_file.endswith('.gb'):
        print 'Checking {0}'.format(the_file)

        validated_file = FixGbk.validate_gbk(path_to_file, check_file_names)       

        if validated_file:
            print 'Importing {0}'.format(the_file)
            DataImport.import_file(validated_file)
        else:
            print 'moving on...'
    else:
        print '{0} is not a valid genbank file, skipping'.format(the_file)

KvasirBlast.make_blast_db()
KvasirBlast.blast()
KvasirBlast.blast_to_db()
get_outputs()

