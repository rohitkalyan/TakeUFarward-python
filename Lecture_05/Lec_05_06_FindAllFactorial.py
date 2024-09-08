def factorialNumbers(n):
    result = []
    factorial = 1
    i = 1

    while factorial <= n:
        result.append(factorial)
        i += 1
        factorial *= i

    return result

n = 3
print(factorialNumbers(n))

n = 6
print(factorialNumbers(n))
