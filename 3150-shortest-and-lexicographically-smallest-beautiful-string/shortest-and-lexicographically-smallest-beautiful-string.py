class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=""
        for i in range(len(s)):
            one=0
            for j in range(i,len(s)):
                if s[j]=='1':
                    one+=1
                if k==one:
                    su=s[i:j+1]

                    if len(su)<len(ans) or ans=="" or(len(su)==len(ans)) and su<ans:
                        ans=su
                    break
                if one>k:
                    break
        return ans
                
                

        