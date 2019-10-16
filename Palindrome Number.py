# class Solution:
#     def isPalindrome(self, x: int) -> bool:
def isPalindrome(x):
    s = list(map(int,str(x)))
    l = len(s)
    for i in range(l // 2) :
        if s[i] == s[l-i-1]:
            return True

assert isPalindrome(121) == True
