# activity01
for i in range(1, 11):
    print(f"25 x {i} = {i * 25}")


# activity02
n = int(input("Enter your number: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# activity03
total_sum = sum(range(0, 11))
print("Sum from 0 to 10 is:", total_sum)

n = int(input("Enter your number to check prime: "))

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print("It's not a prime number")