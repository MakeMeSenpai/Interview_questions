'''Implement an algorithm to determine if a
 string has all unique characters. What if
 you cannot use additional data structures?'''

# h is a dictionary, a dictionary counts as a data structure
# so we added a data structure making this solution invalid. 

# Time Complexity: O(s)
# Space Complexity: O(h)
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
