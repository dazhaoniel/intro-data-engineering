import sys, csv, re

def mapper(stdin):
	remove_list = ".,!?:;\"()<>[]#$=-/"

	reader = csv.reader(stdin,delimiter='\t')

	# Skip column names
	next(reader)

	for line in reader:
		if len(line) == 19:
			node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line

			test = body.split(" ")
			p = re.compile(r'<.*?>')

			for item in test:
				item = p.sub('', item)
				# print item
				for char in remove_list:
					item = item.replace(char, "").lower()


				print "{0}\t{1}".format(item, node_id)


if __name__ == '__main__':
	mapper(sys.stdin)