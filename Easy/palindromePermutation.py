class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        l = sorted(s)
        numOdd = 0
        even = False
        last = l[0]
        for s in l[1:]:
            if s == last:
                even = not even
            else:
                numOdd += 0 if even else 1
                even = False
            last = s
        numOdd += 0 if even else 1
        return True if numOdd <= 1 else False


print(Solution().canPermutePalindrome("hello"))
print(Solution().canPermutePalindrome("racecar"))
print(Solution().canPermutePalindrome("aab"))

