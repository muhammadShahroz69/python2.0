# simple functions + calculator + factorial + armstrong check
def printHello():
    print("hello world")

def printName(name):
    print("Hello, The name is", name)

def add(num1, num2):
    return num1 + num2

def introName(name):
    print("Hello, The Name is", name)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

def is_armstrong(n):
    """Return True if n is an Armstrong number (n == sum of its digits**len)."""
    s = str(n)
    power = len(s)
    total = 0
    for ch in s:
        total += int(ch) ** power
    return total == n

def list_armstrong_upto(limit):
    """Return a list of Armstrong numbers from 0..limit (inclusive)."""
    result = []
    for i in range(limit + 1):
        if is_armstrong(i):
            result.append(i)
    return result


# ----------------- run the things -----------------

# 1) hello + name
printHello()
printName("Obito")

# 2) simple add example
print("the sum is", add(10, 12))

# 3) intro with input
inputname = input("Enter your name: ")
introName(inputname)

# 4) factorial
n = int(input("Enter a number to compute factorial: "))
print("Factorial of", n, "is", factorial(n))

# 5) basic calculator (4 ops)
x = int(input("Enter a number (x): "))
y = int(input("Enter another number (y): "))

print("the addition is", add(x, y))
print("the subtraction is", subtract(x, y))
print("the multiply is", multiply(x, y))
div_res = divide(x, y)
if div_res is None:
    print("the divide is: Error (division by zero)")
else:
    print("the divide is", div_res)

# 6) Armstrong check for one number
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")

# 7) Optional: show all Armstrong numbers up to a limit
limit = int(input("Enter an upper limit to list Armstrong numbers (e.g. 1000): "))
armstrongs = list_armstrong_upto(limit)
print("Armstrong numbers up to", limit, ":", armstrongs)