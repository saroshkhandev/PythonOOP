n = int(input("Enter 4 digit number: "))

c = 0
sum = 0

for i in range(1, 5):
    d = n % 10
    c += 1
    if c == 1 or c == 4:
        sum += d
    n = n // 10

print("Sum of 1st and 4th digit is: ", sum)
