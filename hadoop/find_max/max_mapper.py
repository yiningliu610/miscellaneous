import sys

def mapper():
	for line in sys.stdin:
		line = line.strip()
		# print line.split('\t')
		# for word in line.split():
		# 	print '%s\t%s' %(word, 1)
		info = line.split('\t')
		print '%s\t%s' %(info[0], info[2])

mapper()