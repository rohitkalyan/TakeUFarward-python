def isPalindrome(s):
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]


s1 = "A man, a plan, a canal: Panama"
print(isPalindrome(s1))

s2 = "race a car"
print(isPalindrome(s2))

s3 = " "
print(isPalindrome(s3))
