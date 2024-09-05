def sumOfSeries(n):
    sum_cubes = sum(i ** 3 for i in range(1, n + 1))
    return sum_cubes

n = 5
print(sumOfSeries(n))

n = 7
print(sumOfSeries(n))
