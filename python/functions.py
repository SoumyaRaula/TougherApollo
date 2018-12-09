def function():
	print ("Hello World")

function()

def function(greeting, name = "Cory"):
    print("Hello World : {} {}".format(greeting, name))

function("Soumya", name="Sam")

# Function Unpackaing and Packing
def student(*args, **kwargs):
	print(args)
	print(kwargs)

any_string = ["Hello", "world"]
any_key = {"student":1234}

student(*any_string, **any_key)