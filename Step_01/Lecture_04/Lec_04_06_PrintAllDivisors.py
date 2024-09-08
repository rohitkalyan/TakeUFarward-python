class Solution:
    def sumOfDivisors(self, N: int) -> int:
        # Initialize total sum to 0
        total_sum = 0

        # Iterate from 1 to N
        for i in range(1, N + 1):
            # Count how many numbers are divisible by i and compute contribution of i
            total_sum += i * (N // i)

        return total_sum


if __name__ == '__main__':
    ob = Solution()
    print(ob.sumOfDivisors(4))  # Output: 15
    print(ob.sumOfDivisors(5))  # Output: 21
