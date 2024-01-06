# https://ocw.mit.edu/courses/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/231bd0995d90626f2d7e2ad223fa7eea_MIT6_189IAP11_rec_problems.pdf
#1. Write a function that takes in two numbers and recursively multiplies them together
'''
def mul(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a + mul(a, b-1)
print(mul(11,2))'''


#2. Write a function that takes in a base and an exp and recursively computes base^exp. You are not allowed to use the ** operator!
'''
def power(base, exp):
    if exp == 0:
        return 1
    elif base == 0:
        return 0
    else:
        return base * power(base, exp-1)
print(power(4,3))'''


#3. Write a function using recursion to print numbers from n to 0.
'''
def num(n):
    if n <= 0:
        return n
    else:
        print(n)
        num(n-1)
num(5)'''


#4. Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program of problem 1).
'''
def nums(current,n):
    if current > n:
        return
    else:
        print(current)
        nums(current+1, n)
nums(0,5)'''


#5. Write a function using recursion that takes in a string and returns a reversed copy of the string. The only string operation you are allowed to use is string concatenation.
'''
def reverse(string):
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string
    else:
        return string[-1] + reverse(string[:-1])
print(reverse("Mohit"))'''


#7. Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation
''' 
def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))'''


#https://www.classes.cs.uchicago.edu/archive/2017/fall/12100-1/pp/bac-recursion.html
# Warm-up exercise #1: What is the output of the following code?
'''def mystery(a, b, c, d):
  if c == 0:
    return d
  elif c % 2 == 0:
    return b + mystery(a, b, c - 2, d)
  else:
    return a + mystery(a, b, c - 1, d)

print("Warmup Exercise #1")
print(mystery("x", "y", 6, "z"))
print(mystery("x", "y", 5, "z"))
print()'''

'''
SOLUTION 1:

For the first print statement that is ("x", "y", 6, "z")
It goes like this:
b + mystery(a,b,4,d)
b + mystery(a,b,2,d)
b + mystery(a,b,0,d) as hits 0 so in the next iteration it will satisfy first if statement
d
So - b+b+b+d -> yyyz

For the second statenent ("x", "y", 5, "z")
It goes like this:
a + (a,b,4,d)
b + (a,b,2,d)
b + (a,b,0,d) again hits 0 so will go in 1st if statement
d
So - a+b+b+d -> xyyz
'''
