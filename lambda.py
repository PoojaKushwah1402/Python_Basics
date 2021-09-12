# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

###################
def makeLAmbda(num) :
    return lambda newNum : newNum + num
add2 = makeLAmbda(2)
print(add2(10))