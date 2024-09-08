class Solution:
    def compareNM(self, n: int, m: int) -> str:
        if n < m:
            return 'lesser'
        elif n == m:
            return 'equal'
        else:
            return 'greater'

if __name__ == '__main__':
    ob = Solution()
    print(ob.compareNM(4, 8))  # Output: lesser
    print(ob.compareNM(8, 8))  # Output: equal
    print(ob.compareNM(10, 8)) # Output: greater
