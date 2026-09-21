class Solution:
    def findRadius(self, houses, heaters):
        n, m = len(houses), len(heaters)

        houses.sort()
        heaters.sort()

        def function(x):
            i, j = 0, 0 

            while j < m:
                while i < n and abs(houses[i]-heaters[j]) <= x:
                    i += 1
                j += 1 

            return i == n 
        

        low, high = 0, max(heaters[-1],houses[-1])

        while low <= high:
            mid = (low+high)//2 

            if function(mid):
                high = mid - 1 
            else:
                low = mid + 1 

        return low 