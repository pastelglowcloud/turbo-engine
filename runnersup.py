from unittest import runner

n= 5
arr = [2,3,6,6,5]
arr = sorted(arr)
for i in range(2,n):
    while arr[i] < max(arr):
        runnerup = i
print(runnerup)

winner = max(arr[0],arr[1])
runnerup = min(arr[0],arr[1])

for i in range(2,n):
    if arr[i] > winner:
        runnerup = winner
        winner = arr[1]
    elif arr[i] > runnerup and arr[i] != winner:
        runnerup = arr[i]

winner = max(arr[0],arr[1])
runnerup = min(arr[0],arr[1])
n = len(arr)
for i in range(2,n):
    if arr[i] > winner:
        runnerup = winner
        winner = arr[i]
    elif arr[i] > runnerup and winner != arr[i]:
        runnerup = arr[i]

arr = list(arr)
winner = max(arr[0],arr[1])
runnerup = min(arr[0],arr[1])
for i in range(2,n):
    if arr[i] > winner:
        runnerup = winner
        winner = arr[i]
    elif arr[i] > runnerup and arr[i]!= winner:
        runnerup = arr[i]