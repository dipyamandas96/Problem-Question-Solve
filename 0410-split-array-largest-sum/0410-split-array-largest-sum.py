class Solution:
    def canSplit(self, nums: list[int], k: int, maxSum: int) -> bool:
        subarrayCount = 1
        currentSum = 0

        for num in nums:
            if num > maxSum:
                return False
            if currentSum + num <= maxSum:
                currentSum += num
            else:
                subarrayCount += 1
                currentSum = num

        return subarrayCount <= k

    def splitArray(self, nums: list[int], k: int) -> int:
        start = 0
        end = sum(nums)
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2
            if self.canSplit(nums, k, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans