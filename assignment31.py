# finding factorial of a number using recursion 
def factorial(n):
    if n <2 :
        return 1 
    else:
        return n * factorial(n-1)
print(factorial(5)) # output 120