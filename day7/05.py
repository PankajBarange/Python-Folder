arr=[1,2,3,4,5,6]
size= len(arr)
def reverse(arr,size):
    
    start = 0
    end = size-1

    while start<=end:
        temp = arr [start]
        arr [start] = arr [end]
        arr [end] = temp
        start = start + 1
        end = end - 1

def printarry(arr):
    for i in range(len(arr)):
        print(arr[i],end="")

printarry(arr)
reverse(arr,size)
print("\n")
printarry(arr)