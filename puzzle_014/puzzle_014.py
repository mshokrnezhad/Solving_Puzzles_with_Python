"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""

nums1 = [1, 2, 3, 0, 0, 0]  # First sorted array with extra space for nums2
m = 3  # Number of valid elements in nums1
nums2 = [2, 5, 6]  # Second sorted array
n = 3  # Number of valid elements in nums2

nums1 = nums1[:m]  # Trim nums1 to only its valid elements
nums2 = nums2[:n]  # Trim nums2 to only its valid elements

nums3 = []  # Resultant merged array

j = 0  # Pointer for nums2
i = 0  # Pointer for nums1

if len(nums2) == 0:
    nums3 = nums1  # If nums2 is empty, merged array is just nums1
elif len(nums1) == 0:
    nums3 = nums2  # If nums1 is empty, merged array is just nums2
else:
    while i < len(nums1) and j < len(nums2):  # While both arrays have elements left
        while nums1[i] <= nums2[j]:  # If current nums1 element is less or equal
            nums3.append(nums1[i])  # Add nums1 element to merged array
            i += 1  # Move pointer in nums1
            if i == len(nums1):  # If reached end of nums1
                nums3.extend(nums2[j:])  # Add remaining nums2 elements
                break  # Exit inner loop
            else:
                while nums2[j] <= nums1[i]:  # If current nums2 element is less or equal
                    nums3.append(nums2[j])  # Add nums2 element to merged array
                    j += 1  # Move pointer in nums2
                    if j == len(nums2):  # If reached end of nums2
                        break  # Exit inner loop

print(nums3)  # Print the merged sorted array
