n = int(input("Enter rows:"))
m = int(input("Enter columns:"))
matrix = []
transpose = []
temp = 0

for i in range(n):
    arr = []
    for j in range(m):
        print(f"Enter M[{i}][{j}]:")
        arr.append(int(input()))
    matrix.append(arr)
print(matrix)

for i in range(m):
    tarr = []
    for j in range(n):
        tarr.append(matrix[j][i])
    transpose.append(tarr)

print(transpose)