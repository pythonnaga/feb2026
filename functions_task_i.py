# # Add Function : 
# # Write a Python function named add that takes two arguments a and b and returns their sum.

def add(a,b):
    return a+b

a = int(input("Enter the First Number :"))
b = int(input("Enter the second Number :"))
result = add(a,b)
print(f"Sum of the two numbers  :", result)
print("-"*35)
print("\n")

# # Square Function : 
# # Write a Python function named square that takes a number x as input and returns its square.

def square(i):
    return i*i
a = int(input("Enter the number to get square  :",))

result = square(a)
print(f"Square of the given number is :   ",result)
print("-"*35)
print("\n")


# # Factorial Function :
# # Write a Python function named factorial that takes a positive integer n as input and returns its factorial.

def factorial(n):
    if n ==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter the number to find Factorial:    "))
print(f"Factorial of the given number is ",factorial(num))
print("-"*35)
print("\n")



# # Maximum Function :
# # Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.

def maximum(num):
    return max(num)

num =[25,65,78,95,1250]
print("Maximum Value from the given list is     ", max(num))
print("-"*35)
print("\n")

# # Reverse Function :
# # Write a Python function named reverse that takes a string s as input and returns its reverse.

def reverse(i):
    return i[::-1]
i = input("Enter the String to be reveresed :    ")
print("Reversed String is :    ",reverse(i))
print("-"*35)
print("\n")

# # Check Prime Function :
# # Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n): 
        if n % i == 0:
            return False
        return True
    
n=int(input("enter the number is :"))
print(f"Given number is :",is_prime(n))

print("-"*35)
print("\n")

# Fibonacci Function :
# Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number.

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
num = int(input("Enter the number :   "))
print("Fibonacci : ", fibonacci(num))
print("-"*35)
print("\n")


# Palindrome Function :
# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .

def parlindrome (p):
    p = p.lower()
    return p == p[::-1]
print(parlindrome("rishi"))
print(parlindrome("Gana"))
print(parlindrome("eye"))
print("-"*35)
print("\n")

# Sum of Squares Function :
# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.

def sum_squares(n):
    total = 0
    for num in n:
        total += num **2
    return total
n=(5,8,9,10,25,35)
print("sum of square numbers :   ",sum_squares(n))

print("-"*35)
print("\n")

# Average Function :
# Write a Python function named average that takes a list of numbers as input and returns the average value.

def average(num):
    if len(num) == 0:
        return 0
    return sum(num) / len(num)

num_list = [20, 40, 80, 120, 100]
result = average(num_list)
print("Average:", result)

print("-"*35)
print(".......Functions Task Completed........")
print("\n")