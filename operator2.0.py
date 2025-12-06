# -------- DATA TYPES ----------
name = "Obito"
age = "19"
is_student = "true"
weight = "34.3"

print("your name is", name)
print("the data type of name:", type(name))

print("your age is", age)
print("the data type of age:", type(age))

print("your weight is", weight)
print("the data type of weight:", type(weight))

print("you are student:", is_student)
print("the data type of student:", type(is_student))

print("after type casting")
age = str(age)
weight = float(weight)
is_student = str(is_student)

print("the data type of age:", type(age))
print("the data type of weight:", type(weight))
print("the data type of student:", type(is_student))


# -------- OPERATORS ----------
num1 = 10
num2 = 20

print("Number1 =", num1)
print("Number2 =", num2)

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Modulus =", num1 % num2)
print("Exponent =", num1 ** 2)
print("Floor Division =", num1 // num2)
print("Square root =", num1 ** 0.5)

print("Equal =", num1 == num2)
print("Not Equal =", num1 != num2)


# -------- STRINGS ----------
firstname = "Obito"
lastname = "Uchiha"
fullname = firstname + " " + lastname

print(fullname)
print("multiply firstname 5 times:", firstname * 5)

code = "learning"
print("length of code:", len(code))
print("first letter of firstname:", firstname[0])
print("second letter of lastname:", lastname[1])
print("slice of firstname:", firstname[0:4])


# -------- TWO NUMBER SWAPPING ----------
name = input("Enter your name: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("After swapping two numbers:")
print("num1 =", num1)
print("num2 =", num2)


# -------- THREE NUMBER SWAPPING ----------
print("\n--- 3 Number Swapping ---")

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

print("Before swapping:")
print("n1 =", n1)
print("n2 =", n2)
print("n3 =", n3)

# Swapping using temp variable
temp = n1
n1 = n2
n2 = n3
n3 = temp

print("After swapping:")
print("n1 =", n1)
print("n2 =", n2)
print("n3 =", n3)
