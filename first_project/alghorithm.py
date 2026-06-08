# insertion_sort
def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr
print("This is a Insertion " ,insertion( [25,16,8,2,10] ))
####       merge_sort #############
def merge_sort(A,p,r):
    if p < r:
        q = (r+p) //2
        merge_sort(A,p,q)    ##for the left
        merge_sort(A,q+1,r)  ###for the right
        merge(A,p,q,r)

def merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    n1 = len(L)
    n2 = len(R)
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i<n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
arr = [18,26,85,14,25,2,4]
merge_sort(arr, 0 ,len(arr) - 1)
print("This is a Merge " ,arr)
 ### quick_sort
def Quick_sort(A,p,r):
    if p < r:
        q = Partittion(A,p,r)
        Quick_sort(A,p,q-1)
        Quick_sort(A,q+1,r)

def Partittion(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r-1):
        if A[j] <= x:
            i = i +1
            A[j] = A[i]
    A[i+1] = A[r]
    return i+1

arr = [5,3,2,4]
sorting = Quick_sort(arr,0,len(arr)-1)
print(sorting)

def Binary_search(A,target):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [2,4,6,8,10,12,14]
target = 
print(Binary_search(arr, target))
def seerach_function(root,x):
    current = root
    while current != Null and x!= current.ley:
        if x < current.key:
            current = current.left
        else:
            currrent = current.right
    return currenr


    
