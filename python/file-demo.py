with open("text.txt", 'r') as fp:
	content = fp.read(10)
	print(content, end='')
	# while len(content) > 0:
	# 	print('Position {} \n'.format(f.tell()))
	# 	print(content, end='*')
	# 	content = f.read(15)
	fp.seek(0)
	print(content, end='')

import random

phone = f'{random.randint(100, 999)}-555-{random.randint(666, 999)}'
print(phone)



