with open("file-test.txt", 'r') as fp:
	content = fp.read(10)
	print(content)
	fp.seek(2,0)
	content = fp.read()
	print(content)
import random

phone = f'{random.randint(100, 999)}-555-{random.randint(666, 999)}'
print(phone)



