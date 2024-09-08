"""
Input: n = 5, arr[] = [2, 3, 2, 3, 5], p = 5
Output: [0, 2, 2, 0, 1]
"""

n = 5
res = []
arr = [2, 3, 2, 3, 5]

for i in range(1, n+1):
    res.append(arr.count(i))

print(res)