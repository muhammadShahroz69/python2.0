print("--- EXAM RESULT SYSTEM ---")

name = input("Enter your name: ")
marks = int(input("Enter your marks out of 100: "))

print("Student Name:", name)
print("Marks:", marks)

if marks < 50:
    print("Result: FAIL")
else:
    print("Result: PASS")