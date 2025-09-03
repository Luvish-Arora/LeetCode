class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        i=0
        j=0
        s2=""
        while j<len(s):
            s1=s[i:j+1]
            if s1==s1[::-1] and len(s2)<len(s1):
                s2=s1
                j+=1
            elif j==len(s)-1:
                i+=1
                j=i+1
            else:
                j+=1
        return s2
            

