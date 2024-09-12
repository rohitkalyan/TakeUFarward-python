class Solution:
    def check(self, nums):
        # Initialize count of drops (places where the order breaks)
        count = 0
        n = len(nums)

        for i in range(n):
            # If the current element is greater than the next element, increment count
            if nums[i] > nums[(i + 1) % n]:
                count += 1

            # If there is more than one drop, the array is not a rotated sorted array
            if count > 1:
                return False

        # If we have zero or one drop, it's a valid rotated sorted array
        return True


# Example usage:
sol = Solution()
print(sol.check([3, 4, 5, 1, 2]))  # Output: True
print(sol.check([2, 1, 3, 4]))  # Output: False
print(sol.check([1, 2, 3]))  # Output: True
