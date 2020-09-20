# -*- coding: utf-8 -*-
"""
Selection sort algorithm segments the list into two parts: sorted and unsorted. 
We continuously remove the smallest element of the unsorted segment of the list and append 
it to the sorted segment. 

Treat the leftmost part of the list as the sorted segment. 
We then search the entire list for the smallest element, and swap it with the first element.

Time complexity : The inner loop iterate n-1 when i is equal to 1, and then n-2 as i is equal 
to 2 and so forth.The amount of comparisons are (n - 1) + (n - 2) + ... + 1, which 
gives Selection Sort a time complexity of O(n^2).
"""

def selection_sort(lst):
    for i in range(len(lst)):
        smallest_val_index = i
        
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallest_val_index]:
                smallest_val_index = j
        
        lst[smallest_val_index], lst[i] = lst[i], lst[smallest_val_index]


# Selection sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
selection_sort(lst)
print(lst)