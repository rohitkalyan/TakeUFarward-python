def printNos(N):
    if N < 1:
        return
    print(N, end=" ")
    printNos(N - 1)

N = 10
printNos(N)
