# -*- coding: utf-8 -*-
"""
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. 
This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far 
right and has to be moved to the far left.

Shell sort is an algorithm that first sorts the elements far apart from each other and successively 
reduces the GAP(interval) between the elements to be sorted. It is a generalized version of insertion sort.

In shell sort, elements at a specific interval are sorted. The interval between the elements is gradually 
decreased based on the sequence used. The performance of the shell sort depends on the type of sequence 
used for a given input array.

Some of the optimal sequences used are: Shell's original sequence: N/2 , N/4 , …, 1, Knuth, etc.

Shell sort is an unstable sorting algorithm because this algorithm does not examine the elements 
lying in between the intervals.

Worst Case Complexity: less than or equal to O(n2)
According to Poonen Theorem, worst case complexity for shell sort is Θ(Nlog N)2/(log log N)2) or 
Θ(Nlog N)2/log log N) or Θ(N(log N)2) or something in between.

Best Case Complexity: O(n*log n)   / Average Case Complexity: O(n*log n)

The space complexity for shell sort is O(1).
"""

def shell_sort(lst):   
    gap = len(lst) // 2
    
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]         
            j = i
            
            while j >= gap and lst[j-gap] > temp:
                lst[j] = lst[j-gap]
                j = j - gap
            
            lst[j] = temp
        
        gap = gap // 2
    
    
# hell sort algorithm testing
lst = [64, 34, 25, 12, 22, 11, 90, 0]
shell_sort(lst)
print(lst)

