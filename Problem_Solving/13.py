N = int(input("Enter rows of first matrix:"))
M = int(input("Enter columns of first matrix (rows of second matrix):"))
matrix1 = []
L = int(input("Enter columns of second matrix:"))
matrix2 = []
matrix3 = []

for i in range(N):
    arr1 = []
    for j in range(M):
        print(f"Enter M[{i}][{j}]:")
        arr1.append(int(input()))
    matrix1.append(arr1)

for i in range(M):
    arr2 = []
    for j in range(L):
        print(f"Enter M[{i}][{j}]:")
        arr2.append(int(input()))
    matrix2.append(arr2)

for i in range(N):
    arr3 = []
    for j in range(L):
        sum = 0
        for k in range(M):
            sum += matrix1[i][k] * matrix2[k][j]
        arr3.append(sum)
    matrix3.append(arr3)
print(matrix3)