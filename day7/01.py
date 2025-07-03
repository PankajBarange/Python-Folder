arr=[1,2,5,6,7,10]
element=6

def linearSearch(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1
    
result = linearSearch(arr, element)
print(f"The Element{element}is found at index number={result}")