class Solution:
    def intToRoman(self, num: int) -> str:

        l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        l1 = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        s = ""
        i = 0

        while num > 0:
            if num >= l[i]:
                num -= l[i]
                s += l1[i]
            else:
                i += 1

        return s
