def printNos(n):
    # Base case: if n is 0, return
    if n == 0:
        return

    # Recursive call to print numbers from 1 to n-1
    printNos(n - 1)

    # Print the current number n
    print(n, end=' ')


if __name__ == '__main__':
    printNos(10)
    print()
    printNos(5)
