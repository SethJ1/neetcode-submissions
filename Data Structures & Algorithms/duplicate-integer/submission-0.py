class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set(nums)
        if len(set(nums)) < len(nums):
            return True
        else:
            return False