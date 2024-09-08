import math


class Solution:
    def lcmAndGcd(self, a: int, b: int) -> list:
        # Compute GCD
        gcd_value = math.gcd(a, b)

        # Compute LCM using the formula LCM(a, b) = (a * b) / GCD(a, b)
        lcm_value = abs(a * b) // gcd_value

        # Return the LCM and GCD as a list
        return [lcm_value, gcd_value]


# Example Usage
if __name__ == '__main__':
    ob = Solution()
    print(ob.lcmAndGcd(5, 10))  # Output: [10, 5]
    print(ob.lcmAndGcd(14, 8))  # Output: [56, 2]
