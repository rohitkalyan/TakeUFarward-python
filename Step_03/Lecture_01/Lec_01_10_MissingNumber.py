nums = [3,0,1, 2, 4, 5, 6, 7, 9]
max_element = max(nums)
missingElement = 0
for i in range(0, max_element):
    if not i in nums:
        missingElement = i

print(missingElement)
