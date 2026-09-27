class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        a = 0

        for x in set(nums):
            b = [x if n==x else n for n in nums]
            for y in set(nums):
                if x!=y:
                    c=[y if n == x else n for n in nums]
                    co = 0
                    for i in range(len(c)-1):
                        if c[i] == b[i+1]:
                            co += 1
                    a = max(a,co)
        return a