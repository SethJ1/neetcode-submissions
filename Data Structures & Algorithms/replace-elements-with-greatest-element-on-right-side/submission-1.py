class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            old_value = arr[i]
            arr[i] = rightmax
            if old_value > rightmax:
                rightmax = old_value
        arr[-1] = -1
        return arr
