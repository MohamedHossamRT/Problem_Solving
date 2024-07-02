x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
gcd = 0
i = 1
while i <= x and i <= y:
    if x % i == 0 and y % i == 0:
        gcd = i
    i += 1

print(gcd)