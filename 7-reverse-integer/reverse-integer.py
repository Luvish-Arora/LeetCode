class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if x >= 0:
            s = 0
            x1 = str(x)
            for i in range(len(x1) - 1, -1, -1):
                s += int(x1[i]) * (10 ** i)
            return s if s <= INT_MAX else 0

        else:
            s = 0
            x1 = str(x)  
            for i in range(len(x1) - 1, 0, -1):
                s += int(x1[i]) * (10 ** (i - 1))
            s = -s
            return s if s >= INT_MIN else 0
