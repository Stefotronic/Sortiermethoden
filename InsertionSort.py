
def insertionSort(arr):
    l = len(arr)
    
    for i in range(l):
        elementToSort = arr[i]
        j = i

        while j > 0 and elementToSort < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = elementToSort

    return arr


list = [6, 2, 4, 9, 3, 7, 1]
res = insertionSort(list)
print(res)


