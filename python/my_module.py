print ("Imported by my_module...")

test = 'Test String'

def find_index(to_search, target):
	''' Finds the index of the given target to search'''
	for i, value in enumerate(to_search, start=1):
		if value == target:
			return i

	return -1