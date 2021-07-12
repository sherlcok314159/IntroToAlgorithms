def insertion_sort_increase(A:list) -> list:
    r'''
    >>> Input：未排序的序列
    >>> Output：已升序的序列
    Example:
    >>> A = [1,4,3,1]
    >>> print(insertion_sort_increase(A))
    >>> [1, 1, 3, 4]
    '''
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key 
    return A 

def insertion_sort_decrease(A:list) -> list:
    r'''
    >>> Input：未排序的序列
    >>> Output：已降序的序列
    Example:
    >>> A = [1,4,3,1]
    >>> print(insertion_sort_increase(A))
    >>> [4, 3, 1, 1]
    '''
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] < key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key 
    return A 

def linear_search(A, v):
    r'''
    >>> Input: 一个序列和值
    >>> Output： 返回该值对应的下标，若无则返回NIL
    Example:
    >>> A = [1, 2, 3, 4]
    >>> print(linear_search(A, 4))
    >>> 3
    >>> print(linear_search(A, 9))
    >>> NIL
    '''
    i = "NIL"
    for j in range(len(A)):
        if A[j] == v:
            i = j 
    return i 

def add_two_binary_numbers_better(A:list, B:list) -> list:
    r'''
    >>> Input: 两个储存二进制值的序列A和B
    >>> Output： 将A和B相加的结果存储到C,返回C（len(C) = len(A) + 1 ）
    Example:
    >>> A = [1,1,1]
    >>> B = [1,0,1]
    >>> print(add_two_binary_numbers(A, B))
    >>> [1, 1, 0, 0]
    '''
    n = len(A)
    C = [0] * (n + 1)
    for j in range(n-1, -1, -1):
        tem = A[j] + B[j]
        tem = tem + C[j+1]
        if tem >= 2:
            C[j] = C[j] + 1
            tem = tem - 2
        C[j+1] = tem 
    return C 

def add_two_binary_numbers_low(A:list, B:list) -> list:
    r'''
    >>> Input: 两个储存二进制值的序列A和B
    >>> Output： 将A和B相加的结果存储到C,返回C（len(C) = len(A) + 1 ）
    Example:
    >>> A = [1,1,1]
    >>> B = [1,0,1]
    >>> print(add_two_binary_numbers(A, B))
    >>> [1, 1, 0, 0]
    '''
    n = len(A)
    C = [0] * (n+1)
    for i in range(n):
        C[i+1] = A[i] + B[i]
    for j in range(n, -1, -1):
        if C[j] >= 2:
            C[j-1] = C[j-1] + 1
            C[j] = C[j] - 2  
    return C 

