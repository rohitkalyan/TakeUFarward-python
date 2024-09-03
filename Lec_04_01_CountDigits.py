class Solution:
    def evenlyDivides(self, N):
        original_number = N
        count = 0

        while N > 0:
            digit = N % 10
            if digit != 0 and original_number % digit == 0:
                count += 1
            N //= 10

        return count