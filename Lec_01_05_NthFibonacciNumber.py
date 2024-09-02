def findFibonacci(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1

    for i in range(3, n + 1):
        a, b = b, a + b

    return b

if __name__ == "__main__":
    n = int(input().strip())
    print(findFibonacci(n))
