# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) < 1:
        return -1
    start = start
    end = end
    mid = start + (end-start) //2
    while start <= end:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid -1)
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, end)
        else:
            return -1
    





# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []

print(binary_search(arr1, -8, 0, len(arr1)-1), '1')
print(binary_search(arr1, 0, 0, len(arr1)-1), '6')
print(binary_search(arr2, 6, 0, len(arr2)-1), '-1')
print(binary_search(arr2, 0, 0, len(arr2)-1), '-1')

# ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
# descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

# print(agnostic_binary_search(ascending, 12), '2')
# print(agnostic_binary_search(ascending, 54), '9')
# print(agnostic_binary_search(ascending, 31), '-1')

# print(agnostic_binary_search(descending, 49), '3')
# print(agnostic_binary_search(descending, -17), '7')
# print(agnostic_binary_search(descending, -1), '-1')
