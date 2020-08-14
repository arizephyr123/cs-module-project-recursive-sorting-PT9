# TO-DO: complete the helper function below to merge 2 sorted arrays
# 4 classes we need to consider
#

def merge_helper(arrA, arrB):
    total = len(arrA) + len(arrB)
    merged_arr = [] 
    a_idx = 0
    b_idx = 0
    while len(merged_arr) < total:
        # no more in arrA
        if a_idx >= len(arrA):
            merged_arr.append(arrB[b_idx])
            b_idx += 1
        # no more in arrB
        elif b_idx >= len(arrB):
            merged_arr.append(arrA[a_idx])
            a_idx += 1
        elif arrA[a_idx] < arrB[b_idx]:
            merged_arr.append(arrA[a_idx])
            a_idx += 1
        elif arrA[a_idx] >= arrB[b_idx]:
            merged_arr.append(arrB[b_idx])
            b_idx += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) == 0:
        return []

    # base case
    if len(arr) > 1:
        #divide arr into LHS, RHS
        LHS = arr[:len(arr)//2]
        RHS = arr[len(arr)//2:]
        # next 2 merge sorts half n per call, so O(log n)
        LHS = merge_sort(LHS)
        RHS = merge_sort(RHS)
        arr = merge_helper(LHS, RHS) # O(n)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

l = [3, 6, 4, 5, 2, 9]
merge_sort(l)