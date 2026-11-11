from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set remove duplicates
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

    # O(n) t&s 

    # One liner: return len(nums) != len(set(nums))
    # O(n^2) t: using enumerate() and check if val == values b4 it

solver = Solution()

test = [1, 2, 3, 2]

print(solver.hasDuplicate(test))
