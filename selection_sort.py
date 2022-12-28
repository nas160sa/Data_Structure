def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    return arr


#Test
arr = [5,9,4,2,8,6,1,7,3,0]
print(selection_sort(arr)) 
