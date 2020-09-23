# -*- coding: utf-8 -*-
"""
Merge sort - This divide and conquer algorithm splits a list in half, and keeps splitting the 
list by 2 until it only has singular elements.

Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with 
other pairs as well. This process continues until we get a sorted list with all the 
elements of the unsorted input list.

Fast algorithm. Used in sort() and sorted() built in function based on Tim Sort version.
Efficient for large data sets.

Time complexity of the Merge Sort algorithm is O(nlog(n)).

Merge Sort is useful for sorting linked lists in O(nLogn) time.

The space complexity of merge sort is O(n).
"""

def merge(left_lst, right_lst):
    sorted_list = []
    
    left_list_index = right_list_index = 0

    #left_list_length, right_list_length = len(left_lst), len(right_lst)

    for _ in range(len(left_lst) + len(right_lst)):
        if left_list_index < len(left_lst) and right_list_index < len(right_lst):
            if left_lst[left_list_index] <= right_lst[right_list_index]:
                sorted_list.append(left_lst[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_lst[right_list_index])
                right_list_index += 1

        elif left_list_index == len(left_lst):
            sorted_list.append(right_lst[right_list_index])
            right_list_index += 1

        elif right_list_index == len(right_lst):
            sorted_list.append(left_lst[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst)//2
    
    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])
    
    # Merge the two sorted lists into a new one
    return merge(left_lst, right_lst)
      
        
# Merge sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
sorted_lst = merge_sort(lst)
print(sorted_lst)