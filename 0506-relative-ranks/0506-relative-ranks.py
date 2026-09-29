class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(n, i) for i, n in enumerate(score)]
        score.sort(key=lambda x: x[0], reverse=True)

        op = [0] * len(score)

        for i in range(len(score)):
            if i == 0:
                op[score[i][1]] = 'Gold Medal'
            elif i == 1:
                op[score[i][1]] = 'Silver Medal'
            elif i == 2:
                op[score[i][1]] = 'Bronze Medal'
            else:
                op[score[i][1]] = f'{i + 1}'

        return op