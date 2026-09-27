class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        di = []
        while nums:
            x = sorted(set(nums))
            for n in x:
                di.append(n)
                nums.remove(n)

        return di