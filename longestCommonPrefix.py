class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longestPrefix = strs[0]
        for s in strs[1:]:
            # longest prefix
            formedPrefix = ""
            for i in range(len(s) + 1):
                if s[:i] == longestPrefix[:i]:
                    formedPrefix = s[:i]
            longestPrefix = formedPrefix
        return longestPrefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["aa", "a"]))
