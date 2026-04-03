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

#imp axis
arr= np.arange(1,10)

arr= arr.reshape(3,3)

row_sum=arr.sum(axis=1)
print(row_sum)

column_sum=arr.sum(axis=0)
print(column_sum)

#transpose of matrix
arrt=arr.T #or use arr.transpose()
print(arrt)

#imp
arr=np.array([10,20,30,40,50])
print(arr>20)
print(arr[arr>20])

print(arr[[0, 2]]) #Select multiple indexes at once
                   #[10,30] #[[]]

a = np.array([1,2])
b = np.array([3,4])

print(np.vstack((a,b)))
print(np.hstack((a,b)))                 

arr = np.array([[1,2],[3,4]])
# arr=arr.reshape(1,1) get error
arr=arr.flatten()
print(arr)


#  Gives index where condition is true
arr = np.array([10, 20, 30, 40])
print(np.where(arr > 20)) #(array([2, 3]),)

#sorting
arr = np.array([3,1,2])
print(np.sort(arr))

#Unique Values
arr = np.array([1,2,2,3,3])
print(np.unique(arr))

# Replace all values > 20 with 0
arr[arr>20] = 0
print(arr)

#easy replac
arr[1]=100
print(arr)