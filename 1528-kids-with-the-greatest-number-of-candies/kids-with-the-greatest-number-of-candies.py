class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c=candies[0]
        output=[]
        for i in range(len(candies)):
            max_c=max(max_c,candies[i])
        for i in range(len(candies)):
            output.append(max_c<=(candies[i]+extraCandies))
        return output
        