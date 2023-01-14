
# Bubble sort : O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Selection sort : O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# Insertion sort : O(n^2)
def insertion_sort(arr):
    for i in range(len(arr)):
        ins = arr[i]
        j =  i - 1
        while j>=0 and ins < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ins
    return arr


# Merge sort : O(n log n)
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

# Quick sort - extra space : O(n log n) / O(n^2) if bad pivot choice
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


# Tests
print(bubble_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(selection_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(insertion_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(merge_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))

print(quick_sort(([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])))