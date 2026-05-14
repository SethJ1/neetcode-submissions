class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        doubledsize = 2 * len(nums)
        ans = [0] * doubledsize

        for i in range(len(nums)):
            ans[i] = nums[i]
        
        for i in range(len(nums)):
            ans[i + len(nums)] = nums[i]
        
        return ans