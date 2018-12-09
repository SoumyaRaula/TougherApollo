from functools import reduce
nums = [1,1,2,2,3,4,5,6,7,8]

my_nums = {n for n in nums}
print(my_nums)

my_list = list(map(lambda n: n*n , nums))
print('my map {}'.format(my_list))

my_filter = list(filter(lambda n : n%2 == 0, nums))
print('my filter {}'.format(my_filter))

my_reduce = reduce(lambda n,y : n+y, nums)
print('my reduce {}'.format(my_reduce))

names = ["a", "b", "c"]
heroes = [1,2,3]

my_string = [(letter, names) for letter, names in zip(names, heroes)]
print (my_string)

my_dict = {letter: names for letter, names in zip(names, heroes)}
print (my_dict)

my_dict = {letter: names for letter, names in zip(names, heroes)}
print (my_dict)