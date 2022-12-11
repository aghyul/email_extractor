#1/usr/bin/env python
# coding: utf-8
# feel free to use my code , J already i use someone else (Stack OverFlow ) Code
# User : 4chano
    # hack the fucking world

from optparse import OptionParser
import os.path
import time
import re


regex = re.compile(("([a-z0-9!#$%&*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def file_to_str(filename):
    """Returns the contents of filename as a string."""
    with open(filename) as f:
        return f.read().lower() 

def get_emails(s):
    """Returns an iterator of matched emails found in string s."""
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def add_to_file(myFile, email):
	"""Save in a text file the emails extracted """
	with open(myFile,"a") as emailsfile:
            emailsfile.write(email+",")
	
if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    # No options added yet. Add them here if you ever need them.
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isfile(arg):
            # create file to export emails
            extensionTime = time.strftime("%H%M%S")
            myFile = "emailList_"+extensionTime+".txt"
            # regex emails
            for email in get_emails(file_to_str(arg)):
                print (email)
                add_to_file(myFile, email)

        else:
            print ('"{}" is not a file.'.format(arg))
            parser.print_usage()
