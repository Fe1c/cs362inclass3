def palindrome(string):
    r = string[::-1]
    if r == string:
        return 1
    else:
        return 0