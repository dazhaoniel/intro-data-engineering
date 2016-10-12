import sys, csv

def mapper(stdin):
	reader = csv.reader(stdin,delimiter='\t')

	# Skip column names
	next(reader)


	for line in reader:
		if len(line) == 19:
			node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

			if node_type and node_type == 'question':
				print "{0}\t{1}".format(node_id, author_id)
			else:
				print "{0}\t{1}".format(abs_parent_id, author_id)


if __name__ == '__main__':
	mapper(sys.stdin)