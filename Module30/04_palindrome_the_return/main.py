from collections import Counter


def is_palindrome(string: str) -> bool:
    if sum(map(lambda odd: 1, (filter(lambda x: x % 2 != 0, Counter(list(string)).values())))) < 2:
        return True
    return False


print(is_palindrome('abcba'))
print(is_palindrome('abbbc'))