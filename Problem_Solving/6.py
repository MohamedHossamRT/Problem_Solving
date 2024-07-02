from math import pi,pow,factorial

print("Enter x in degrees:")
x = float(input())
x *= pi/180

print("Enter number of terms:")
n = int(input())

sinx = 0.0
i = 1
counter = 0
sign = 0

while counter < n and i <= 12:
    sinx += (pow(x,i) / factorial(i)) * pow(-1,sign)
    sign += 1
    i += 2

print(f"Sin(x) = {sinx}")   