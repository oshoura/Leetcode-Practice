'''
192938 -> 192938
hello -> 0
hi 89 -> 0
89 hi -> 89
-00098 -> 98
hi -009 -> 0
    9 -> 9
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        
        #isolating the number in str format
        num_str = ""
        neg = False
        num_started = False
        for c in s:
            if c == "-" and not num_started: 
                neg = True
                num_started = True
            elif c =="+" and not num_started:
                num_started = True
            elif isNum(c):
                num_str += c
                num_started = True
            elif isAllow(c) and num_started:
                break
            elif not isAllow(c):
                break
        dig = len(num_str)

        #reading  
        num = 0
        i = 0
        while (dig>0):
            num += char_num(num_str[i])*(10**(dig-1))
            dig -= 1
            i +=1
        num = num if neg==False else num*-1
        return clamp(num, -2**31, (2**31)-1)

            
def isAllow(c):
    return c in '0123456789- '

def isNum(c):
    return c in '0123456789'

def char_num(c):
    if c in " +-": return 0
    return ord(c) - ord('0')

def clamp(num, min_value, max_value):
        num = max(min(num, max_value), min_value)
        return num

print(Solution().myAtoi("+-12"))
