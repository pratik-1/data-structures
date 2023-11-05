"""
You have been given an array of strings, where each string may contain only lowercase English letters.
You need to write a function group_anagrams(strings) that groups the anagrams in the array together.
The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"],
the function should return [["eat","tea","ate"],["tan","nat"],["bat"]]
because the first three strings are anagrams of each other, the next two strings are anagrams of each other,
and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists,
where each inner list contains a group of anagrams according to the above requirements.
"""
# Method 1: Using hash function
def index_hash(key) -> int:
    ix = 0
    for i in key:
        ix = (ix + ord(i)*23)%7
    return ix

def group_anagrams(lst) -> list:
    d ={}
    for word in lst:
        ix = index_hash(word)
        if ix in d:
            d[ix].append(word)
        else:
            d[ix] = [word]
    return list(d.values())


# Method 2: Using sorted function
def group_anagram(lst) -> list:
    d ={}
    for word in lst:
        ix = ''.join(sorted(word))
        if ix in d:
            d[ix].append(word)
        else:
            d[ix] = [word]
    return list(d.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )
print( group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )
print( group_anagram(["abc", "cba", "bac", "foo", "bar"]) )
print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )
print( group_anagram(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""