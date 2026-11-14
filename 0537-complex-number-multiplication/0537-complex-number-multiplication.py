class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=num1.split('+')
        num2=num2.split('+')
        a=int(num1[0])
        b=int(num2[0])
        c=int(num1[1][:-1]) 
        d=int(num2[1][:-1]) 
        res=''
        res+=str((a*b)-(c*d))
        res+='+'
        res+=str((a*d)+(b*c))
        res+='i'
        return res
    