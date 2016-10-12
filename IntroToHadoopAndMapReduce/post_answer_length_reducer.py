import sys, numpy

def reducer(stdin):

	answers = []

	last_node_id = None
	last_len_body = 0

	for line in stdin:
	    data_mapped = line.strip().split("\t")
	    
	    if len(data_mapped) != 3:
	        continue
	    
	    node_id, len_body, node_type = data_mapped

	    if last_node_id and last_node_id != node_id:
	    	avg_len_answer = 0
	    	if answers:
	    		avg_len_answer = numpy.mean(answers)
	    	print "{0}\t{1}\t{2}".format(last_node_id, last_len_body, avg_len_answer)

	    	answers = []
	        last_node_id = node_id
	        if node_type == 'question':
	        	last_len_body = len_body


	    if node_type == 'answer':
	    	answers.append(int(len_body))
	    else:
	    	last_len_body = len_body
	    last_node_id = node_id

	avg_len_answer = 0
	if answers:
	    avg_len_answer = numpy.mean(answers)
	print "{0}\t{1}\t{2}".format(last_node_id, last_len_body, avg_len_answer)


if __name__ == '__main__':
	reducer(sys.stdin)