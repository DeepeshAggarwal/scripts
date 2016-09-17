#script to create properties files for chef support

import os
import re

if len(sys.argv) < 2:
	print "please provide directory of properties file. Can be absolute or relative path"
	sys.exit(0)

for paths in sys.argv[1:]:
	listFiles = []
	for (path, dnames, fnames) in os.walk(paths):
		listFiles = [path + "/" + file for file in fnames if re.match(".*\.properties$", file) is not None]
		break
	wHandle = open(paths + '/new.properties', 'w')
	for file in listFiles:
		print file
		fHandle = open(directory + file)
		for line in fHandle:
			matched  = re.match("^([\S]*?)[\s]*=[\s]*([\S]*)", line)
			print matched.group(1).replace('.', '_')
			if matched is not None :
				wHandle.write("\"" + matched.group(1).replace('.', '_') + "\":\"" + matched.group(2) + "\",\n")
