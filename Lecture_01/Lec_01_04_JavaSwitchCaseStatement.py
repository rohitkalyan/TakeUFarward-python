import math

class Solution:
    def switchCase(self, choice, arr):
        # Calculate area based on the choice
        if choice == 1:
            # Area of circle
            R = arr[0]
            return math.pi * R * R
        elif choice == 2:
            # Area of rectangle
            L = arr[0]
            B = arr[1]
            return L * B

# Example Usage
if __name__ == '__main__':
    ob = Solution()
    # Example 1: Area of Circle
    print(ob.switchCase(1, [5]))  # Output: 78.53981633974483
    # Example 2: Area of Rectangle
    print(ob.switchCase(2, [5, 10]))  # Output: 50
