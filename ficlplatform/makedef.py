###
### makedef.py
### Generates a simple .DEF file for Ficl,
### based on a text file containing all exported symbols.
###
### Contributed by Larry Hastings.
###

import string
import time

f = open("ficlexports.txt", "rt")
output = open("../src/ficldll.def", "wt")
counter = 1

print >> output, ";;;"
print >> output, ";;; Generated by makedef.py at " + time.strftime("%Y/%m/%d %H:%M:%S")
print >> output, ";;;"
print >> output, ""
print >> output, "EXPORTS"
print >> output, ""
for a in f.readlines():
	a = string.strip(a)
	if len(a) == 0:
		continue
	print >> output, a + " @" + str(counter)
	counter += 1

print >> output, ""
print >> output, ";;; end-of-file"
print >> output, ""
f.close()
output.close()
