def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i, j = 0,0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result # Return the sorted array
if __name__ == "__main__":
    a = [4, 5, 3, 10, 21, 12, 15, 0, 9]
    print(merge_sort(a)) # [0, 3, 4, 5, 9, 10, 12, 15, 21]
