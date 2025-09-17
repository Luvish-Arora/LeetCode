class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if 1 not in nums:
            return 0
        i=0
        j=1
        a=0
        count=1
        while j<len(nums):
            if nums[i]!=1:
                i+=1
                j+=1
            elif nums[i]==1 and nums[j]==1:
                count+=1
                j+=1
            elif nums[i]==1 and nums[j]==0:
                a=max(a,count)
                i=j+1
                j=i+1
                count=1
        a=max(a,count)
        return a