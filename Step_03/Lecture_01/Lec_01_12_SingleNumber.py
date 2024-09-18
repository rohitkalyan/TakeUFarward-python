def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [2, 2, 1]
single_number = singleNumber(nums)
print(single_number)