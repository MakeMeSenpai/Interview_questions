"""Given two strings, write a method to
 decide if one is a permutation of the other."""

def checkP(string, perm):
    if perm in string:
        return True
    return False

print(checkP("the cat", "hec"))