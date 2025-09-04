class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<numRows or numRows==1:
            return s
        s1=[]
        s2=""
        count=0
        n=len(s)
        for i in range(1,numRows+1):
            s1.append(i)
            n-=1
        while n>0:
            if count==1:
                for i in range(2,numRows+1):
                    s1.append(i)
                    n-=1
                count-=1
            elif count==0:
                for i in range(numRows-1,0,-1):
                    s1.append(i)
                    n-=1
                count+=1
        for i in range(1,numRows+1):
            for j in range(0,len(s)):
                if i==s1[j]:
                    s2+=s[j]
        return s2
