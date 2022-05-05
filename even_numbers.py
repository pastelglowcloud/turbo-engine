def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1):
		if x % 2 == 0:
			return_string += str(x) + " "
	return return_string.strip()