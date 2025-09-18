class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        final=[]
        for i in range(len(positive)):
            final.append(positive[i])
            final.append(negative[i])
        return final
