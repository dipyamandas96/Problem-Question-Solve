class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        ones = [i for i, digit in enumerate(s) if digit == '1']   
        
        if len(ones) < k: return ''

        cands = list(zip(ones,ones[k-1:]))                          
        minLen = min(r-l for l, r in cands)                       

        cands = list(filter(lambda x: x[1]-x[0] == minLen, cands))  

        return min([s[l:r+1] for l,r in cands])                  