def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

# Example Test Cases
nums1 = [3, 3, 1]
print(single_number(nums1))  # Output: 1

nums2 = [5, 1, 3, 1, 3]
print(single_number(nums2))  # Output: 4