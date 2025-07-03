arr=[1,2,3,4,5,6,7,8,9,10]
element=99
size=len(arr)

def BinarySearch(arr,element):
    start=0
    end=size-1

    while start<=end:

        mid=(start+end)/2
        mid=int(mid)

        if arr[mid]==element:
            return mid
        
        elif arr[mid]<element:
            start=mid+1

        else:
            end=mid-1
    return -1      

result=BinarySearch(arr,element)
print(f"The Element{element}is found at index={result}")
  

        
        
    