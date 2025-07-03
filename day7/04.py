arr1=int(input("enter the value"))
arr2=int(input("enter the value"))
arr3=int(input("enter the value"))
arr4=int(input("enter the value"))
arr5=int(input("enter the value"))

arr = [arr1,arr2,arr3,arr4,arr5]
size= len(arr)

def reverse(arr, size):

    start = 0
    end = size - 1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start+1
        end = end - 1


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i],end="")

printArray(arr)
reverse(arr,size)
print("\n")
printArray(arr)     