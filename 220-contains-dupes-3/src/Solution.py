from trees.RedBlackTree import RedBlackTree

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        tree: RedBlackTree = RedBlackTree()
        counts:dict[int,int] = {}
        
        for i in range(0, len(nums)):
            x:int = nums[i]
            candidate = tree.lower_bound_node(x-valueDiff)
            if candidate is not None and candidate.data <= x + valueDiff:
                return True
            counts[x] = counts.get(x, 0) + 1
            if counts[x] == 1:
                tree.insert(x)

            if i >= indexDiff:
                old_val = nums[i - indexDiff]
                counts[old_val] -= 1
                if counts[old_val] == 0:
                    del counts[old_val]
                    tree.remove(old_val)
        
        return False


def main():
    sol: Solution = Solution()
    raise NotImplementedError

if __name__ == '__main__':
    main()
  
