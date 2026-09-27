class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        a = 0
        dic ={}
        
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                a += 1
            else:
                p = tuple(sorted((nums[i],nums[i+1])))
                dic[p] = dic.get(p,0) + 1
            if dic:
                a += max(dic.values())
        return a