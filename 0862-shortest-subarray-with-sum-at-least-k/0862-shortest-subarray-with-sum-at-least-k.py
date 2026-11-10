class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        
        # window based algo would have worked for non -ve numbers
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        result = n + 1

        for i in range(n + 1):

            # Find valid subarrays ending at i
            while dq and prefix[i] - prefix[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            # Maintain increasing prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return result if result <= n else -1