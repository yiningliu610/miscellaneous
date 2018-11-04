import sys

def mapper():
	for line in sys.stdin:
		line = line.strip()
		for word in line.split():
			print '%s\t%s' %(word, 1)

mapper()