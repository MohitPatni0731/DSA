# https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=string&difficulty=EASY
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            new = ""
            find_min_length = []
            for t in strs:
                find_min_length.append(len(t))
            shortest_word_length = min(find_min_length)

            for i in range(shortest_word_length):
                if strs[0][i] == strs[1][i] == strs[2][i]:
                    new += strs[0][i]
                else:
                    break
            return new

# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_res = sorted(nums)
        for i in range(len(nums_res)-1):
            if len(nums_res) == 1:
                return False
            else:
                if nums_res[i] == nums_res[i+1]:
                    return (True)
                else:
                    i+=1
        return(False)

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack)):
            if haystack[index] == needle:
                return index
                break
        else:
            return -1

# https://leetcode.com/problems/group-anagrams/
# Took some time to figure out that we have to make new_temp array also in order to tackle repeated entries but this solution is not efficient so it is giving TLE on Leetcode so I am thinking of some other solution using dictonary
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = []
        new_temp = []  
        for i in range(len(strs)):
            new_one = []
            sorted_i = sorted(strs[i])
            if strs[i] not in new_temp:
                new_one.append(strs[i])
            for j in range(i+1, len(strs)):
                if sorted_i == sorted(strs[j]):
                    if strs[j] not in new_temp:
                        new_one.append(strs[j])
            if new_one:
                new.append(new_one)
                new_temp.extend(new_one)
                
        for word in strs:
            if word not in new_temp:
                new.append([word])
               
        return new
