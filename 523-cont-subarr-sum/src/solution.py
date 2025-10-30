class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        if k == 0:
            for a, b in zip(nums, nums[1:]):
                if a == b == 0:
                    return True
            return False

        if k < 0:
            k *= -1

        currSum: int = 0
        prefixMods: dict[int, int] = {0: -1}
        for i, num in enumerate(nums):
            currSum += num
            r: int = currSum % k

            if r in prefixMods:
                if i - prefixMods[r] >= 2:
                    return True
            else:
                prefixMods[r] = i

        return False


def main():
    pass


if __name__ == "__main__":
    main()
