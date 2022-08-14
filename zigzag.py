class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for x in range(numRows)]
        down = True
        i = 0
        for c in s:
            result[i].append(c)
            if down:
                if i < numRows - 1:
                    i += 1
                else:
                    down = False
                    i -= 1
            else:
                if i <= 0:
                    down = True
                    i += 1
                else:
                    i -=1
        output = ''
        for l in result:
            for c in l:
                output += (c)
        return output





