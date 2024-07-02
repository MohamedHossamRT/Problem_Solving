print("Enter number of integers:")
n = int(input())
print("Enter k places:")
k = int(input())
arr = []

print("Enter integers:")
for i in range(n):
    arr.append(int(input()))

for i in range(k):
    temp = arr[-1]
    for j in range(n-1,0,-1):
        arr[j] = arr[j-1]   
    arr[0] = temp     
       
print(arr)
