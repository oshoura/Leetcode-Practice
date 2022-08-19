class Solution:
    def longestPalindrome(self, s: str) -> str:
        longPalind = ""
        longestLen = 0
        for i in range(len(s)):
            #for odd
            l, r = i, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r-l+1) > longestLen:
                    longestLen = r-l+1
                    longPalind = s[l:r+1]
                r +=1
                l -=1
            
            #for even
            l, r = i, i+1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r-l+1) > longestLen:
                    longestLen = r-l+1
                    longPalind = s[l:r+1]
                r +=1
                l -=1
        return longPalind


      
    
print(Solution().longestPalindrome("babad"))

 # big o(n^3)

  # l = 0
        # r = 1
        # longestPalindrom = s[l:r]
        # longestLen = 1
        # while l + longestLen < len(s):
        #     r = l + longestLen + 1
        #     while r <= len(s):
        #         str = s[l:r]
        #         if str == str[::-1]:
        #             longestLen = r-l
        #             longestPalindrom = str[::-1]
        #         r +=1
        #     l+=1
                    
        # return longestPalindrom