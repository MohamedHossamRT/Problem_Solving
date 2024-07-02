n = int(input("Enter size of first array:"))
m = int(input("Enter size of second array:"))

arr1 = []
arr2 = []
union = []
intersection = []

print("Enter items of first array:")
for i in range(n):
    arr1.append(int(input()))
print("Enter items of second array:")
for i in range(m):
    arr2.append(int(input()))

for i in range(n):
    if not arr1[i] in union:
        union.append(arr1[i])
for i in range(m):
    if not arr2[i] in union:
        union.append(arr2[i])

i = 0
while i < n and i < m:
    for j in range(m):
        if arr1[i] == arr2[j] and not arr1[i] in intersection:
            intersection.append(arr1[i])
    i += 1

print(union)
print(intersection)