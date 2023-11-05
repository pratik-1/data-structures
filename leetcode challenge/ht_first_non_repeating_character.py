"""
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first
non-repeating character in the given string.
If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l"
because "l" is the first character that appears only once in the string.
.Similarly, if the input string is "hello", the function should return "h" because "h"
is the first non-repeating character in the string.
"""

def first_non_repeating_char(string) -> str:
    d = {}
    for i in string:
        d[i] = d.get(i,0)+1
    for k,v in d.items():
        if v==1:
            return k
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""




