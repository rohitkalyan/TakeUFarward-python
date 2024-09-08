class Solution:
    def passedBy(self, a: int, b: int) -> list:
        a_value = a + 1
        b_reference = b + 2

        return [a_value, b_reference]


# Example Usage
if __name__ == '__main__':
    ob = Solution()
    print(ob.passedBy(1, 2))
    print(ob.passedBy(10, 20))
