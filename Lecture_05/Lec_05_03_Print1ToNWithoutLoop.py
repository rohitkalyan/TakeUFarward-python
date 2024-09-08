def printNos(n):
    if n < 1:
        return
    printNos(n - 1)
    print(n, end=" ")

n = 10
printNos(n)
