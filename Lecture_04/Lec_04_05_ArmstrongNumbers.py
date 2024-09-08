def checkArmstrong(n):
    num_str = str(n)
    k = len(num_str)
    sum_of_powers = sum(int(digit) ** k for digit in num_str)

    return sum_of_powers == n


if __name__ == '__main__':
    print(checkArmstrong(1))  # Output: True
    print(checkArmstrong(103))  # Output: False
    print(checkArmstrong(1634))  # Output: True
