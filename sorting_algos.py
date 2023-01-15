
# Bubble sort : O(n^2) -----------------------------------------------------
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Selection sort : O(n^2) --------------------------------------------------
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# Insertion sort : O(n^2) -------------------------------------------------------
def insertion_sort(arr):
    for i in range(len(arr)):
        ins = arr[i]
        j =  i - 1
        while j>=0 and ins < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ins
    return arr


# Merge sort : O(n log n) -----------------------------------------------------
def merge(left, right):
    res = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            res.append(left[leftindex])
            leftindex += 1
        else:
            res.append(right[rightindex])
            rightindex += 1
    
    return res + left[leftindex:] + right[rightindex:]

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    return merge(merge_sort(left), merge_sort(right))

# Quick sort - extra space : O(n log n) / O(n^2) if bad pivot choice ------------
from random import randint

def quick_sort(arr):
    if len(arr) < 2:
        return arr  
    low, high, same = [], [], []
    pivot = arr[randint(0, len(arr) - 1)]
    for item in arr:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        elif item == pivot:
            same.append(item)
        
    return quick_sort(low) + same + quick_sort(high)


# Tim Sort - O(n log n) ----------------------------------------------------------
def insertion_tim_sort(arr, start, end):
    for i in range(start+1, end+1):
        ins = arr[i]
        j = i - 1
        while j>=start and ins < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ins
    return arr

def tim_sort(arr):
    # A chosen run size
    min_run_size = 3

    # Phase 1 - Sort each run with insertion sort
    for start in range(0, len(arr), min_run_size):
        end = min((start + min_run_size - 1), (len(arr) - 1))
        insertion_tim_sort(arr, start, end)

    # Phase 2 - Merge the sorted runs using merge sort
    size = min_run_size
    while size < len(arr):
        for start in range(0, len(arr), min_run_size * 2):
            mid = start + size - 1
            end = min((start + 2*size - 1), len(arr) - 1)

            left = arr[start : mid+1]
            right = arr[mid+1 : end+1]
            merged_arr = merge(left, right)

            arr[start : start+len(merged_arr)] = merged_arr
        
        size *= 2
    
    return arr


# Tests -------------------------------------------------------------------------
print(bubble_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(selection_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(insertion_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(merge_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(quick_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(tim_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))