def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example Usage
data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Insertion Sort:", insertion_sort(data.copy()))
