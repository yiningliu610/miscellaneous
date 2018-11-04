import sys

def word_count():
	key, count = None, 0
	for line in sys.stdin:
		line = line.strip()
		if not key:
			key, count = line.split('\t')
			count = int(count)

		elif key != line.split()[0]:
			if key:
				print '%s\t%s' %(key, count)
			key, count = line.split()
			count = int(count)
		else:
			count = count + 1
	print '%s\t%s' %(key, count)

word_count()

