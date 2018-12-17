def square_number(nums):
	for i in nums:
		yield (i*i)

my_nums = square_number([1,2,3,4,5])

for i in my_nums:
	print (i)