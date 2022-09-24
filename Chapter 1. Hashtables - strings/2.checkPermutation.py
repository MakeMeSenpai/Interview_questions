"""Given two strings, write a method to
 decide if one is a permutation of the other."""

# what is a permutation?
# a permutation is a reordered set of characters
# CBA BCA CAB BAC and ACB are permutations of ABC

# Time Complexity: O(perm^2 + combinations) -> O(perm)
# Space Complexity: O(combos)

from itertools import permutations

def checkP(string, perm):
    # edge cases 
    # include the string being the same
    if perm == string:
        return False
    # or the length of strings differ
    elif len(perm) != len(string):
        return False

    # create list of all combos of perm
    combos = [''.join(p) for p in permutations(perm)]
    print(combos)

    #compare string with all combos
    for i in combos:
        # if a combo matches
        if string == i:
            # it's a permutation of string
            return True

    # if nothing matches, it's not a permutation
    return False

print(checkP("the cat", "hec tat"))