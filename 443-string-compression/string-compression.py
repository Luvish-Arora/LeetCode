class Solution:
    def compress(self, chars: List[str]) -> int:
        r=0
        w=0
        count=0
        l=[]
        l1=[]
        while w<len(chars):
            if chars[r]==chars[w]:
                count+=1
                w+=1
            elif chars[r]!=chars[w]:
                l1.append(chars[r])
                l.append(count)
                r=w
                count=0
            if w==len(chars):
                l1.append(chars[r])
                l.append(count)
        s=''
        for i in range(len(l1)):
            s+=l1[i]
            if l[i]!=1:
                s+=str(l[i])
        for i in range(len(s)):
            if chars[i]!=s[i]:
                chars[i]=s[i]
        return len(s)