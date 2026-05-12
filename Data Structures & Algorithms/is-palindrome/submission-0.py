class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for v in s:
            if v.isalnum():
                newStr += v.lower()
        return newStr == newStr[::-1]