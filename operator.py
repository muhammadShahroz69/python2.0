name="Obito"
age="19"
is_student="true"
weight="34.3"
print("your name is",name)
print("the data type of name",type(name))
print("your age is",age)
print("the data type of age",type(age))
print("your weight is",weight)
print("the data type of weight",type(weight))
print("your are student",is_student)
print("the data type of student",type(is_student))     
print("after type casting")
age=str("age")
weight=int("weight")
is_student=str("is_student")
print("the data type of age",type(age))
print("the data type of weight",type(weight))
print("the data type of student",type(is_student))

#operAtor in python

num1=10
num2=20
print("Number1",num1)
print("Number2",num)
print("Addition",num1+num2)
print("Substraction",num1-num2)
print("Multiplication",num1*num2)
print("Division",num1/num2)
print("Modulus",num1%num2)
print("Exponent",num1**2)
print("Floor Division",num1/num2)
print("Square root",num1*0.5)
print("Equal",num1==num2)
print("Not Equal",num1!=num2)

firstname="Obito"
lastname="Uchiha"
fullname=firstname+" "+lastname
print(fullname)
print("multiply name 5 times",firstname*5)
code ="learning"
print("length of this code",len(code))
print("first name id",firstname[0])
print("last name id",lastname[1])
print("slice of string",firstname[0:4])


name=input("Enter your name")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
temp=num1
num1=num2
num2=temp
print("after swaping")
print("numb1",num1)
print("numb2",num2)