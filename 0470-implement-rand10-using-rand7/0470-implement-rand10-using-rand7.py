# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        curr = 40

        while curr >= 40:
            a, b = rand7(), rand7()
            curr = (a - 1) * 7 + (b - 1)

        return curr % 10 + 1