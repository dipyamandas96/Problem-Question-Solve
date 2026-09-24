import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self._radius = radius
        self._x_center = x_center
        self._y_center = y_center
        random.seed(1)

    def randPoint(self):
        t = random.random() * 2 * math.pi
        r = self._radius * max(random.random(), random.random())
        x = r * math.cos(t)
        y = r * math.sin(t)
        return [x + self._x_center, y + self._y_center]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()