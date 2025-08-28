class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            a=target-nums[i]
            if a in nums[i+1:]:
                l.append(i)
                break
        for j in range(i+1,len(nums)):
            if a==nums[j]:
                l.append(j)
        return l
        