def sumDigits(x):
    if x < 10:
        return x
    else:
        return x % 10 + sumDigits(int(x/10))

if __name__ == '__main__':
    x = int(input("Enter the number:"))
    print(sumDigits(x))