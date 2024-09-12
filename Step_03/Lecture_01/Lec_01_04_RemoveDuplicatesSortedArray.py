class Solution:
    def removeDuplicates(self, nums):
        # If the array is empty, return 0
        if not nums:
            return 0

        # Initialize the index for the next unique element
        unique_index = 0

        # Iterate through the array, starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[unique_index]:
                # Move the unique index forward and update the element
                unique_index += 1
                nums[unique_index] = nums[i]

        # The length of the array with unique elements is unique_index + 1
        return unique_index + 1


# Example usage:
sol = Solution()
nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]
