class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0:-1}
        pre_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                pre_sum -= 1
            else:
                pre_sum += 1
            
            if pre_sum in count:
                ans = max(ans, i - count[pre_sum])
            else:
                count[pre_sum] = i
            
        return ans