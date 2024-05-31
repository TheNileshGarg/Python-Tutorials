# Lambda functions 

#def square(x):
#    return x*x


square = lambda x : x*x
cube = lambda x: x*x*x 
avg = lambda x,y : (x+y)/2

print(square(5))
print(cube(5))
print(avg(3,4))

# Lambda functions are used when you have function with simple logic 
# It is mainly used when we need to pass function as an argument 

# Example 

def ex(fx, value):
    return 10 + value + fx(value)

print(ex(lambda x : x*x*x + 10*x, 3))