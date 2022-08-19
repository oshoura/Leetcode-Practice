import sys

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        numsInReverseList = []
        tens = 1
        ##reverse to a list
        while x > 0:
            tens *= 10
            lastDig = x % tens
            numsInReverseList.append(lastDig / tens * 10)
            x -= lastDig

        ##compute into an int
        result = 0
        for n in numsInReverseList:
            tens /= 10
            result += n * tens
        return int(result * sign) if result < sys.maxint else 0
 
