import sys, csv
from datetime import datetime

def mapper(stdin):
	reader = csv.reader(stdin,delimiter='\t')

	# Skip column names
	next(reader)


	for line in reader:
		if len(line) == 19:
			node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

			# 2012-02-22 21:36:17.077627+00
			dates = added_at.split(".")
			time = datetime.strptime(dates[0],'%Y-%m-%d %H:%M:%S')

			print "{0}\t{1}".format(author_id, time.hour)


if __name__ == '__main__':
	mapper(sys.stdin)