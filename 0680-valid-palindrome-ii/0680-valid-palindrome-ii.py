class Solution:
    def validPalindrome(self, s: str) -> bool:
        String = s
        Low = 0
        High = len(String) -1 

        while Low <= High:
            if String[Low] == String[High]:
                Low +=1
                High -= 1
            else:
                return String[Low:High] == String[Low:High][::-1] or String[Low+1:High+1] == String[Low+1:High+1][::-1]
        return True
