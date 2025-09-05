class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=float("-inf")
        left=0
        right=len(height)-1
        while right>left:
            area=max(area,(right-left)*min(height[right],height[left]))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return area
        