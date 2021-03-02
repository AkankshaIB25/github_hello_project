# Addition Function
def add(x,y):
	return x+y

# Subtraction Function
def subtract(x,y):
    if x<y:
		return INVALID_INPUTS
	return x-y

#Multiplication Function
def multiply(x,y):
	return x*y

#Division Function
def divide(x,y):
    if y==0:
		return DIVIDE_BY_0_ERROR
	return x/y

#Square Function
def square(x):
	return x*x
	
#Cube Function
def square(x):
	return x*x*x