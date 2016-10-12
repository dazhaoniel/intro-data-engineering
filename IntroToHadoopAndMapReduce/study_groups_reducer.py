import sys

def reducer(stdin):

	students = []

	last_node_id = None

	for line in stdin:
	    data_mapped = line.strip().split("\t")
	    
	    if len(data_mapped) != 2:
	        continue
	    
	    node_id, author_id = data_mapped

	    if last_node_id and last_node_id != node_id:
	    	print "{0}\t{1}".format(last_node_id, students)

	    	students = []
	        last_node_id = node_id

	    students.append(author_id)
	    last_node_id = node_id


	if last_node_id != None:
	    print "{0}\t{1}".format(last_node_id, students)


if __name__ == '__main__':
	reducer(sys.stdin)