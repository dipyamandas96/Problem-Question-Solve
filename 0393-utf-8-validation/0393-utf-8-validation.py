class Solution:
    def validUtf8(self, data: List[int]) -> bool:
      
        count = 0 
        for n in data:
            if count>0:
                if n>>6==0b10:
                    count -=1
                else:
                    return False 
            else:
                if n>>7==0b0:
                    count = 0 
                elif n>>5==0b110:
                    count = 1 
                elif n>>4==0b1110:
                    count = 2 
                elif n>>3==0b11110:
                    count = 3 
                else:
                    return False
        
        return True if count==0 else False