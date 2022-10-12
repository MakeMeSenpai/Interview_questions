'''Implement an algorithm to determine if a
 string has all unique characters. What if
 you cannot use additional data structures?'''

# Time Complexity: O(s)
# Space Complexity: O(h)
"""def isUniqueChars(s):
    h = {}
    for i in range(len(s)):
        print(h)
        if s[i] not in h:
            h[s[i]] = i
        else:
            return False
    return True"""
# h is a dictionary, a dictionary counts as a data structure
# so we added a data structure making the above solution invalid.

# Time Complexity: O(s^2 - 1)
# Space Complexity: O(1)
def isUniqueChars(s):
    # grabs first char
    for i in range(len(s)):
        # compares to other chars
        for j in range(len(s)-1):
            print(i, j+1)
            # ensures we don't check the same index
            if i > 0 and i != j+1:
                print(s[i], s[j+1])
                # if any char is the same
                if s[i] == s[j+1]:
                    # it's not a unique string
                    return False
            elif i == 0:
                print(s[i], s[j+1])
                # if any char is the same
                if s[i] == s[j+1]:
                    # it's not a unique string
                    return False
    # else, it is
    return True

print(isUniqueChars("qwertr"))
