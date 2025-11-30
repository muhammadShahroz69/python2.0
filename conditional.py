# EVEN / ODD CHECK
number = int(input("Enter any number: "))
print("Number is", number)

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# BMI CALCULATOR
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height / 100) ** 2

print("The BMI index is", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")


# NUMBER CHECK (GREATER THAN 50 & EVEN/ODD)
num = int(input("Enter your number: "))

if num > 50:
    print("The number is greater than 50")
    if num % 2 == 0:
        print("The number is even too")
    else:
        print("The number is odd too")
else:
    print("The number is less than 50")


# DATE AND TIME
import datetime
current_Time = datetime.datetime.now()
print("The date and time is", current_Time)

# CALENDAR
import calendar
print(calendar.calendar(2025))