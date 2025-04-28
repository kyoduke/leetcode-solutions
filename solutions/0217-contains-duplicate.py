from runpy import run_module
from typing import List

import test


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        content = {}
        l = 0
        r = len(nums) - 1

        while l < r:
            l_number = nums[l]
            r_number = nums[r]
            if l_number == r_number:
                return True
            if content.get(l_number) is not None or content.get(r_number) is not None:
                return True
            content[nums[l]] = l
            content[nums[r]] = r
            l += 1
            if l == (r - 1):
                if content.get(nums[l]) is not None:
                    return True
                break
            r -= 1
        return False


if __name__ == "__main__":
    s = Solution()

    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([0, 4, 5, 0, 3, 6], True),
        ([1000000000, 1000000000, 11], True),
        ([1, 5, -2, -4, 0], False),
    ]
    for testcase, expected in cases:
        result = s.containsDuplicate(testcase)
        print(f"Expected: {result} --- Result: {expected}")
