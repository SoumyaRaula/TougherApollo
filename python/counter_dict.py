from collections import Counter
lista = [8,1,3,1,4,5,6,3,2]
counter = ((i, lista.count(i)) for i in lista)
print (counter)

dup_count = 0
for items, value in counter:
	print (items, value)
	if value > 1:
		dup_count +=1

print (dup_count)