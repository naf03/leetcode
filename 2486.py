class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # use two pointers
        # iterate both strings, if there is a match, move the pointer on string s and t, otherwise, move the pointer on
        # t. If the pointers on S reaches the end of the string. Then the remaining string from the pointer needs to 
        # be appended to t.
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                continue
            if s[i]!=t[j]:
                i+=1
                continue
        if i==len(s):
            return len(t[j:])
        if j==len(t):
            return 0