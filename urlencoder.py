#!/usr/bin/python

import sys
import urllib
import urllib.parse

sys.argv.pop(0)	
length = len(sys.argv)
args = str(sys.argv)
	
print ("Number of arguments: {} arguments".format(length))
print ("Argument List: {}".format(args))

query = ' '.join(sys.argv)

print(urllib.parse.quote(query))