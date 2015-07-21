"""Author: John deGuise, Date: 6/10/15

Script takes an input file from a user logging script (file0, file1)
formats the globalid to eliminate odd cases
Splits line into three (2 relevant) parts: 
  globaid, folder size, and a bool if the folder exists
Takes first two pieces, if globalid is a copy, adds folder size to copy's
else, records new pair to dictionary
sorts dict, takes biggest 20 pairs and writes both log results to output_file
"""

import re
import pprint

userdata = dict()
biggest = list()
userdicts = dict()
errorlist = list()

file0 = 'sum_up.log'
file1 = 'sum_up2.log'

def log_parser(input_file):
	with open(input_file) as f:
		
		# everything lowercased
		for line in f:
			line_lower = line.lower()
			
			# formatting what to affect
			if line_lower[:6] != 'parent' and line_lower[:1] != '{' and line_lower[:1] != '-':
				
				# if it's not an empty line, split [0] into key and [1] into value
				if line_lower != '':
					key = line_lower.split(' --> ')[0]
					value = line_lower.split(' --> ')[1]

					# prepping for a duplicate case
					if key not in userdicts.keys():
						userdicts[key] = 0

					# add the duplicate or non-duplicate value
					userdicts[key] = int(value) + userdicts[key]


log_parser(file1)
log_parser(file0)

# print the sorted dictionary as folder size globalid
sorted_dict = sorted(userdicts.iteritems(), key=lambda (k,v): (v,k))

# print the top 20 folder sizes
for key, value in sorted_dict[len(sorted_dict) - 20:]:
	print "%s: %s" % (key, value)

# write to a file of the top 20 to be input for the final output_file.txt
with open('top20_file.txt', 'w+') as f:
	for key, value in sorted_dict[len(sorted_dict) - 20:]:
		f.write("%s: %s\n" % (key, value))

# write to a file of the total 20 biggest from each log
with open('output_file.txt', 'w+') as f:
	for key, value in sorted_dict:
		f.write("%s: %s\n" % (key, value))
