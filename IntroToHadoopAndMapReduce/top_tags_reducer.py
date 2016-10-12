import sys

def reducer(stdin):

	last_tag = None
	count = 0

	tags = []

	for line in stdin:
	    data_mapped = line.strip().split("\t")
	    
	    if len(data_mapped) != 2:
	        continue

	    tagname, node_id = data_mapped

	    if last_tag and last_tag != tagname:
	    	tags.append((count, last_tag))

	    	count = 0
	        last_tag = tagname


	    count += 1
	    last_tag = tagname

	if last_tag != None:
		tags.append((count, last_tag))

	tags.sort()
	tags = tags[::-1][:10]
	for count, item in tags:
		print "{0}\t{1}".format(item, count)


if __name__ == '__main__':
	reducer(sys.stdin)