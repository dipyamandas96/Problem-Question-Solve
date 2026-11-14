class Solution:
    def largestPalindrome(self, n: int) -> int:

        if n == 1:
            return 9
        
        min_num = 10 ** (n - 1)
    
        max_num = 10 ** n - 1       
        
        max_pal = 0
    
        for i in range(max_num, min_num - 1, -2): 
  
            if i * i < max_pal:
                break
                
            for j in range(max_num, i - 1, -2):
                product = i * j
            
                if product % 11 != 0 and product >= max_pal:
                    continue
                if str(product) == str(product)[::-1]:
                    max_pal = product

        return max_pal % 1337