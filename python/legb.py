'''
LEGB 
Local, Enclosing, Global , Built-In
'''

#x = 'global x'

def test():
	y = 'local y'
	print (x)

x = "Under Global X"
test()