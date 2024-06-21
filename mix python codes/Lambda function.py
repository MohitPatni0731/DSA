# Write a lambda function that takes two numbers and returns their sum
x = key=lambda a,b : a + b 
print(x(5,3))

# Use a lambda function with builtin function map to convert a list of integers to their squares
array = [1,2,3,4,5]
y = map(key=lambda x: x**2, array)
print(list(y))

# Use a lambda function with built in function filter to get all the even numbers from a list
array = [1,2,3,4]
z = filter(lambda x: x%2==0, array)
print(list(z))

# Use a lambda function to sort a list of tuples by the second element
tuple_ = [(1,7), (2,3), (3,4)]
a = sorted(tuple_, key=lambda x: x[1])
print(a)

# Sort a list of strings in a case-insensitive manner
array = ['banana', 'Apple', 'cherry', 'Date']
a = sorted(array, key=lambda x: x.lower())
print(a)
