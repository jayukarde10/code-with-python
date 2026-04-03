import numpy as np
import random
arr = np.array([5, 10, 15, 20, 25, 30])

# Find mean of values greater than 15
print(arr[arr>15].mean())

arr = np.arange(1, 13).reshape(3,4)

# Output:
# Row sums
print(arr.sum(axis=1))
# Column means
print(arr.mean(axis=1))

arr = np.array([10, 25, 30, 15, 40])

# Replace all values > 20 with 0
arr[arr>20] = 0
print(arr)

arr = np.arange(1,10).reshape(3,3)

# Extract diagonal elements
print(arr.diagonal())
arr=[]
for i in range(1,6):
    arr.append(random.randint(1,51))
arr=np.array(arr)
print(np.sort(arr))

arr = np.array([1,2,3])
arr1=arr.copy()
arr2=arr.copy()
arr3=arr.copy()
arr=np.array([arr1,arr2,arr3])
print(arr)
# Convert to:
# [[1,2,3],
#  [1,2,3],
#  [1,2,3]]