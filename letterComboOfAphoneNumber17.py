from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mymap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        results = []
        current = []
        def helper(i, current):
            if i == len(digits):
                results.append("".join(current))
                return 
            letters = mymap[digits[i]]
            for j in range(len(letters)):
                current.append(letters[j])
                
                helper(i+1, current)
                current.pop()
                
        
        helper(0, current)
        return results
        
# digits = "34"
# solution = Solution()
# answer = solution.letterCombinations(digits)
# print(answer)