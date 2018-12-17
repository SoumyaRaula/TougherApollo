
# Complete the maxDifference function below.
def maxDifference(a):
    max_diff_in_array = -1
    diff_compute_array = []
    size_of_array = len(a)
    
    if not size_of_array > 1:
        return max_diff_in_array
    
    if size_of_array == 2:
        max_diff_in_array = a[1] - a[0] if (a[1] > a[0]) else -1
        return max_diff_in_array

    def return_value(size_of_array):
    	for value in range(1, size_of_array):
    		yield value 

    for value in return_value(size_of_array):
        for curr_index in range(0, value):
            if a[curr_index] < a[value]:
            	diff_compute_array.append(a[value] - a[curr_index])
            else:
            	continue

    print(max(diff_compute_array))


print (maxDifference([2,1]))