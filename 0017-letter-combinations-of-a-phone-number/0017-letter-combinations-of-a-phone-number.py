class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        hashmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def dfs(idx, cur):
            if idx == len(digits): 
                res.append(cur)
                return
            for letter in hashmap[digits[idx]]: 
                dfs(idx + 1, cur + letter)
        
        dfs(0, "")
        return res
            

                
        