class Solution:
    def print2largest(self, arr):
        # Convert array to a set to remove duplicates and then back to a list
        distinct_elements = list(set(arr))

        # If there are less than 2 distinct elements, return -1
        if len(distinct_elements) < 2:
            return -1

        # Sort the distinct elements in descending order
        distinct_elements.sort(reverse=True)

        # The second element in the sorted list is the second largest
        return distinct_elements[1]


# Example usage:
sol = Solution()
print(sol.print2largest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(sol.print2largest([10, 10]))  # Output: -1
