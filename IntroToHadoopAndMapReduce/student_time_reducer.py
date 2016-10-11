import sys

def reducer(stdin):

	active_hours = [0] * 24
	last_author_id = None

	for line in stdin:
	    data_mapped = line.strip().split("\t")
	    
	    if len(data_mapped) != 2:
	        continue
	    
	    author_id, added_at = data_mapped

	    if last_author_id and last_author_id != author_id:     
	        most_active_hour_posts = max(active_hours)
	        
	        for hour, post_count in enumerate(active_hours):
	            
	            if post_count == most_active_hour_posts:
	                
	                print "{0}\t{1}".format(author_id, hour)
	                
	                active_hours = [0] * 24

	    active_hour = int(added_at)
	    active_hours[active_hour] += 1
	    last_author_id = author_id


	most_active_hour_posts = max(active_hours)	
	for hour, posts_count in enumerate(active_hours):
	    
	    if posts_count == most_active_hour_posts:
	        
	        print "{0}\t{1}".format(author_id, hour)



if __name__ == '__main__':
	reducer(sys.stdin)