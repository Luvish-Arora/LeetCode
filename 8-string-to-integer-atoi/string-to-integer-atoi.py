class Solution:
    def myAtoi(self, s: str) -> int:
        min_int=-2**31
        max_int=2**31 - 1
        i=0
        s1=""
        if len(s)==0:
            return 0
        while i<len(s):
            if s[i]==" ":
                i+=1
            else:
                break
        def num(s2,i,s1):
            while i<len(s):
                if s[i].isdigit()==True:
                    s1+=s[i]
                    i+=1
                else:
                    break
            return s1
        if len(s[i:])>0:
            if s[i]=="-" or s[i]=="+":
                s1+=s[i]
                i+=1
                s1=num(s[i:],i,s1)
                if len(s1)==1:
                    return 0
                else:
                    if int(s1)<min_int:
                        return min_int
                    elif int(s1)>max_int:
                        return max_int
                    else:
                        return int(s1)

            elif s[i].isdigit()==True:
                s1=num(s[i:],i,s1)
                if int(s1)>max_int:
                    return max_int
                else:
                    return int(s1)
            else:
                return 0

        else:
            return 0