class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [c for c in s.lower() if c.isalnum()]
        l, r = 0, len(palindrome) - 1
        while l < r:
            if palindrome[l] == palindrome[r]:
                l += 1
                r -= 1    
            else:
                return False                
        return True