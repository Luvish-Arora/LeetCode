class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=''
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in s1:
                    s1+=s[j]
                elif s[j] in s1:
                    count=max(count,len(s1))
                    s1=''
                    break
        count=max(count,len(s1))
        return count