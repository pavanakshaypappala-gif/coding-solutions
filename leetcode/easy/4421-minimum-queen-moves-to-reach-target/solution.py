class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        a1 , b1 = source
        a2 , b2 = target
        if a1 == a2 and b1 == b2:
            return 0
        if a1 == a2 or b1 == b2 or abs(a1-a2) == abs(b1-b2):
            return 1
        return 2