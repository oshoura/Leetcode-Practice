class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longestStr = ""
        curLongestStr = ""
        while r < len(s):
            if s[r] not in s[l:r]:
                curLongestStr += s[r]
                r += 1
            else:
                if len(curLongestStr) > len(longestStr):
                    longestStr = curLongestStr
                curLongestStr = ""
                l += 1
                r = l
        return max(len(curLongestStr), len(longestStr))


