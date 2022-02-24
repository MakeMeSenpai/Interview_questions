'''Implement an algorithm to determine if a
 string has all unique characters. What if
 you cannot use additional data structures?'''

def isUniqueChars(s):
    h = {}
    for i in range(len(s)):
        print(h)
        if s[i] not in h:
            h[s[i]] = i
        else:
            return False
    return True

print(isUniqueChars("qwertyuiopasdfghjklzxcvbnm"))