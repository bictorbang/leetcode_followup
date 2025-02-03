class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [c for c in s.lower() if c.isalnum()]
        return palindrome == palindrome[::-1]