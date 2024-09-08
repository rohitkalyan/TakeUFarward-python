class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the number to a string
        str_x = str(x)

        # Check if the string is the same as its reverse
        return str_x == str_x[::-1]


# Example Usage
if __name__ == '__main__':
    ob = Solution()
    print(ob.isPalindrome(121))  # Output: True
    print(ob.isPalindrome(-121))  # Output: False
    print(ob.isPalindrome(10))  # Output: False
