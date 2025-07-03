arr = [8,6,2,3,5,4]
size = len(arr)

def bubbleSort(arr,size):
     
     for i in range (size):
          
          for j in range (size - 1):
               
               if arr[i] < arr[j]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp

def printArray(arr):
      for i in arr:
        print(i, end=" ")

printArray(arr)
bubbleSort(arr,size)
print("\n")
printArray(arr)