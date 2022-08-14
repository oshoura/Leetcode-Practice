class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(s):
            r,l = i, i
           