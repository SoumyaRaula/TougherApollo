class MyException(Exception):
	pass

try:
	hello = 5
	print(hello/3)

	if hello:
		raise MyException("This is my exception")
except ZeroDivisionError as e:
	print (f'Exception occured {e}')

except MyException as e:
	print (e)
else:
	print ("Success")
finally:
	print('This always prints')