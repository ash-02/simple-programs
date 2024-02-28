def find_neither_min_max(arr):
    length = len(arr)
    
    if length <= 2:
        return "Array length must be greater than 2"

    minimumElement = arr[0]
    maximumElement = arr[1]
    middleElement = arr[2]

    if arr[0] > arr[1]:
        minimumElement = arr[1]
        maximumElement = arr[0]
    
    if arr[2] < minimumElement:
        middleElement = minimumElement
    
    if arr[2] > maximumElement:
        middleElement = maximumElement
    
    return middleElement


arr = [78879,17282,82827]
result = find_neither_min_max(arr)
print(result)