#script to create tmpl files for chef support in project

import os
import re
import sys

if len(sys.argv) < 2:
	print "please provide directory of properties file. Can be absolute or relative path"
	sys.exit(0)

for paths in sys.argv[1:]:
	listFiles = []
	for (path, dnames, fnames) in os.walk(paths):
		listFiles = [path + "/" + file for file in fnames if re.match(".*\.properties$", file) is not None]
		break
	for file in listFiles:
		print file
		fHandle = open(file)
		filename = file + ".tmpl"
		wHandle = open(filename, 'w')
		for line in fHandle:
			matched  = re.match("^([\S]*)[\s]*=", line)
			if matched is not None :
				wHandle.write(matched.group(1) + "=<%= @" + matched.group(1).replace('.', '_') + " %>\n")
