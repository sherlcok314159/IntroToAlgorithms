def selection_sort_mine(A):
    r'''
    >>> Input：未排序的序列
    >>> Output：已升序的序列
    Example:
    >>> A = [1,4,3,1]
    >>> print(selection_sort_mine(A))
    >>> [1, 1, 3, 4]
    '''
    for j in range(len(A)-1):
        key = min(A[j:])
        A[A[j:].index(key)+j] = A[j]
        A[j] = key
    return A 


def selection_sort_official(A:list) -> list:
    r'''
    >>> Input：未排序的序列
    >>> Output：已升序的序列
    Example:
    >>> A = [1,4,3,1]
    >>> print(selection_sort_official(A))
    >>> [1, 1, 3, 4]
    '''
    for j in range(len(A)-1):
        smallest = j
        for i in range(j+1, len(A)):
            if A[i] < A[smallest]:
                smallest = i 
        key = A[j]
        A[j] = A[smallest]
        A[smallest] = key 
    return A 
