class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sumMap: dict[int,int] = {}
        