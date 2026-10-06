class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []

        def backtrack(i, curr):
            if len(curr) >= 2:
                res.append(curr[:])
            used = set()

            for j in range(i, n):
                if nums[j] in used:
                    continue
                if not curr or nums[j] >= curr[-1]:
                    used.add(nums[j])
                    curr.append(nums[j])
                    backtrack(j+1, curr)
                    curr.pop()
            return

        backtrack(0, [])
        return res