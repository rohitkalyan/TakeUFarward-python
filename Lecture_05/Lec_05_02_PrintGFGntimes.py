def printGfg(n):
    if n <= 0:
        return
    print("GFG", end=" ")
    printGfg(n - 1)
n = 5
printGfg(n)
