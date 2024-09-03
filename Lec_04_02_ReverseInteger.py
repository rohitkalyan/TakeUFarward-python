import sys


class Solution:
    def reverse(self, x: int) -> int:
        # Use sys to get the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Determine the sign of x
        sign = -1 if x < 0 else 1

        # Convert the absolute value of x to a string, reverse it, and convert back to integer
        reversed_num = int(str(abs(x))[::-1])

        # Apply the sign to the reversed number
        reversed_num *= sign

        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num


# Example Usage
if __name__ == '__main__':
    ob = Solution()
    print(ob.reverse(123))  # Output: 321
    print(ob.reverse(-123))  # Output: -321
    print(ob.reverse(120))  # Output: 21
