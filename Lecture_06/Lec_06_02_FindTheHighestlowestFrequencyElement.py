from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array to use sliding window
        nums.sort()

        # Initialize variables
        left = 0
        total = 0
        max_frequency = 1

        # Iterate through the array using right pointer
        for right in range(len(nums)):
            # Add the current element to the total sum
            total += nums[right]

            # Check if the current window is valid
            while nums[right] * (right - left + 1) > total + k:
                # If not valid, shrink the window from the left
                total -= nums[left]
                left += 1

            # Update the maximum frequency
            max_frequency = max(max_frequency, right - left + 1)

        return max_frequency


# Example usage:
sol = Solution()
print(sol.maxFrequency([1, 2, 4], 5))  # Output: 3
print(sol.maxFrequency([1, 4, 8, 13], 5))  # Output: 2
print(sol.maxFrequency([3, 9, 6], 2))  # Output: 1
