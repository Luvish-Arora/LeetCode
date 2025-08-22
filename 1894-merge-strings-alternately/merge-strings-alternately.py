class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        i=0
        c=min(len(word1),len(word2))
        while i<c:
            word3+=word1[i]
            word3+=word2[i]
            i+=1
        word3+=word1[i:]
        word3+=word2[i:]
        return word3