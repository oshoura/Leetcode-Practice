class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0 and len(s) == 0:
            return True
        elif len(p) >= 2 and p[1] == "*":
            ##### 1+ occurance of char ## OR ## zero occurance of char#
            return self.isMatch(s, (p[0] + p)) or self.isMatch(s, p[2:])
        elif (len(s) >= 1  and len(p) >= 1) and (p[0] == "." or s[0] == p[0]):
            #first char is a . or it matches reduce and recur
            return self.isMatch(s[1:], p[1:])
        else:
            return False

import pickle

from functools import wraps
def memoize(func):
    cache = {}
    @wraps(func)
    def wrap(*args,**kwargs):
        key = pickle.dumps((args, kwargs))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrap

Solution.isMatch = memoize(Solution.isMatch)

print(Solution().isMatch("aa", "a"))