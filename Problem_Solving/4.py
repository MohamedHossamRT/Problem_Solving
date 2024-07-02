print("Enter the number: ")
n = int(input())
i = 1
factorial = 1
if n <= 12:
    while i <= n:
        factorial = factorial * i 
        i+=1
print(factorial)
