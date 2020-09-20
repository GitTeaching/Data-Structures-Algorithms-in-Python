# -*- coding: utf-8 -*-
"""
Insertion algorithm segments the list into sorted and unsorted parts. It iterates over the 
unsorted segment, and inserts the element being viewed into the correct position of 
the sorted list.

Insertion sort involves finding the right place for a given element in a sorted list. 
So in beginning we compare the first two elements and sort them by comparing them. 
Then we pick the third element and find its proper position among the previous two 
sorted elements. This way we gradually go on adding more elements to the already sorted 
list by putting them in their proper position.

Time complexity of O(n^2)
"""

def insertion_sort(lst):
    for i in range(1, len(lst)):
        element_to_insert = lst[i]
        
        j = i - 1
        
        while j>=0 and lst[j] > element_to_insert:
            lst[j+1] = lst[j]
            j = j - 1
        
        lst[j+1] = element_to_insert
        

# Insertion sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
insertion_sort(lst)
print(lst)