class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        i=1
        s=''
        first=strs[i-1]
        second=strs[i]
        while i<len(strs):
            for j in range(min(len(first),len(second))):
                if first[j]==second[j]:
                    s+=first[j]
                else:
                    break
            first=s
            if i+1 < len(strs):
                second=strs[i+1]
                i+=1
            elif i+1>=len(strs):
                break
            s=''
        return first