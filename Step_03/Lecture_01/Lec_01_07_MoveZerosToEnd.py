class Solution:
    def moveZeroes(self, nums):
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

sol = Solution()
nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # Output: [0]
