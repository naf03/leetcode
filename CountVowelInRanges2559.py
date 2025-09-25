# O(n^3)
# from typing import List
# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         results = []
#         vowels = ['a','e','i','o','u']
#         for q1, q2 in queries:
#             result = 0
#             for i in range(q1, q2+1):
#                 if words[i][0] in vowels and words[i][-1] in vowels:
#                     result+=1
#             results.append(result)
#         return results


from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        results = {}
        vowels = ['a','e','i','o','u']
        result = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                result+=1
            results[i]=result

        # print(results)
        finalResults = []
        for q1, q2 in queries:
            if q1==0:
                finalResults.append(results[q2])
            else:
                finalResults.append(results[q2]-results[q1-1])
        return finalResults



        

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
solution = Solution()
result = solution.vowelStrings(words, queries)
print(result)

