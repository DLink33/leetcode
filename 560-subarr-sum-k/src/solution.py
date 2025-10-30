class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if not nums:
            return 0

        prefixMap: dict[int, int] = {}
        prefixMap[0] = 1
        prefixSum: int = 0
        rslt: int = 0

        for num in nums:
            # compute curr running total at curr elem
            prefixSum += num

            # if we have found a prefix sum (a running sum at a previous index in the array)
            # whose value is the same as our current running sum minus k (meaning we have a prefix
            # whose value we can remove from our running sum to get k) add the number of count of
            # that prefix to our return value
            if (prefixSum - k) in prefixMap:
                rslt += prefixMap[prefixSum - k]

            # update our prefix map
            if prefixSum in prefixMap:
                prefixMap[prefixSum] += 1
            else:
                prefixMap[prefixSum] = 1

        return rslt

    def subPosArraySum(self, nums: list[int], k: int) -> int:
        left: int = 0
        right: int = 0
        windowSum: int = nums[0]
        rslt: int = 0

        while left < len(nums):
            if left > right:
                left = right
                windowSum = nums[left]

            if windowSum < k:
                right += 1
                if right == len(nums):
                    break
                windowSum += nums[right]
            elif windowSum > k:
                windowSum -= nums[left]
                left += 1
            else:
                rslt += 1
                windowSum -= nums[left]
                left += 1

        return rslt


def main():
    sol: Solution = Solution()
    nums: list[int] = [2, 0, 1, 0, 1]
    k: int = 2
    rslt: int = sol.subarraySum(nums, k)
    print(rslt)


if __name__ == "__main__":
    main()
