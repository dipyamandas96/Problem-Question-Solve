class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        G = gcd(p,q)
        p//= G
        q//= G
        
        return 2 if p%2 == 0 else q%2