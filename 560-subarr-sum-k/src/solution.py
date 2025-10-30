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


def main():
    sol: Solution = Solution()
    nums: list[int] = [2, 0, 1, 0, 1]
    k: int = 2
    rslt: int = sol.subarraySum(nums, k)
    print(rslt)


if __name__ == "__main__":
    main()
