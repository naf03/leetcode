from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the candidates
        candidates.sort()
        resultSets = []
        currentSet = []
        runningSum = 0
        def dfs(i, currentSet, runningSum):
            if runningSum==target:
                resultSets.append(currentSet.copy())
                return 
            if i==len(candidates):
                return 
            if runningSum > target:
                return 
        
            currentSet.append(candidates[i])
            runningSum+=candidates[i]
            dfs(i+1, currentSet, runningSum)

            currentSet.pop()
            runningSum-=candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1] :
                i=i+1
            dfs(i+1, currentSet, runningSum)


        dfs(0,currentSet, runningSum)
        return resultSets
    


# candidates = [10,1,2,7,6,1,5]
# target = 8

candidates = [2,5,2,1,2]
target = 5

sol1 = Solution()
result = sol1.combinationSum2(candidates, target)
print(result)
