class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        n=len(nums)
        nums[:]=nums[n-k:]+nums[:n-k]
        