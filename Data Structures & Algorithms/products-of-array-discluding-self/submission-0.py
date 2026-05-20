class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1]*length
        left = 1
        for i in range(length):
            output[i] = left
            left *= nums[i]
        right = 1
        for i in range(length-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output