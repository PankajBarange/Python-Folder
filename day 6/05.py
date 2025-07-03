arr = [2,3,4,5,6,8]
element =5

def linearSearch(arr, element):

    for i in arr:
        if arr[i] == element:
            return i
    return -1

result = linearSearch(arr, element) 

print("The Element {element} is found at index = {result}")