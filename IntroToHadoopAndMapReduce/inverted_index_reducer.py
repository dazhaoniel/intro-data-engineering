import sys


def reducer(stdin):
	wordTotal = 0
	oldKey = None

	f = open('out_final.txt', 'w')

	for line in stdin:
		data_mapped = line.strip().split("\t")

		if len(data_mapped) != 2:
			continue

		word, node_id = data_mapped

		if oldKey and oldKey != word:
			# print oldKey, "\t", wordTotal
			f.write( "{0}\t{1}\n".format(oldKey, wordTotal) )
			
			oldKey = word
			wordTotal = 0

		oldKey = word
		wordTotal += 1

	if oldKey != None:
		# print oldKey, "\t", wordTotal
		f.write( "{0}\t{1}\n".format(oldKey, wordTotal) )

	f.close()

if __name__ == '__main__':
	reducer(sys.stdin)