def printTable(n):
    i = 10
    while i >= 1:
        print(n * i, end=" ")
        i -= 1
    print()

n = int(input())
printTable(n)
