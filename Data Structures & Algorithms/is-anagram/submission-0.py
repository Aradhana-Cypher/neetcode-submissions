class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            if len(s) == len(t):
                return True
        else:
            return False

