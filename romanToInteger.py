class Solution:
    def romanToInt(self, s: str) -> int:
        numeralToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = 0
        while i < len(s):
            if numeralToInt[s[i]] < numeralToInt[s[i + 1]] and i != len(s) - 1:
                sum += numeralToInt[s[i + 1]] - numeralToInt[s[i]]
                i += 2
            else:
                sum += numeralToInt[s[i]]
                i += 1
        return sum
