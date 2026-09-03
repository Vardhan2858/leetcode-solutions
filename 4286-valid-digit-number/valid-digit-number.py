class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        
        s=str(n)
        k=str(x)
        if k in s and s[0]!=k:
            return True
        return False 
