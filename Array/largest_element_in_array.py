
def largest_number(arr):
    if not arr:
        return None
    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i 
    return largest