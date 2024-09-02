class Solution:
    def dataTypeSize(self, str):
        type_sizes = {
            "Character": 1,
            "Integer": 4,
            "Long": 8,
            "Float": 4,
            "Double": 8
        }

        return type_sizes.get(str, -1)


# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)

