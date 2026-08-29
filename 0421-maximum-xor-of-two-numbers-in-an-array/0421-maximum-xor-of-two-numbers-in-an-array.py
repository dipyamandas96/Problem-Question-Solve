class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        max_xor = 0
        for i in range(32, -1, -1):
            #set each bit and printing
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    max_xor |= candidate
                    break

        return max_xor