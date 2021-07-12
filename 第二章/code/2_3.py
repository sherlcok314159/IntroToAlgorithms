from math import floor

def merge(A:list,p:int,q:int,r:int) -> list:
    r'''
    >>> A = [0,1,3,5,2,4,6,0]
    >>> print(merge(A,1,3,6))
    >>> [0, 1, 2, 3, 4, 5, 6, 0]
    '''
    L = A[p:q+1] + [float("inf")]
    R = A[q+1:r+1] + [float("inf")]
    i,j = 0,0 
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    return A

def merge_sort(A:list,p:int,r:int) -> list:
    r'''
    >>> A = [8,7,6,5,4,3,2,1]
    >>> print(merge_sort(A,0,7))
    '''
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A,p,q,r)
    return A 

def binary_search_iterative(A:list,v:int,low:int,high:int):
    r'''
    >>> A = [i+2 for i in range(10)]
    >>> print(binary_search(A,10,0,9))
    >>> 8
    '''
    while low <= high:
        mid = floor((low + high) / 2)
        if A[mid] == v:
            return mid
        elif A[mid] > v:
            high = mid - 1
        else:
            low = mid + 1
    return "NIL"

def binary_search_recursive(A:list,v:int,low:int,high:int):
    r'''
    >>> A = [i+2 for i in range(10)]
    >>> print(binary_search(A,10,0,9))
    >>> 8
    '''
    if low > high:
        return "NIL"
    mid = floor((low + high)/2)
    if A[mid] == v:
        return mid 
    elif A[mid] > v:
        return binary_search_recursive(A,v,low,mid-1)
    else:
        return binary_search_recursive(A,v,mid+1,high)

def sum_search_binary_search(A:list, x:int):
    r'''
    >>> A = [1,2,3,4]
    >>> print(sum_search_two_way(A,7))
    >>> True
    '''
    merge_sort(A,0,len(A)-1)
    for i in range(len(A)):
        index = binary_search_recursive(A,x-A[i],0,len(A)-1)
        if index != "NIL" and index != i:
            return True
    return False

def sum_search_two_way(A:list, x:int):
    r'''
    >>> A = [1,2,3,4]
    >>> print(sum_search_two_way(A,7))
    >>> True
    '''
    merge_sort(A,0,len(A)-1)
    low = 0
    high = len(A) - 1
    while low < high:
        if A[low] + A[high] == x:
            return True 
        elif A[low] + A[high] > x:
            high = high - 1
        else:
            low = low + 1
    return False

