def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    n = int(input("Enter the number of term:"))
    print(fibonacci(n))