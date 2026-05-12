class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter > output:
                    output = counter
            else:
                counter = 0
        return output

        