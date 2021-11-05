"""
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Logic:

Use a temporary dictionary to store the encountered values
If current value is not in the dict:
    Add it to the dictionary 
    Append it to the current sub-string

currentLongestSubString = firstSubstring extracted
if len(futureSubstrings) > len(currentLongestSubString):
    currentLongestSubString = futureSubstring

return(currentLongestSubstring)

"""

letters = {}
word = "dvdf"
substring = ""
longest = ""

for x in word:
    if x in letters.keys(): # If a duplicate is encountered
        print("Duplicate")
        if len(substring) > len(longest):
            longest = substring
        # Clear substring and dict, start over from x
        substring = x
        letters = {}
        letters[x] = x
    else:
        print("New")
        letters[x] = x
        substring = substring + x
        longest = substring

print("Substring",longest)
print("Length:", len(longest))