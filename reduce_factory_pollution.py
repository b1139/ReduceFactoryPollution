def reduce_pollution(A):
	expected_pollution = sum(A)/2
	filter_count = 0
	total_pollution = sum(A)
	A.sort(reverse=True)

	# If the factories have the same number of pollution
	# Then to reduce it half one filter each respectively is enough 
	if len(set(A)) == 1:
		return len(A)

	# Once the Total pollution is reduced below or equal to half the loop ends
	while total_pollution > expected_pollution:
		curr_val = A.pop(0)/2
		A.append(curr_val)
		# The highest pollution always get divided
		A.sort(reverse=True)
		filter_count += 1
		total_pollution -= curr_val
		
	return filter_count
