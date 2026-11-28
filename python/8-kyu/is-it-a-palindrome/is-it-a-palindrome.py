def is_palindrome(s):
    return "".join(reversed(s)).lower() == s.lower()
​