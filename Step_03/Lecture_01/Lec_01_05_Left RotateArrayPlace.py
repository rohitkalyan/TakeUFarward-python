class Solution:
    def rotate(self, nums, k):
        # Find the effective rotation steps needed
        k = k % len(nums)

        # Reverse the entire array
        nums.reverse()

        # Reverse the first k elements
        self.reverseArray(nums, 0, k - 1)

        # Reverse the rest of the elements
        self.reverseArray(nums, k, len(nums) - 1)

    def reverseArray(self, nums, start, end):
        # Helper function to reverse a portion of the array in place
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# Example usage:
sol = Solution()
nums1 = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
sol.rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]
