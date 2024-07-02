n = int(input("Enter rows:"))
m = int(input("Enter columns:"))
matrix = []
temp = []
max_sum = 0

for i in range(n):
    arr = []
    for j in range(m):
        print(f"Enter M[{i}][{j}]:")
        arr.append(int(input()))
    matrix.append(arr)

for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j]
        if max_sum < row_sum:
            max_row = i
            max_sum = row_sum

temp = matrix[0]
matrix[0] = matrix[max_row]
matrix[max_row] = temp

print(matrix)