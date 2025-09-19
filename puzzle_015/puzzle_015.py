"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

nums = [3, 2, 2, 3]  # Input array
val = 3  # Value to remove

k = len(nums)-1  # k points to the last index of the array
i = 0  # i is the current index being checked
while (i <= k):  # Continue until i passes k
    if (nums[i] == val):  # If current element equals val
        nums[k], nums[i] = nums[i], nums[k]  # Swap it with the element at k (end of current array)
        k -= 1  # Decrement k, as the last element is now "removed"
    else:
        i += 1  # Only increment i if no swap (otherwise, need to check swapped-in value)

print(k+1, nums[:k+1])  # Print the count of elements not equal to val and the modified array
