class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        if a[0]=="-":
            return False
        if a==a[::-1]:
            return True
        else:
            return False
