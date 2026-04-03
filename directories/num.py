import numpy as np
a = np.array([1,2,3])
print(a)
print(type(a))

#types
print(np.zeros(5))#array of 5 zeros
print(np.ones(5))#array of 5 ones
print(np.full(5,7))#array of 5 sevens

print(np.arange(1,9))#array of 1 to 8
print(np.linspace(0,1,5))#equal sliicing

#2d array
arr= np.array([[1,2,3],
              [4,5,6]])
print(arr,
      arr.shape,   #shape → rows × columns
      arr.ndim,    #ndim → dimension
      arr.size)    #size → total elements

arr=np.array([1,2,3,4,5])
print(arr[5:0:-1]) #slicing 

arr= np.array([[1,2,3],
              [4,5,6]])

print(arr[1,1])   # 5 [nth list,nth in list]

#property
print("____________________")

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+5) #imp
print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print("____________________")
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4,5,6],[7,8,9]])

print(a + b)   
print(a * b)   


arr = np.array([1,2,3,4])

print(
np.sum(arr),    # 10
np.mean(arr),   # 2.5
np.max(arr)  ,  # 4
np.min(arr)    ,# 1
)

#Converts 1D → 2D
arr = np.arange(6)

arr= arr.reshape(2,3)
print(arr)

