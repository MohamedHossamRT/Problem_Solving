print("Enter number of apples: ")
n = abs(int(input()))

dozens = 0

while n >= 12:
    dozens += 1
    n -= 12

print(f"{dozens} dozens and {n} apples")

