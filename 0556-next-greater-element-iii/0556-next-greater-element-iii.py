class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)

        i = len(n) - 2

        while i >= 0 and n[i] >= n[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = len(n) - 1

        while n[j] <= n[i]:
            j -= 1

  
        nums = list(n)
        nums[i], nums[j] = nums[j], nums[i]

   
        nums[i + 1:] = sorted(nums[i + 1:])

        result = int(''.join(nums))

   
        if result > 2147483647:
            return -1

        return result