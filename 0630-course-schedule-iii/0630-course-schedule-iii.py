class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []

        courses.sort(key=lambda x: x[1])

        ans = 0
        current_day = 1

        for dur, dead_l in courses:

            if current_day + dur - 1 <= dead_l:
                current_day += dur
                heappush(heap, -dur)
                ans += 1
            elif heap:
                d = -heap[0]  

                if current_day - d + dur - 1 <= dead_l and dur <= d:
                    current_day -= d
                    current_day += dur

                    heappop(heap)
                    heappush(heap, -dur)

        return ans