class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # If the array length is 1, we are already at the end
        if n == 1:
            return 0

        # If the first element is 0, we cannot move further
        if arr[0] == 0:
            return -1

        # Initialize the variables
        jumps = 0
        current_end = 0
        farthest = 0

        # Traverse the array to calculate the minimum jumps
        for i in range(n):
            # Update the farthest point that can be reached
            farthest = max(farthest, i + arr[i])

            # If we reach the end of the range with the current number of jumps
            if i == current_end:
                # Increment the jump count
                jumps += 1
                current_end = farthest

                # If the current end is greater than or equal to the last index
                if current_end >= n - 1:
                    return jumps

            # If we cannot move further from the current position
            if i == farthest:
                return -1

        return -1


# Example Usage
if __name__ == '__main__':
    ob = Solution()
    print(ob.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))  # Output: 3
    print(ob.minJumps([1, 4, 3, 2, 6, 7]))  # Output: 2
    print(ob.minJumps([0, 10, 20]))  # Output: -1
