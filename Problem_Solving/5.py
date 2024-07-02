print("Enter the number:")
n = int(input())
i = 2
prime = 1
while i < n:
    if n % i == 0:
        prime = 0
        break
    else:
        i+=1
if prime and n!=0 and n!=1:
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT a prime number")