class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        freq = [0] * (n + 1)
        result = [0, 0]

        # Count frequencies of each number
        for value in nums:
            freq[value] += 1

        # Find the duplicate and missing number
        for i in range(1, n + 1):
            if freq[i] == 2:
                result[0] = i  # Duplicate number
            elif freq[i] == 0:
                result[1] = i  # Missing number

        return result