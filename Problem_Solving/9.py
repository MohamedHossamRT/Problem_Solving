n = int(input("Enter size of first array:"))
m = int(input("Enter size of second array:"))
arr1 = []
arr2 = []
arr3 = []

print("Enter items of first array (sorted):")
for i in range(n):
    arr1.append(int(input()))
print("Enter items of second array (sorted):")
for i in range(m):
    arr2.append(int(input()))

i = 0
j = 0

while i < n and j < m:
    if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j+=1

if m!=n:
    if i < n:
        arr3.append(arr1[i])
        i+=1
    if j < m:
        arr3.append(arr3[j])
        j+=1

print(arr3)  