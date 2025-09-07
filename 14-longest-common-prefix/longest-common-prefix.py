class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<=1:
            print(strs[0])
        j=1
        s=strs[0]
        while j<len(strs):
            s1=''
            for k in range(min(len(s),len(strs[j]))):
                if s[k]==strs[j][k]:
                    s1+=s[k]
                else:
                    break
            j+=1
            s=s1
        return s