class Solution:

    def backtrack(self, idx, matchsticks, sides, length):
    
        if idx == len(matchsticks):
            return True
   
        for j in range(4):
           
            if sides[j] + matchsticks[idx] <= length:
                sides[j] += matchsticks[idx]

                if self.backtrack(idx + 1, matchsticks, sides, length):
                    return True

                sides[j] -= matchsticks[idx]
        
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4
        sides = [0] * 4

        matchsticks.sort(reverse=True)

        return self.backtrack(0, matchsticks, sides, length)