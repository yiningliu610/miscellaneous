import sys

def reducer():
	current_key, max_temp = None, None
	for line in sys.stdin:
		line = line.strip()
		key, temp = line.split('\t')
		temp = int(temp)

		if not current_key:
			current_key = key
			max_temp = temp

		elif current_key != key:
			print '%s\t%s' %(current_key, max_temp)
			current_key = key
			max_temp = temp

		else:
			if max_temp <= temp:
				max_temp = temp
	print '%s\t%s' %(key, max_temp)
reducer()

