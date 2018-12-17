class Duck:
	def quacks(self):
		print('Quack!!!!')
	def fly(self):
		print('Flap!!!!')

class Person:
	def quacks(self):
		print('I can Quack!!!!')
	def fly(self):
		print('I can Flap my arms!!!!')

# Non Pythonic Way to this
# def quack_and_fly(thing):
# 	if isinstance(thing, Duck):
# 		thing.quacks()
# 		thing.fly()
# 	else:
# 		print('This has to be Human!!!')

# 	print()

def quack_and_fly(thing):
	try:
		thing.quacks()
		thing.fly()
		thing.bark()
	except AttributeError as e:
		print('Exception {}'.format(e))

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)