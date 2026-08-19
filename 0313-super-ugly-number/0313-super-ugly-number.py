import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        visited = set([1])

        count = 0

        while heap:
            val = heapq.heappop(heap)
            count += 1

            if count == n:
                return val

            for mult in primes:
                nxt = val * mult

                if nxt not in visited:
                    visited.add(nxt)
                    heapq.heappush(heap, nxt)